#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Mu Yang <http://muyang.pro>'
__copyright__ = '2018-2023 CKIP Lab'
__license__ = 'GPL-3.0'

import os as _os
import warnings as _warnings

from ._parser import CkipParserSocket

################################################################################################################################

class CkipParserClient:
    """The CKIP sentence parsing client.

    Parameters
    ----------
        username : str
            the username (default to the environment variable ``$CKIPPARSER_USERNAME``).
        password : str
            the password (default to the environment variable ``$CKIPPARSER_PASSWORD``).

    Note
    ----
        One may register an account at http://parser.iis.sinica.edu.tw/v1/reg.exe

    """

    def __init__(self, *,
            username=_os.getenv('CKIPPARSER_USERNAME'),
            password=_os.getenv('CKIPPARSER_PASSWORD'),
        ):

        if username is None:
            raise RuntimeError('Username not specified.')
        if password is None:
            raise RuntimeError('Password not specified.')

        self.socket = CkipParserSocket(username=username, password=password)

    def __call__(self, text):
        return self.apply(text)

    def apply(self, text):
        """Parse a sentence.

        Parameters
        ----------
            text : str
                the input sentence.

        Returns
        -------
            str
                the output sentence.

        .. hint::
            One may also call this method as :meth:`__call__`.
        """
        res = self.socket(text)[0]
        if res == 'Account Error':
            raise RuntimeError('Invalid Username/Password')
        return self.socket(text)[0]

    def apply_list(self, ilist):
        """Parse a list of sentences.

        Parameters
        ----------
            ilist : List[str]
                the list of input sentences.

        Returns
        -------
            List[str]
                the list of output sentences.
        """
        res = []
        for itext in ilist:
            res += self.socket(itext)
        return res
