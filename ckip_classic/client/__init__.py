#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Mu Yang <http://muyang.pro>'
__copyright__ = '2018-2020 CKIP Lab'
__license__ = 'CC BY-NC-SA 4.0'

from ._parser import CkipParserSocket

################################################################################################################################

class CkipParserClient:
    """The CKIP sentence parsing client.

    Parameters
    ----------
        username : str
            the username.
        password : str
            the password.

    Note
    ----
        One may register an account at http://parser.iis.sinica.edu.tw/v1/reg.exe

    """

    def __init__(self, *, username, password):
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
