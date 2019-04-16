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

- [x] Python3.5 + MacOs
- [x] Python3.5 + Windows10
- [ ] Python2.7 + 

## Sample Usage:

#### Install package:

```
pip install binance-dex
```
Notes: If you are working on Windows platform, compiling tools `Microsoft Visual C++ 14.0` is required.
#### Easy to Use
```
from binance_dex.api import Client

# create API Client instance
api_client = Client()

# call corresponding methods
print(api_client.get_block_time())

```
Expected to get results as:

```
{'status': True, 'result': {'ap_time': '2019-03-06T04:43:48Z', 'block_time': '2019-03-06T04:43:47Z'}}
```
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
|Need Network   |&radic;    |&radic;    |&radic;    |           |

#### Note:
**This package development just getting started, feel free to join if you have interest**

#### License:
This Binance Chain Python Package will stick to the MIT license permanently.

##
#### Book to read, put on readme: https://www.fullstackpython.com/websockets.html
