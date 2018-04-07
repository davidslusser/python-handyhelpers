from setuptools import setup
import handyhelpers

setup(
    name='python-handyhelpers',
    packages=['handyhelpers'],
    version=handyhelpers.__version__,
    license=handyhelpers.__license__,
    author='David Slusser',
    author_email='dbslusser@gmail.com',
    description='A collection of handy utilities to support python operations',
    long_description='A collection of handy utilities to support python operations',
    url='https://github.com/davidslusser/python-handyhelpers',
    download_url='https://github.com/davidslusser/python-handyhelpers/archive/0.1.tar.gz',
    keywords=['python', 'helpers', ],
    classifiers=[],
    install_requires=[

    ],
    dependency_links=[],
)
