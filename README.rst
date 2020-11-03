Introduction
============

A Linux Python wrapper for CKIP classic tools — `CKIP Word Segmentation <http://ckip.iis.sinica.edu.tw/project/wordsegment/>`__ and `CKIP Parser <http://ckip.iis.sinica.edu.tw/project/parser/>`__.

.. attention::
   Please use `CKIPNLP <https://ckipnlp.readthedocs.io/>`__ for structured data types and pipeline drivers.

.. attention::
   For Python 2 users, please use `PyCkip 0.4.2 <https://pypi.org/project/pyckip/0.4.2/>`__ instead.

Git
---

https://github.com/ckiplab/ckip-classic

|GitHub Version| |GitHub Release| |GitHub Issues|

.. |GitHub Version| image:: https://img.shields.io/github/v/release/ckiplab/ckip-classic.svg?maxAge=3600
   :target: https://github.com/ckiplab/ckip-classic/releases

.. |GitHub License| image:: https://img.shields.io/github/license/ckiplab/ckip-classic.svg?maxAge=3600
   :target: https://github.com/ckiplab/ckip-classic/blob/master/LICENSE

.. |GitHub Release| image:: https://img.shields.io/github/release-date/ckiplab/ckip-classic.svg?maxAge=3600

.. |GitHub Downloads| image:: https://img.shields.io/github/downloads/ckiplab/ckip-classic/total.svg?maxAge=3600
   :target: https://github.com/ckiplab/ckip-classic/releases/latest

.. |GitHub Issues| image:: https://img.shields.io/github/issues/ckiplab/ckip-classic.svg?maxAge=3600
   :target: https://github.com/ckiplab/ckip-classic/issues

.. |GitHub Forks| image:: https://img.shields.io/github/forks/ckiplab/ckip-classic.svg?style=social&label=Fork&maxAge=3600

.. |GitHub Stars| image:: https://img.shields.io/github/stars/ckiplab/ckip-classic.svg?style=social&label=Star&maxAge=3600

.. |GitHub Watchers| image:: https://img.shields.io/github/watchers/ckiplab/ckip-classic.svg?style=social&label=Watch&maxAge=3600

PyPI
----

https://pypi.org/project/ckip-classic

|PyPI Version| |PyPI License| |PyPI Downloads| |PyPI Python| |PyPI Implementation| |PyPI Status|

.. |PyPI Version| image:: https://img.shields.io/pypi/v/ckip-classic.svg?maxAge=3600
   :target: https://pypi.org/project/ckip-classic

.. |PyPI License| image:: https://img.shields.io/pypi/l/ckip-classic.svg?maxAge=3600
   :target: https://github.com/ckiplab/ckip-classic/blob/master/LICENSE

.. |PyPI Downloads| image:: https://img.shields.io/pypi/dm/ckip-classic.svg?maxAge=3600
   :target: https://pypi.org/project/ckip-classic#files

.. |PyPI Python| image:: https://img.shields.io/pypi/pyversions/ckip-classic.svg?maxAge=3600

.. |PyPI Implementation| image:: https://img.shields.io/pypi/implementation/ckip-classic.svg?maxAge=3600

.. |PyPI Format| image:: https://img.shields.io/pypi/format/ckip-classic.svg?maxAge=3600

.. |PyPI Status| image:: https://img.shields.io/pypi/status/ckip-classic.svg?maxAge=3600

Documentation
-------------

https://ckip-classic.readthedocs.io/

|ReadTheDocs Home|

.. |ReadTheDocs Home| image:: https://img.shields.io/website/https/ckip-classic.readthedocs.io.svg?maxAge=3600&up_message=online&down_message=offline
   :target: https://ckip-classic.readthedocs.io

Contributers
------------

* `Mu Yang <https://muyang.pro>`__ at `CKIP <https://ckip.iis.sinica.edu.tw>`__ (Author & Maintainer)
* `Wei-Yun Ma <https://www.iis.sinica.edu.tw/pages/ma/>`__ at `CKIP <https://ckip.iis.sinica.edu.tw>`__ (Maintainer)

