import os

#from distutils.core import setup
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname )).read()

#with open('README.rst') as file:
# long_description = file.read()

setup(name='cartridge-cart',
      version='1.0',
      author='Willem Sijp',
      author_email='wim.sijp@gmail.com',
      description='Stripe integration for Mezzanine Cartridge',
      download_url="https://github.com/willo12/cartridge-cart/tarball/1.0",
      keywords=('web shop','e-commerce','stripe','mezzanine','cartridge','credit card charging'),
      packages = find_packages(exclude="tests"),
      classifiers = [],
# package_data = {
# "spacegrids": ['README.rst']
# },
      long_description=read('README.md'),
      url='https://github.com/willo12/spacegrids',
      license = "BSD",
      install_requires = []
      )
