from setuptools import find_packages, setup

from {{package}} import __version__, config

import os
from os.path import (realpath, dirname, abspath, isdir, join)

def files_whitelist(module_name):
    base = join(dirname(abspath(__file__)), module_name)
    modules = filter(lambda x: isdir(join(base, x)), os.listdir(base))
    return 


setup(
    name='<package>',
    version=meta_api.__version__,
    url='http://github.com/spilgames/{{package}}',
    author='SpilGames',
    author_email='{{email}}',
    description=(
        "your description here"
        "and continue like this"
        "THE END"
    ),
    packages=find_packages(),
    include_package_data=True,
    package_data={'{{package}}': [x + '/views/*' for x in config.modules]
        # other examples:
        #'sources/config/*',
        #'lib/regexes.yaml',
    },
    scripts=[
        'start_gunicorn',
        'run.py',
    ],
    install_requires=[
        'flask',
        'gunicorn',
    ]
)