External Links
--------------

- `Online Demo <https://ckip.iis.sinica.edu.tw/service/corenlp>`__

Requirements
------------

* `Python <https://www.python.org>`__ 3.5+
* `Cython <https://cython.org>`__ 0.29+

Note that one should have CKIPWS/CKIPParser for this project:

* `CKIP Word Segmentation <https://ckip.iis.sinica.edu.tw/project/ws/>`__ Linux version 20190524+

   - `Academic License <http://ckipsvr.iis.sinica.edu.tw/ckipws/reg.php>`__
   - `Commercial License <https://iptt.sinica.edu.tw/shares/405>`__

* `CKIP Parser <https://ckip.iis.sinica.edu.tw/project/parser/>`__ Linux version 20190725+

   - `Academic License <http://parser.iis.sinica.edu.tw/v1/reg.exe>`__ (Online Version)
   - `Commercial License <https://iptt.sinica.edu.tw/shares/447>`__

Installation
============

.. attention::

   - Offline version: CKIPWS (Academic/Commercial License) and CKIPParser (Commercial License).
   - Online version: CKIPParser (Academic License).

Offline Version
---------------

Download CKIPWS and/or CKIPParser from above links. Denote ``<ckipws-linux-root>`` as the folder containing CKIPWS, and ``<ckipparser-linux-root>`` as the folder containing CKIPParser.

.. code-block:: bash

   pip install --force-reinstall --upgrade ckip-classic \
      --install-option='--ws' \
      --install-option='--ws-dir=<ckipws-linux-root>' \
      --install-option='--parser' \
      --install-option='--parser-dir=<ckipparser-linux-root>'

Ignore ws/parser options if one doesn't have CKIPWS/CKIPParser.

.. attention::
   Please use absolute paths.

Online Version
--------------

Register an account at `http://parser.iis.sinica.edu.tw/v1/reg.exe`

.. code-block:: bash

   pip install --force-reinstall --upgrade ckip-classic \
      --install-option='--no-ws' \
      --install-option='--no-parser'

Installation Options
--------------------

+-----------------------------------------------+---------------------------------------+-------------------------------+
| Option                                        | Detail                                | Default Value                 |
+===============================================+=======================================+===============================+
| ``--[no-]ws``                                 | Enable/disable CKIPWS.                | False                         |
+-----------------------------------------------+---------------------------------------+-------------------------------+
| ``--[no-]parser``                             | Enable/disable CKIPParser.            | False                         |
+-----------------------------------------------+---------------------------------------+-------------------------------+
| ``--ws-dir=<ws-dir>``                         | CKIPWS root directory.                |                               |
+-----------------------------------------------+---------------------------------------+-------------------------------+
| ``--ws-lib-dir=<ws-lib-dir>``                 | CKIPWS libraries directory            | ``<ws-dir>/lib``              |
+-----------------------------------------------+---------------------------------------+-------------------------------+
| ``--ws-share-dir=<ws-share-dir>``             | CKIPWS share directory                | ``<ws-dir>``                  |
+-----------------------------------------------+---------------------------------------+-------------------------------+
| ``--parser-dir=<parser-dir>``                 | CKIPParser root directory.            |                               |
+-----------------------------------------------+---------------------------------------+-------------------------------+
| ``--parser-lib-dir=<parser-lib-dir>``         | CKIPParser libraries directory        | ``<parser-dir>/lib``          |
+-----------------------------------------------+---------------------------------------+-------------------------------+
| ``--parser-share-dir=<parser-share-dir>``     | CKIPParser share directory            | ``<parser-dir>``              |
+-----------------------------------------------+---------------------------------------+-------------------------------+
| ``--data2-dir=<data2-dir>``                   | "Data2" directory                     | ``<ws-share-dir>/Data2``      |
+-----------------------------------------------+---------------------------------------+-------------------------------+
| ``--rule-dir=<rule-dir>``                     | "Rule" directory                      | ``<parser-share-dir>/Rule``   |
+-----------------------------------------------+---------------------------------------+-------------------------------+
| ``--rdb-dir=<rdb-dir>``                       | "RDB" directory                       | ``<parser-share-dir>/RDB``    |
+-----------------------------------------------+---------------------------------------+-------------------------------+

