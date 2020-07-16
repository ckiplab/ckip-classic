#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Mu Yang <http://muyang.pro>'
__copyright__ = '2018-2020 CKIP Lab'
__license__ = 'CC BY-NC-SA 4.0'

import os
import tempfile

from ckip_classic.parser import CkipParser

sample_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'file')

################################################################################################################################

parser = CkipParser(new_style_format=True, lex_list=[('哈哈哈', 'T')])

text_in = [
    '中文字耶，啊哈哈哈。',
    '「完蛋了！」畢卡噌他想',
]

def test_apply():
    text_out = parser(text_in[0])
    assert text_out == '#1:1.[0] %(property:Nab:中文字|particle:Td:耶|property:COMMACATEGORY:，|particle:I:啊|particle:T:哈哈哈)#'

def test_apply_list():
    text_out = parser.apply_list(text_in)
    assert text_out == [
        '#1:1.[0] %(property:Nab:中文字|particle:Td:耶|property:COMMACATEGORY:，|particle:I:啊|particle:T:哈哈哈)#',
        '#2:1.[0] %(property:VH11:完蛋|particle:Ta:了|property:EXCLAMATIONCATEGORY:！|property:Nb:畢卡噌|agent:Nhaa:他|property:VE2:想)#',
    ]

def test_apply_file():
    tmpdir = tempfile.TemporaryDirectory()
    parser.apply_file(
        ifile=f'{sample_path}/sample.txt',
        ofile=f'{tmpdir.name}/output.parse',
    )

    assert open(f'{sample_path}/sample.parse').read() == open(f'{tmpdir.name}/output.parse').read()
