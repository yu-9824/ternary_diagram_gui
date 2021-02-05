"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup, find_packages
from shutil import copyfile
import os
import sys

# 再帰回数に引っかかるのでとりあえず大きい数に．
sys.setrecursionlimit(10 ** 9)


VERSION = '0.1.0'
VERSION_PYTHON = '{0}.{1}'.format(sys.version_info.major, sys.version_info.minor)
APP_NAME = 'ternary_diagram'
DESCRIPTION = 'Making ternary diagram.'
AUTHOR = 'yu-9824'
ID = 'yu-9824'
EMAIL = '{0}@{1}'.format('yu.9824', 'gmail.com')

# py2app用の変数
SRC = ['gui/main.py']
DATA_FILES = [
    ('img', ['gui/img/w_o_z.png', 'gui/img/w_z.png'])
]
ICON = os.path.join('gui', 'icon', '{}.icns'.format(APP_NAME))
PKGS = ['pandas', 'numpy', 'matplotlib', 'element_recognition', 'ternary_diagram']


# 諸変数・定数の定義
lib_path = os.path.join(os.environ['CONDA_PREFIX'], 'lib')
fname_libpython = 'libpython{}.dylib'.format(VERSION_PYTHON)

# libpython3.7.m.dylibだとエラーになるのであらかじめコピーしておく．
path_original = os.path.join(lib_path, 'libpython{}m.dylib'.format(VERSION_PYTHON))
path_converted = os.path.join(lib_path, fname_libpython)
if os.path.exists(path_original) and not os.path.exists(path_converted):
    copyfile(path_original, path_converted)

# 諸変数の準備
dylib_files = [os.path.join(lib_path, f) for f in os.listdir(lib_path) if '.dylib' in f]
contents_path = os.path.join('dist', '{}.app'.format(APP_NAME), 'Contents')
frameworks_path = os.path.join(contents_path, 'Frameworks')

OPTIONS = {
    'argv_emulation': False,
    'packages': PKGS,
    'iconfile': ICON,
    'plist':{
        'PyRuntimeLocations':[
            '@executable_path/../Frameworks/{}'.format(fname_libpython),
            os.path.join(lib_path, fname_libpython),
        ],
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': DESCRIPTION,
        'CFBundleIdentifier': "com.{0}.osx.{1}".format(ID, APP_NAME),
        'CFBundleVersion': VERSION,
        'CFBundleShortVersionString': VERSION,
        'NSHumanReadableCopyright': u"Copyright © 2020-, {}".format(AUTHOR)
    },
    # 'frameworks': dylib_files,
}

setup(
    name = APP_NAME,
    app = SRC,
    author = AUTHOR,
    author_email = EMAIL,
    version = VERSION,
    data_files = DATA_FILES,
    options = {'py2app': OPTIONS},
    setup_requires = ['py2app'],
    url = 'https://github.com/{0}/{1}'.format(ID, APP_NAME),
)