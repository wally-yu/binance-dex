from setuptools import setup, find_packages
version = '0.1.3'

with open('README.md') as readme_file:
    long_description = readme_file.read()

setup(
    name='binance_dex',
    version=version,
    packages=find_packages(),
    author=u'Wally Yu',
    install_requires=['requests==2.11.1', 'websocket-client-py3==0.15.0', 'mnemonic==0.18', 'rlp==1.1.0',
                      'eth_utils==1.4.1', 'two1==3.10.9', 'pycrypto==2.6.1', 'pycryptodome==3.8.0', 'base58==0.2.2',
                      'protobuf==3.6.1'],
    url='https://github.com/wally-yu/binance-dex',
    include_package_data=True,
    license='MIT License',
    description='Python Library for Binance DEX, including API, Websocket, JSONRPC and Crypto',
    long_description=long_description,
    long_description_content_type='text/markdown',
      )

# build: python3 setup.py sdist bdist_wheel