Usage
=====

See https://ckip-classic.readthedocs.io/ for API details.

CKIPWS
------

CKIP Word Segmentation offline driver.

.. code-block:: python

   import ckip_classic.ws
   print(ckip_classic.__name__, ckip_classic.__version__)

   ws = ckip_classic.ws.CkipWs(logger=False)
   print(ws('中文字喔'))
   for l in ws.apply_list(['中文字喔', '啊哈哈哈']): print(l)

   ws.apply_file(ifile='sample/sample.txt', ofile='output/sample.tag', uwfile='output/sample.uw')
   with open('output/sample.tag') as fin:
       print(fin.read())
   with open('output/sample.uw') as fin:
       print(fin.read())


CKIPParser
----------

CKIP Parser offline driver.

.. code-block:: python

   import ckip_classic.parser
   print(ckip_classic.__name__, ckip_classic.__version__)

   ps = ckip_classic.parser.CkipParser(logger=False)
   print(ps('中文字喔'))
   for l in ps.apply_list(['中文字喔', '啊哈哈哈']): print(l)

   ps.apply_file(ifile='sample/sample.txt', ofile='output/sample.tree')
   with open('output/sample.tree') as fin:
       print(fin.read())


CKIPParserClient
----------------

CKIP Parser online client.

.. code-block:: python

   import ckip_classic.client
   print(ckip_classic.__name__, ckip_classic.__version__)

   ps = ckip_classic.client.CkipParserClient(username='USERNAME', password='PASSWORD')
   print(ps('中文字(Na)　耶(T)　，(COMMACATEGORY)'))
   for l in ps.apply_list(['中文字(Na)　耶(T)　，(COMMACATEGORY)', '啊(I)　哈(D)　哈(D)　哈(D)　。(PERIODCATEGORY)']): print(l)


FAQ
===

.. danger::

   Due to C code implementation, both ``CkipWs`` and ``CkipParser`` can only be instance once.

------------

.. warning::

   CKIPParser fails if input text contains special characters such as ``()+-:|``. One may replace these characters by

   .. code-block:: python

      text = text
         .replace('(', '（')
         .replace(')', '）')
         .replace('+', '＋')
         .replace('-', '－')
         .replace(':', '：')
         .replace('|', '｜')

------------

.. tip::

   **fatal error: Python.h: No such file or directory". What should I do?**

   Install Python development package

   .. code-block:: bash

      sudo apt-get install python3-dev

------------

.. tip::

   **The CKIPWS throws "what():  locale::facet::_S_create_c_locale name not valid". What should I do?**

   Install locale data.

   .. code-block:: bash

      apt-get install locales-all

------------

.. tip::

   **The CKIPParser throws "ImportError: libCKIPParser.so: cannot open shared object file: No such file or directory". What should I do?**

   Add below command to ``~/.bashrc``:

   .. code-block:: bash

      export LD_LIBRARY_PATH=<ckipparser-linux-root>/lib:$LD_LIBRARY_PATH

License
=======

|CC BY-NC-SA 4.0|

Copyright (c) 2018-2020 `CKIP Lab <https://ckip.iis.sinica.edu.tw>`__ under the `CC BY-NC-SA 4.0 License <http://creativecommons.org/licenses/by-nc-sa/4.0/>`__.

.. |CC BY-NC-SA 4.0| image:: https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png
   :target: http://creativecommons.org/licenses/by-nc-sa/4.0/
