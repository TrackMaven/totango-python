from setuptools import setup, find_packages

requires = ['grequests']

from totango import __version__

setup(name='totango',
      version=__version__,
      description='Totango Python Library',
      author='Dominik Gehl',
      author_email='dominik.gehl@returnpath.com',
      url='http://github.com/trackmaven/totango-python',
      license='Apache 2.0',
      packages=find_packages(),
      install_requires=requires,
      setup_requires=requires,
      keywords="totango",
      zip_safe=False)
