#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Mu Yang <http://muyang.pro>'
__copyright__ = '2018-2020 CKIP Lab'
__license__ = 'CC BY-NC-SA 4.0'

import os

from ckip_classic.client import CkipParserClient

################################################################################################################################

parser = CkipParserClient()

text_in = [
    '中文字(Na)　耶(T)　，(COMMACATEGORY)',
    '啊(I)　哈(D)　哈(D)　哈(D)　。(PERIODCATEGORY)',
]

def test_apply():
    text_out = parser(text_in[0])
    assert text_out == '#1:1.[0] S(Head:Nab:中文字|particle:Td:耶)#，(COMMACATEGORY)'

def test_apply_list():
    text_out = parser.apply_list(text_in)
    print(text_out)
    assert text_out == [
        '#1:1.[0] S(Head:Nab:中文字|particle:Td:耶)#，(COMMACATEGORY)',
        '#1:1.[0] %(particle:interjection(Head:I:啊)|time:Dh:哈|time:Dh:哈|time:Dh:哈)#。(PERIODCATEGORY)',
    ]
