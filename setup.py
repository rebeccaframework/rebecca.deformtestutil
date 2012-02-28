from setuptools import setup, find_packages

__version__ = '0.1'

setup(
    name="rebecca.deformtestutil",
    version=__version__,
    namespace_packages=['rebecca',],
    packages=find_packages(),
    install_requires=[
        'peppercorn',
        'deform',
        'webtest',
    ],
)
