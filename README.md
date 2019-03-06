## Binance DEX Python Package

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

## Sample Usage:

#### Install package:

```
pip install binance-dex
```

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
#### Note:
**This package development just getting started, feel free to join if you have interest**