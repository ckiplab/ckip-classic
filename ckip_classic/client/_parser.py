#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Mu Yang <http://muyang.pro>'
__copyright__ = '2018-2023 CKIP Lab'
__license__ = 'GPL-3.0'

import json
import socket
import time

################################################################################################################################

class CkipParserSocket:

    def __init__(self, *, username, password, host='140.109.20.151', port=9998):

        self.username = username
        self.password = password
        self.host = host
        self.port = port

    def __call__(self, text):

        # Payload
        payload = dict(
            text=text.strip(),
            user=self.username,
            pwd=self.password,
            ws=str(True),
        )
        retry = 3

        # Communication
        response = []
        data = self.communicate(self.host, self.port, payload, retry)
        if data is not None:
            response = data.strip().replace('\r\n', '\n').split('\n')

        return response

    def communicate(self, host, port, payload, retry):
        data = None

        for i in range(retry):
            try:
                client = self.connect(host, port)
                client = NonBlockingWocket(client)
                client.send(payload)
                data = client.receive()
                client.close()
                break
            except:  # pylint: disable=bare-except
                time.sleep(5 * (i + 1))

        return data

    @staticmethod
    def connect(host, port):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        client.connect((host, port,))
        return client

################################################################################################################################

class NonBlockingWocket:

    def __init__(self, client, buffer=4096):
        self.buffer = buffer
        self.client = client

    def get_iters(self, data):
        try:
            field = data.split(':', 1)
            length = int(field[0])
            if len(data) == self.buffer:
                iters = int(length / self.buffer) + 1
            else:
                iters = int(length / self.buffer)
        except:  # pylint: disable=bare-except
            iters = None
        return iters

    def receive(self):
        self.client.setblocking(0)

        count = 0
        data = bytes()
        first = True
        iters = None

        while True:
            try:
                request = self.client.recv(self.buffer)
                if not request:
                    time.sleep(0.05)
                    continue
            except:  # pylint: disable=bare-except
                continue
            if first:
                first = False
                iters = self.get_iters(request.decode('utf-8'))
                if iters is None:
                    break
                data = request
            else:
                data += request
                count += 1
            if count == iters:
                break
        try:
            data = self.decapsulate(data)
        except:  # pylint: disable=bare-except
            data = None

        return data

    def send(self, data):
        data = self.encapsulate(data)
        self.client.sendall(data)

    def close(self):
        self.client.close()

    @staticmethod
    def encapsulate(data):
        jsno_data = json.dumps(data)
        length = str(len(jsno_data))
        pack_data = f'{length}:{jsno_data}'
        pack_data = pack_data.encode('utf-8', errors='ignore')
        return pack_data

    @staticmethod
    def decapsulate(data):
        data = data.decode('utf-8', errors='ignore')
        jsno_data = data.split(':', 1)[1]
        info = json.loads(jsno_data)
        return info
