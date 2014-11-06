from setuptools import setup
import os

import HPOlibConfigSpace

here = os.path.abspath(os.path.dirname(__file__))
desc = 'Package to describe configuration spaces for automated algorithm ' \
       'configuration and hyperparameter tuning'
keywords = 'algorithm configuration hyperparameter optimization empirical ' \
           'evaluation black box'


data_files = []
scripts = ['scripts/HPOlib-convert']

package_dir = {'HPOlibConfigSpace': 'HPOlibConfigSpace',
               'HPOlibConfigSpace.nx': 'HPOlibConfigSpace/nx',
               'HPOlibConfigSpace.nx.algorithms':
                   'HPOlibConfigSpace/nx/algorithms',
               'HPOlibConfigSpace.nx.classes': 'HPOlibConfigSpace/nx/classes',
               'HPOlibConfigSpace.nx.external': 'HPOlibConfigSpace/nx/external',
               'HPOlibConfigSpace.nx.utils': 'HPOlibConfigSpace/nx/utils',
               'HPOlibConfigSpace.converters': 'HPOlibConfigSpace/converters'}


def get_find_packages():
    packages = ['HPOlibConfigSpace',
                'HPOlibConfigSpace.nx',
                'HPOlibConfigSpace.nx.algorithms',
                'HPOlibConfigSpace.nx.classes',
                'HPOlibConfigSpace.nx.external',
                'HPOlibConfigSpace.nx.utils',
                'HPOlibConfigSpace.converters']
    return packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='HPOlibConfigSpace',
    version=HPOlibConfigSpace.__version__,
    url='https://github.com/automl/HPOlibConfigSpace',
    license='GPLv3',
    platforms=['Linux'],
    author=HPOlibConfigSpace.__authors__,
    test_suite="nose.collector",
    install_requires=['argparse',
                      'numpy',
                      'pyparsing'
                      ],
    author_email='feurerm@informatik.uni-freiburg.de',
    description=desc,
    long_description=read("README.md"),
    keywords=keywords,
    packages=get_find_packages(),
    package_dir=package_dir,
    data_files=data_files,
    scripts=scripts,
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: General Public License v3 (LGPLv3)',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
    ]
)
