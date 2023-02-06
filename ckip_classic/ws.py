#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Mu Yang <http://muyang.pro>'
__copyright__ = '2018-2023 CKIP Lab'
__license__ = 'GPL-3.0'

import os as _os

try:
    if not _os.environ.get('_SPHINX'):
        from ckip_classic._core.ws import CkipWsCore
except ImportError as exc:  # pragma: no cover
    raise ImportError(  # pragma: no cover
        'Please reinstall ‘ckip-classic’ with ‘--install-option=\'--ws\' --install-option=\'--ws-dir=<...>\'’. '
        'Visit https://pypi.org/project/ckip-classic for more information.'
    ) from exc

from ckip_classic.ini import create_ws_lex, create_ws_ini

class CkipWs:
    """The CKIP word segmentation driver.

    Parameters
    ----------
        logger : bool
            enable logger.
        lex_list : Iterable
            passed to :meth:`ckip_classic.ini.create_ws_lex`
            overridden **lex_file** for :meth:`ckip_classic.ini.create_ws_ini`.
        ini_file : str
            the path to the INI file.

    Other Parameters
    ----------------
        **
            the configs for CKIPWS, passed to :meth:`ckip_classic.ini.create_ws_ini`, ignored if **ini_file** is set.

    .. danger::
        Never instance more than one object of this class!
    """

    def __init__(self, *,
        logger=False,
        ini_file=None,
        lex_list=None,
        **kwargs,
    ):

        self.__core = CkipWsCore()

        if logger:
            self.__core.enable_logger()  # pragma: no cover

        if lex_list:
            lex_file, f_lex = create_ws_lex(*lex_list)
            kwargs['lex_file'] = lex_file

        if not ini_file:
            ini_file, f_ini, kwargs = create_ws_ini(**kwargs)

        def CkipWs(*, _=None): pass  # pylint: disable=redefined-outer-name, invalid-name, multiple-statements
        CkipWs(**kwargs)

        self.__core.init_data(ini_file)

        try:
            f_lex.close()
        except:  # pylint: disable=bare-except  # pragma: no cover
            pass  # pragma: no cover

        try:
            f_ini.close()
        except:  # pylint: disable=bare-except  # pragma: no cover
            pass  # pragma: no cover

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
        return self.apply_list([text])[0]

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
        return self.__core.apply_list(ilist)

    def apply_file(self, ifile, ofile, uwfile=''):
        """Segment a file.

        Parameters
        ----------
            ifile : str
                the input file.
            ofile : str
                the output file (will be overwritten).
            uwfile : str
                the unknown word file (will be overwritten).
        """
        return self.__core.apply_file(ifile, ofile, uwfile)
