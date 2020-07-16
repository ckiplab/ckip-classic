#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Mu Yang <http://muyang.pro>'
__copyright__ = '2018-2020 CKIP Lab'
__license__ = 'CC BY-NC-SA 4.0'

from setuptools import dist
dist.Distribution().fetch_build_eggs([
    'Cython>=0.29',
])

################################################################################

import os
import sys
import warnings

from distutils.version import StrictVersion
import setuptools

assert StrictVersion(setuptools.__version__) >= StrictVersion('40.0'), \
    'Please update setuptools to 40.0+ using `pip install -U setuptools`.'

################################################################################

from setuptools import setup, find_namespace_packages
from setuptools.extension import Extension
from setuptools.command.install import install
from setuptools.command.develop import develop
from Cython.Build import cythonize

import ckip_classic as about

################################################################################

def main():

    with open('README.rst', encoding='utf-8') as fin:
        readme = fin.read()

    setup(
        name='ckip-classic',
        version=about.__version__,
        author=about.__author_name__,
        author_email=about.__author_email__,
        description=about.__description__,
        long_description=readme,
        long_description_content_type='text/x-rst',
        url=about.__url__,
        download_url=about.__download_url__,
        platforms=['linux_x86_64'],
        license=about.__license__,
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3 :: Only',
            'Programming Language :: Cython',
            'License :: Free for non-commercial use',
            'Operating System :: POSIX :: Linux',
            'Natural Language :: Chinese (Traditional)',
        ],
        python_requires='>=3.5',
        packages=find_namespace_packages(include=['ckip_classic', 'ckip_classic.*',]),
        ext_modules=cythonize(
            [
                Extension('ckip_classic._core.ws',
                    sources=['src/ws/ckipws.pyx'],
                    libraries=['WordSeg'],
                    language='c++',
                ),
                Extension('ckip_classic._core.parser',
                    sources=['src/parser/ckipparser.pyx'],
                    libraries=['CKIPCoreNLP', 'CKIPParser', 'CKIPWS', 'CKIPSRL'],
                    language='c++',
                ),
            ],
            build_dir='build',
        ),
        data_files=[],
        cmdclass={
            'install': InstallCommand,
            'develop': DevelopCommand,
        },
    )

################################################################################

def os_environ_append(name, dirpath):
    if name in os.environ:
        os.environ[name] += os.pathsep + dirpath
    else:
        os.environ[name] = dirpath

def os_environ_prepend(name, dirpath):
    if name in os.environ:
        os.environ[name] = dirpath + os.pathsep + os.environ[name]
    else:
        os.environ[name] = dirpath

