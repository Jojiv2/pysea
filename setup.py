from setuptools import setup, find_packages

setup(
  name='pysea',
  version='1.0.0',
  description='PySea is a very easy to use python lib, based and working over opensea api no need to for api key or login information...',
  author='Jojiv2',
  author_email='https://github.com/Jojiv2',
  keywords=['opensea', 'pyton opensea', 'NFT'], 
  packages=find_packages(),
  install_requires=['urllib3'] 
)