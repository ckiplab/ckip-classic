#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Mu Yang <http://muyang.pro>'
__copyright__ = '2018-2020 CKIP Lab'
__license__ = 'GPL-3.0'

import os
import tempfile

from ckip_classic.ws import CkipWs

sample_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'file')

################################################################################################################################

ws = CkipWs(new_style_format=True, lex_list=[('哈哈哈', 'T')])

text_in = [
    '中文字耶，啊哈哈哈。',
    '「完蛋了！」畢卡噌他想',
]

def test_apply():
    text_out = ws(text_in[0])
    assert text_out == '中文字(Na)　耶(T)　，(COMMACATEGORY)　啊(I)　哈哈哈(T)　。(PERIODCATEGORY)'

def test_apply_list():
    text_out = ws.apply_list(text_in)
    assert text_out == [
        '中文字(Na)　耶(T)　，(COMMACATEGORY)　啊(I)　哈哈哈(T)　。(PERIODCATEGORY)',
        '「(PARENTHESISCATEGORY)　完蛋(VH)　了(T)　！(EXCLAMATIONCATEGORY)　」(PARENTHESISCATEGORY)　畢卡噌(Nb)　他(Nh)　想(VE)',
    ]

def test_apply_file():
    tmpdir = tempfile.TemporaryDirectory()
    ws.apply_file(
        ifile=f'{sample_path}/sample.txt',
        ofile=f'{tmpdir.name}/output.tag',
        uwfile=f'{tmpdir.name}/output.uw',
    )

    assert open(f'{sample_path}/sample.tag').read() == open(f'{tmpdir.name}/output.tag').read()
    assert open(f'{sample_path}/sample.uw').read() == open(f'{tmpdir.name}/output.uw').read()