class CommandMixin:

    user_options = [
        ('ws',        None, 'with CKIPWS [default]'),
        ('parser',    None, 'with CKIPParser [default]'),
        ('no-ws',     None, 'without CKIPWS'),
        ('no-parser', None, 'without CKIPParser'),

        ('ws-dir=',       None, 'CKIPWS root directory'),
        ('ws-lib-dir=',   None, 'CKIPWS libraries directory [default is <ws-dir>/lib]'),
        ('ws-share-dir=', None, 'CKIPWS share directory [default is <ws-dir>]'),

        ('parser-dir=',       None, 'CKIPParser root directory'),
        ('parser-lib-dir=',   None, 'CKIPParser libraries directory [default is "<parser-dir>/lib"]'),
        ('parser-share-dir=', None, 'CKIPWS share directory [default is "<parser-dir>"]'),

        ('data2-dir=', None, 'CKIPWS "Data2" directory [default is "<ws-share-dir>/Data2" or "<parser-share-dir>/Data2"]'),
        ('rule-dir=',  None, 'CKIPParser "Rule" directory [default is "<parser-share-dir>/Rule"]'),
        ('rdb-dir=',   None, 'CKIPParser "RDB" directory [default is "<parser-share-dir>/RDB"]'),
    ]

    negative_opt = {
        'no-ws':     'ws',
        'no-parser': 'parser',
    }

    def initialize_options(self):
        self.ws     = False
        self.parser = False

        self.ws_dir       = None
        self.ws_lib_dir   = None
        self.ws_share_dir = None

        self.parser_dir       = None
        self.parser_lib_dir   = None
        self.parser_share_dir = None

        self.data2_dir = None
        self.rule_dir  = None
        self.rdb_dir   = None

        super(CommandMixin, self).initialize_options()

    def finalize_options(self):

        # subdirectory
        opt_subdirectory = [
            ('ws_lib_dir',       'ws_dir',     'lib',),
            ('ws_share_dir',     'ws_dir',     '',),
            ('parser_lib_dir',   'parser_dir', 'lib',),
            ('parser_share_dir', 'parser_dir', '',),

            ('data2_dir', 'ws_share_dir',     'Data2',),
            ('data2_dir', 'parser_share_dir', 'Data2',),
            ('rule_dir',  'parser_share_dir', 'Rule',),
            ('rdb_dir',   'parser_share_dir', 'RDB',),
        ]
        for opt0, opt1, subdir in opt_subdirectory:
            dir0 = getattr(self, opt0)
            dir1 = getattr(self, opt1)
            if not dir0 and dir1:
                setattr(self, opt0, os.path.join(dir1, subdir))

        # directory
        opt_directory = [
            'ws_lib_dir',
            'parser_lib_dir',
            'data2_dir',
            'rule_dir',
            'rdb_dir',
        ]
        for opt0 in opt_directory:
            dir0 = getattr(self, opt0)
            if dir0 and not os.path.isdir(dir0):
                raise IOError('--%s (%s) is not a directory' % (opt0.replace('_', '-'), dir0,))

        super(CommandMixin, self).finalize_options()

    def run(self):

        name2mod = {em.name: em for em in self.distribution.ext_modules}

        # CKIPWS
        if self.ws:
            print('- Enable CKIPWS support')
            if self.ws_lib_dir:
                print('- Use CKIPWS library from "%s"' % self.ws_lib_dir)
                mod_ws = name2mod['ckip_classic._core.ws']
                mod_ws.library_dirs.append(self.ws_lib_dir)
                mod_ws.runtime_library_dirs.append(self.ws_lib_dir)
                for lib in mod_ws.libraries:
                    libfile = os.path.join(self.ws_lib_dir, f'lib{lib}.so')
                    if not os.path.exists(libfile):
                        print('  - [WARNING] Shared library not exist: %s' % libfile)
        else:
            print('- Disable CKIPWS support')
            del name2mod['ckip_classic._core.ws']

        # CKIPParser
        if self.parser:
            print('- Enable CKIPParser support')
            if self.parser_lib_dir:
                print('- Use CKIPParser library from "%s"' % self.parser_lib_dir)
                mod_parser = name2mod['ckip_classic._core.parser']
                mod_parser.library_dirs.append(self.parser_lib_dir)
                mod_parser.runtime_library_dirs.append(self.parser_lib_dir)
                for lib in mod_parser.libraries:
                    libfile = os.path.join(self.parser_lib_dir, f'lib{lib}.so')
                    if not os.path.exists(libfile):
                        print('  - [WARNING] Shared library not exist: %s' % libfile)
        else:
            print('- Disable CKIPParser support')
            del name2mod['ckip_classic._core.parser']

        # Re-register modules
        self.distribution.ext_modules = list(name2mod.values())

        # Data
        if self.data2_dir:
            print('- Use "Data2" from "%s"' % self.data2_dir)
            self.data_files('share/ckip_classic/Data2/', self.data2_dir)

        if self.rule_dir:
            print('- Use "Rule" from "%s"' % self.rule_dir)
            self.data_files('share/ckip_classic/Rule/', self.rule_dir)

        if self.rdb_dir:
            print('- Use "RDB" from "%s"' % self.rdb_dir)
            self.data_files('share/ckip_classic/RDB/', self.rdb_dir)

        # Python packages
        # self.distribution.packages = list(self.distribution.package_dir.keys())

        super(CommandMixin, self).run()

    def data_files(self, prefix, dirtop):
        count = 0
        for dirpath, _, files in os.walk(dirtop):
            count += len(files)
            self.distribution.data_files.append((
                os.path.join(prefix, os.path.relpath(dirpath, dirtop)),
                [os.path.join(dirpath, file) for file in files],
            ))
        print('  - Found %s files' % count)

class InstallCommand(CommandMixin, install):
    user_options = install.user_options + CommandMixin.user_options
    negative_opt = install.negative_opt
    negative_opt.update(CommandMixin.negative_opt)

    def __init__(self, *args, **kwargs):
        install.__init__(self, *args, **kwargs)

class DevelopCommand(CommandMixin, develop):
    user_options = develop.user_options + CommandMixin.user_options
    negative_opt = develop.negative_opt
    negative_opt.update(CommandMixin.negative_opt)

    def __init__(self, *args, **kwargs):
        develop.__init__(self, *args, **kwargs)

################################################################################

if __name__ == '__main__':
    main()
