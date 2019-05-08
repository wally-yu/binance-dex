## Binance DEX / Binance Chain Python Package
<img src="https://github.com/wally-yu/binance-dex/blob/master/binance-chain-python.jpg" width=375px height=108.75px>


## Introudction:
This Python package develop based on [Binance Chain official doc](https://docs.binance.org/) and tested all functionalities on test-net as well as main-net.

#### Dex Links:
 - Test-net: https://testnet.binance.org/
 - Main-net: https://www.binance.org

According to official doc, ways to connect to Binance DEX are:
 - REST API
 - CLI
 - Web Socket
 - Node RPC

This python package will provide all methods available as from binance official document except cli:
- [x] REST API
- [ ] CLI
- [x] WebSocket
- [x] Node NRPC

## Environment:
Due to time limitation, we didn't test different python version + os environment combinations, below are what we tested so far:
- [x] Python3.5 + MacOs
- [x] Python3.5 + Windows10

we are not sure if there would be any compatibility issues for python2.7, let us know if you encounter any issue.

BTW, we do suggest to use Virtual Environment.

## Python SDK Sample Usage:

#### Install package:

```
pip install binance-dex
```
 - Notes: If you are working on Windows platform, compiling tools `Microsoft Visual C++ 14.0` is required.

#### Full Code Example
Find full Sample Usage from [code_examples.py](https://github.com/wally-yu/binance-dex/blob/master/sample.py)

---

#### Code Examples Sector by Sector

#### - API Sample Usage
```
from binance_dex.api import BinanceChainClient

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


####  - Crypto Sample Usage

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

####  - Socket Sample Usage

```
from binance_dex.sockets import BinanceChainSocket

# --- Notice: Need to provide customized Call Back function to handle socket return data ---

# Sample of Customized Callback function to handle received data
def customized_call_back(ws, received_message):
    ''' Simply print out '''
    print('----- Customized handler -----')
    print(str(received_message))


# Create Socket Instance
socket_instance = BinanceChainSocket(IS_TEST_NET)

# 24hr Ticker statistics for a single symbol, push every second
socket_instance.fetch_ticker_streams(trading_pair='100K-9BC_BNB',
                                     is_full_data=True,
                                     one_off=False, # long lived connection
                                     callback_function=customized_call_back)
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
####  - Node RPC Sample Usage

```
from binance_dex.node_rpc import BinanceChainNodeRPC

# Create Instance

# OPTION 1: using existing RPC node
node_rpc_instance = BinanceChainNodeRPC(is_test_net=True,
                                        node_rpc_url=None)
                                        
# OPTION 2: using your own node
# node_rpc_instance = BinanceChainNodeRPC(node_rpc_url='https://seed-pre-s3.binance.org')

# Get number of unconfirmed transactions
print(node_rpc_instance.num_unconfirmed_txs())                                        
```
Sample return

```
Using Existing RPC server, trying to find a healthy node server...

Request URL: https://seed-pre-s3.binance.org:443/health ... ...

Successfully found healthy node RPC server: https://seed-pre-s3.binance.org:443

Request URL: https://seed-pre-s3.binance.org:443/num_unconfirmed_txs ... ...
{'status': True, 'result': {'jsonrpc': '2.0', 'id': '', 'result': {'n_txs': '0', 'txs': None}}}
```
[++Find more Node RPC Doc by clicking this link++](https://github.com/wally-yu/binance-dex/blob/master/README_NodeRPC.md)



## SDK Overview
As you might noticed from above code sample, this SDK is composed with 4 parts:
- API
- WebSockets
- Node RPC
- Crypto

#### Description
- **API:** HTTP API provides access to a Binance Chain node deployment and market data services [DETAILED API DOC](https://github.com/wally-yu/binance-dex/blob/master/README_API.md)

- **Web Sockets:** The DEX exposes several data streams over standard WebSocket connections, which can be consumed by modern web browsers and server-side WebSocket libraries [DETAILED SOCKET DOC](https://github.com/wally-yu/binance-dex/blob/master/README_WebSockets.md)

- **Node RPC:** May be used to interact with a node directly over HTTP or websockets. Using RPC, you may perform low-level operations like executing ABCI queries, viewing network/consensus state or broadcasting a transaction [DETAILED NODE DOC](https://github.com/wally-yu/binance-dex/blob/master/README_NodeRPC.md)

- **Crypto:** Crypto related functions (such as key managment) [DETAILED CRYPTO DOC](https://github.com/wally-yu/binance-dex/blob/master/README_Crypto.md)

#### Availability:

<html>
<table>
    <thead>
        <tr>
            <th></th>
            <th></th>
            <th>API</th>
            <th>WebSockets</th>
            <th>Node RPC</th>
            <th>Crypto</th>
        </tr>
    </thead>
        <tr>
            <td rowspan=3>Key</td>
            <td>generate mnemonic</td>
            <td></td>
            <td></td>
            <td></td>
            <td>&radic;</td>
        </tr>
        <tr>
            <td>generate key</td>
            <td></td>
            <td></td>
            <td></td>
            <td>&radic;</td>
        </tr>
        <tr>
            <td>generate keys</td>
            <td></td>
            <td></td>
            <td></td>
            <td>&radic;</td>
        </tr>
        <tr>
            <td rowspan=6>Chain</td>
            <td>get block height</td>
            <td>&radic;</td>
            <td>&radic;</td>
            <td></td>
            <td>&radic;</td>
        </tr>
        <tr>
            <td>get block info</td>
            <td></td>
            <td></td>
            <td>&radic;</td>
            <td></td>
        </tr>
        <tr>
            <td>get consensue info</td>
            <td></td>
            <td></td>
            <td>&radic;</td>
            <td></td>
        </tr>
        <tr>
            <td>get network info</td>
            <td></td>
            <td></td>
            <td>&radic;</td>
            <td></td>
        </tr>
        <tr>
            <td>get unconfirmed tx</td>
            <td></td>
            <td></td>
            <td>&radic;</td>
            <td></td>
        </tr>
        <tr>
            <td>get Tendermint status</td>
            <td></td>
            <td></td>
            <td>&radic;</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=6>Node</td>
            <td>get block time</td>
            <td>&radic;</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>get node info</td>
            <td>&radic;</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>get validators</td>
            <td>&radic;</td>
            <td></td>
            <td>&radic;</td>
            <td></td>
        </tr>
        <tr>
            <td>get peers</td>
            <td>&radic;</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>get end points</td>
            <td></td>
            <td></td>
            <td>&radic;</td>
            <td></td>
        </tr>
        <tr>
            <td>get abci info</td>
            <td></td>
            <td></td>
            <td>&radic;</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=5>Market</td>
            <td>get listing tokens</td>
            <td>&radic;</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>get trading pairs</td>
            <td>&radic;</td>
            <td>&radic;</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>get depth</td>
            <td>&radic;</td>
            <td>&radic;</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>get klines</td>
            <td>&radic;</td>
            <td>&radic;</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>get updated ticker statistics</td>
            <td>&radic;</td>
            <td>&radic;</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=3>Account</td>
            <td>get account balance</td>
            <td>&radic;</td>
            <td>&radic;</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>get account sequence</td>
            <td>&radic;</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>get account orders</td>
            <td></td>
            <td>&radic;</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>Transaction</td>
            <td>get transaction info</td>
            <td>&radic;</td>
            <td></td>
            <td>&radic;</td>
            <td></td>
        </tr>
        <tr>
            <td>broadcast transaction</td>
            <td>&radic;</td>
            <td></td>
            <td>&radic;</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>Others</td>
            <td>view chain fees</td>
            <td>&radic;</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
</table>
</html>


#### Network requirement:

|               |API        |WebSockets |JSONRPC    |Crypto     |
|:---:          |:---:      |:---:      |:---:      |:---:      |
|Requir Network |&radic;    |&radic;    |&radic;    |    X      |


## Join us:
You are always welcomed to join us! Leave your suggestions / or submit your codes

## License:
We promise will stick to MIT license permanently.
