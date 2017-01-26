from setuptools import setup, find_packages

requires = ['requests-futures']

setup(name='totango',
      version='0.5.0',
      description='Totango Python Library',
      author='Dominik Gehl',
      author_email='dominik.gehl@returnpath.com',
      url='http://github.com/trackmaven/totango-python',
      license='Apache 2.0',
      packages=find_packages(),
      install_requires=requires,
      keywords="totango",
      zip_safe=False)
