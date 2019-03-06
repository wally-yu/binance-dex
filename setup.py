from setuptools import setup, find_packages
version = '0.0.34'

with open('README.md') as readme_file:
    long_description = readme_file.read()

setup(
    name='binance_dex',
    version=version,
    packages=find_packages(),
    author=u'Wally Yu',
    install_requires=['requests==2.18.4'],
    url='https://github.com/wally-yu/binance-dex',
    include_package_data=True,
    license='MIT License',
    description='Python Library for Binance DEX, including API, Websocket, JSONRPC',
    long_description=long_description,
    long_description_content_type='text/markdown',
      )

# build: python3 setup.py sdist bdist_wheel