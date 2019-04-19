## Binance DEX / Binance Chain Python Package
<img src="https://github.com/wally-yu/binance-dex/blob/master/binance-chain-python.jpg" width=375px height=108.75px>


## Introudction:

Ways to connect to Binance DEX are:
 - REST API
 - CLI
 - WebSocket
 - JSONRPC

This python package will provide all methods available as from binance official document except cli:
- [x] REST API
- [ ] CLI
- [x] WebSocket
- [x] JSONRPC
## Environment:
Due to time limitation, below environment are tested.
- [x] Python3.5 + MacOs
- [x] Python3.5 + Windows10
- we are not sure if there would be any compatibility issues for python2.7, let us know if you encounter any issue

## Sample Usage:

#### Install package:

```
pip install binance-dex
```
 - Notes: If you are working on Windows platform, compiling tools `Microsoft Visual C++ 14.0` is required.

---

#### API Sample 
```
from binance_dex.api import Client

# create API Client instance
api_client = BinanceChainClient(is_test_net=True)

# call corresponding methods
print(api_client.get_block_time())

```
Sample return:

```
{'status': True, 'result': {'ap_time': '2019-04-06T04:43:48Z', 'block_time': '2019-04-06T04:43:47Z'}}
```
[++Find more API information by clicking this link++](https://github.com/wally-yu/binance-dex/blob/master/README_API.md)


---


#### Crypto Sample 

```
from binance_dex.crypto import BinanceChainCrypto

# Create crypto instance
crypto_instance = BinanceChainCrypto(is_test_net=True)

# Generate Mnemonic words
mnemonic_words = crypto_instance.generate_mnemonic()
print("Generating Mnemonic Words: ")
print(mnemonic_words)

# Generate Private Key, Public Address and mnemonic
key = crypto_instance.generate_key()
print('Generating Private Key / Public Key / Mnemonic words: ')
print(key)
```
Sample return:

```
Generating Mnemonic Words: 
early solid bronze civil version orange prize curve glory cricket ticket already weekend home early buyer zebra olive melody enrich park jeans apart tower

Generating Private Key / Public Key / Mnemonic words: 
{'private_key': '65dba225a6965020ff7aae6efc8b9494cbf52bea36e44341d471a7b4b8207e1a', 'public_address': 'tbnb1uvjsrw2pstxqwk45n8k6ke53yw8fsegjery2en', 'mnemonic': 'allow adult frown ivory coffee inhale calm assist galaxy indoor credit oyster tower exclude popular veteran first hint flag boost right zone clown flower'}

```
[++Find more Crypto information by clicking this link++](https://github.com/wally-yu/binance-dex/blob/master/README_Crypto.md)


---

#### Socket Sample 

```
from binance_dex.sockets import BinanceChainSocket


# Sample of Customized Callback function to handle received data
def customized_msg_handler(ws, received_message):
    ''' Simply print out '''
    print('----- Customized handler -----')
    print(str(received_message))


# Create Socket Instance
socket_instance = BinanceChainSocket(IS_TEST_NET)

# 24hr Ticker statistics for a single symbol, push every second
socket_instance.fetch_ticker_streams(trading_pair='100K-9BC_BNB',
                                     is_full_data=True,
                                     one_off=False, # long lived connection
                                     callback_function=customized_msg_handler)
```
Sample return:

```
----- Customized handler -----
{"stream":"ticker","data":{"e":"24hrTicker","E":1555687041,"s":"100K-9BC_BNB","p":"0.00000000","P":"0.00000000","w":"49999.00000000","x":"49999.00000000","c":"49999.00000000","Q":"0.00009820","b":"0.00000000","B":"0.00000000","a":"4700.00000000","A":"0.13197840","o":"49999.00000000","h":"49999.00000000","l":"49999.00000000","v":"0.00000000","q":"0.00000000","O":1555600601881,"C":1555687001881,"F":"8274485-0","L":"8274485-0","n":0}}

----- Customized handler -----
{"stream":"ticker","data":{"e":"24hrTicker","E":1555687042,"s":"100K-9BC_BNB","p":"0.00000000","P":"0.00000000","w":"49999.00000000","x":"49999.00000000","c":"49999.00000000","Q":"0.00009820","b":"0.00000000","B":"0.00000000","a":"4700.00000000","A":"0.13197840","o":"49999.00000000","h":"49999.00000000","l":"49999.00000000","v":"0.00000000","q":"0.00000000","O":1555600601881,"C":1555687001881,"F":"8274485-0","L":"8274485-0","n":0}}

----- Customized handler -----
{"stream":"ticker","data":{"e":"24hrTicker","E":1555687043,"s":"100K-9BC_BNB","p":"0.00000000","P":"0.00000000","w":"49999.00000000","x":"49999.00000000","c":"49999.00000000","Q":"0.00009820","b":"0.00000000","B":"0.00000000","a":"4700.00000000","A":"0.13197840","o":"49999.00000000","h":"49999.00000000","l":"49999.00000000","v":"0.00000000","q":"0.00000000","O":1555600601881,"C":1555687001881,"F":"8274485-0","L":"8274485-0","n":0}}
```
[++Find more Web Socket Doc by clicking this link++](https://github.com/wally-yu/binance-dex/blob/master/README_WebSockets.md)


---
#### Node RPC Sample 

```
from binance_dex.node_rpc import BinanceChainNodeRPC

# Create Instance

# # OPTION 1: using existing RPC node
node_rpc_instance = BinanceChainNodeRPC(is_test_net=True,
                                        node_rpc_url=None)
                                        
# #OPTION 2: using your own node
# node_rpc_instance = BinanceChainNodeRPC(node_rpc_url='https://seed-pre-s3.binance.org')

# Get number of unconfirmed transactions
print(node_rpc_instance.num_unconfirmed_txs())                                        
```
Sample return

```
Using Binance RPC server, trying to find a healthy node server...

Request URL: https://seed-pre-s3.binance.org:443/health ... ...

Successfully found healthy node RPC server: https://seed-pre-s3.binance.org:443

Request URL: https://seed-pre-s3.binance.org:443/num_unconfirmed_txs ... ...
{'status': True, 'result': {'jsonrpc': '2.0', 'id': '', 'result': {'n_txs': '0', 'txs': None}}}
```
[++Find more Node RPC Doc by clicking this link++](https://github.com/wally-yu/binance-dex/blob/master/README_NodeRPC.md)

---

#### Service availability:
|Service Name   |API        |WebSockets |JSONRPC    |Crypto     |
|---            |:---:      |:---:      |:---:      |:---:      |
|time           |&radic;    |&radic;    |           |           |
|node-info      |&radic;    |           |           |           |
|validators     |&radic;    |           |           |           | 
|peers          |&radic;    |           |           |           | 
|account        |&radic;    |&radic;    |           |           |
|tx             |&radic;    |           |           |           |
|tokens         |&radic;    |           |           |           |
|markets        |&radic;    |           |           |           |
|fees           |&radic;    |           |           |           |
|depth          |&radic;    |&radic;    |           |           |
|broadcast      |&radic;    |           |           |           |
|klines         |&radic;    |           |           |           |
|orders         |&radic;    |&radic;    |           |           |
|ticker         |&radic;    |&radic;    |           |           |
|trades         |&radic;    |&radic;    |           |           |
|transactions   |&radic;    |&radic;    |           |           |

#### Network requirement:

|               |API        |WebSockets |JSONRPC    |Crypto     |
|:---:          |:---:      |:---:      |:---:      |:---:      |
|Need Network   |&radic;    |&radic;    |&radic;    |    X       |

#### Note:
**This package development just getting started, feel free to join if you have interest**

#### License:
This Binance Chain Python Package will stick to the MIT license permanently.

##
#### Book to read, put on readme: https://www.fullstackpython.com/websockets.html
