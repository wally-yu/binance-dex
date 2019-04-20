## WebSockets Lib 

The Binance DEX Python WebSockets Package provides connection to data streams exposed by The DEX official site 
over standard WebSocket connections, which can be consumed by modern web browsers and server-side WebSocket libraries.

- The base endpoint is: `wss://testnet-dex.binance.org/api/.`
- Each connection can consume a single stream or multiple streams may be multiplexed through one connection for more complex apps.
- All symbols in stream names are lowercase.

For more information: https://binance-chain.github.io/api-reference/dex-api/ws-connection.html
### Usage
`Step1:` Create API Client instance

```python
from binance_dex.sockets import BinanceChainSocket

socket_instance = BinanceChainSocket(IS_TEST_NET)
```
***NOTES:***  
`class BinanceChainSocket` has one positional argument during initializing:
- If `is_test_net = True` , server API calling node will be set to `'wss://testnet-dex.binance.org/api/ws/'`, otherwise 
`'wss://dex.binance.org/api/ws/'`.


`Step2:` call the specific function

```python
socket_instance.fetch_XXX(*args)
```
***NOTES:***     
Each of the instance methods takes several positional arguments, `one_off` and `callback_function` **are the 
common ones**:    
 - `one_off`: defines choosing short-lived or long-lived connection to websocket
 - `callback_function`: callback function of handling returned message of websocket. __New achievement for developers to 
handel message__

**For example:**

- Sample of Short-lived (one-off / send-receive) Connection
```python
socket_instance.fetch_block_height_updates()
```

- Sample of Long Lived Connection WITHOUT customized Callback, 
If callback function not provided, will simply print out
```python
socket_instance.fetch_block_height_updates(one_off=False)
```

- If callback function provided, can customized handle received data
```python
def customized_msg_handler(ws, received_message):
    ''' Simply print out '''
    print('----- Customized handler -----')
    print(str(received_message))
    
socket_instance.fetch_block_height_updates(one_off=False, callback_function=customized_msg_handler)
```


#### Service availability:
|Service Name                               | WebSockets                |
|---                                        |:---:                      |
|Orders                                     |&radic;                    |
|Account                                    |&radic;                    |
|Transfer                                   |&radic;                    |
|Trades                                     |&radic;                    |
|Diff.Depth Stream                          |&radic;                    |
|Book Depth Streams                         |&radic;                    |
|Kline/Candlestick Streams                  |&radic;                    |
|Individual Symbol Ticker Streams           |&radic;                    |
|All Symbols Ticker Streams                 |&radic;                    |
|Individual Symbol Mini Ticker Streams      |&radic;                    |
|All Symbols Mini Ticker Streams            |&radic;                    |
|Blockheight                                |&radic;                    |
      
&ensp;     &radic;: Able to Use  &ensp;&ensp;     &bigcirc;: Unfinished   &ensp;&ensp;    &ominus;:Unstable &ensp;&ensp;  &times;: Official Unsupported 



### Referance
The following document subhead will appear like that: `WebSockets service func`  ->  `raw WebSockets stream`, 
which declare the mapping relationships between Python WebSockets Package service function and raw WebSockets stream.
Samples will simply use **long-lived connection** and **customized_msg_handler** for description convenience.

#### `fetch_account_updates(user_address, one_off, callback_function)`  -> `Orders/Account/Transfer`
- Summary: Return account updates
- Description: This function may receive serveral kinds of data, distinguished by "stream" from returned data
- Topic Name: accounts/account/orders
- Stream: /ws/userAddress
- Parm `user_address`: user address hash, **must be specified**
- Parm `one_off`
- Parm `callback_function` 

Success sample result:

```python
> socket_instance.fetch_account_updates(user_address='tbnb1r4gc5ftrkr9ez2khph4h5xxd0mf0hd75jf06gw',
                                        one_off=False,
                                        callback_function=customized_msg_handler)
```
- Account sample return (notice `"stream" == "accounts"`):
```python
{
    "stream": "accounts",
    "data": {
        "e": "outboundAccountInfo",         # Event type
        "E": 7364509,                       # Event height
        "B": [{                             # Balances array
            "a": "BNB",                     # Asset
            "f": "1371.08750000",           # Free amount
            "r": "0.00000000",              # Locked amount
            "l": "0.00000000"               # Frozen amount
        }, {
            "a": "DEX.B-C72",
            "f": "999999791.11200000",
            "r": "0.00000000",
            "l": "0.00000000"
        }]
    }
}
```

- Transfer sample return (notice `"stream" == "transfers"`):
```python
{
    "stream": "transfers",
    "data": {
        "e": "outboundTransferInfo",                                                # Event type
        "E": 7364509,                                                               # Event height
        "H": "08B71F862CDB820AF499D6E4FB34494CA163EBDADD5DC5D0A61EB1A0725BB4F4",    # Transaction hash
        "f": "tbnb1r4gc5ftrkr9ez2khph4h5xxd0mf0hd75jf06gw",                         # From addr
        "t": [{
            "o": "tbnb1fn9z9vn4f44ekz0a3pf80dcy2wh4d5988phjds",                     # To addr
            "c": [{                                                                 # Coins
                "a": "DEX.B-C72",                                                   # Asset
                "A": "8.88800000"                                                   # Amount
            }]
        }]
    }
}
```

- Orders sample return (notice `"stream" == "orders"`):
```python
{
    "stream": "orders",                                       
    "data": [{                                                
        "e": "executionReport",                               # Event type
        "E": 7366949,                                         # Event height 
        "s": "100K-9BC_BNB",                                  # Symbol
        "S": 1,                                               # Side, 1 for Buy, 2 for sell 
        "o": 2,                                               # Order type, 2 for LIMIT (only) 
        "f": 1,                                               # Time in force,  1 for Good Till Expire (GTE); 3 for Immediate Or Cancel (IOC)
        "q": "0.00001500",                                    # Order quantity
        "p": "66666.00000000",                                # Order price
        "x": "NEW",                                           # Current execution type
        "X": "Ack",                                           # Current order status, possible values Ack, Canceled, Expired, IocNoFill, PartialFill, FullyFill, FailedBlocking, FailedMatching, Unknown
        "i": "1D518A2563B0CB912AD70DEB7A18CD7ED2FBB7D4-10",   # Order ID
        "l": "0.00000000",                                    # Last executed quantity
        "L": "0.00000000",                                    # Cumulative filled quantity
        "z": "0.00001500",                                    # Last executed price
        "n": "",                                              # Commission amount for all user trades within a given block. Fees will be displayed with each order but will be charged once.
                                                              # Fee can be composed of a single symbol, ex: "10000BNB"
                                                              # or multiple symbols if the available "BNB" balance is not enough to cover the whole fees, ex: "1.00000000BNB;0.00001000BTC;0.00050000ETH"
        "T": 1554890366040313451,                             # Transaction time
        "t": "",                                              # Trade ID
        "O": 1554890366040313451                              # Order creation time
    }]  
}
```


#### `fetch_trades_updates(trading_pair, one_off, callback_function)`  -> `Trades`
- Summary: Returns individual trade updates.
- Description: NA
- Topic Name: trades
- Stream: \<symbol>@trades
- Parm `trading_pair`: trade pair, **must be specified**
- Parm `one_off`
- Parm `callback_function` 

Success sample result:

```python
> socket_instance.fetch_trades_updates(trading_pairs='100K-9BC_BNB',
                                       one_off=False,
                                       callback_function=customized_msg_handler)
                                       
{
    "stream": "trades",
    "data": [{
        "e": "trade",                                           # Event type
        "E": 7549438,                                           # Event height
        "s": "100K-9BC_BNB",                                    # Symbol
        "t": "7549438-0",                                       # Trade ID
        "p": "3333.00000000",                                   # Price
        "q": "0.02611100",                                      # Quantity
        "b": "1D518A2563B0CB912AD70DEB7A18CD7ED2FBB7D4-11",     # Buyer order ID
        "a": "EA1AE716501D1DB0B9F295A30891D9E562828678-12",     # Seller order ID
        "T": 1554964166437515341,                               # Trade time
        "sa": "tbnb1agdww9jsr5wmpw0jjk3s3yweu43g9pnc4p5kg7",    # SellerAddress
        "ba": "tbnb1r4gc5ftrkr9ez2khph4h5xxd0mf0hd75jf06gw"     # BuyerAddress
    }]
}
```


#### `fetch_market_diff_stream(trading_pair, one_off, callback_function)`  -> `Diff. Depth Stream`
- Summary: Order book price and quantity depth updates used to locally keep an order book.
- Description: NA
- Topic Name: marketDiff
- Stream: \<symbol>@marketDiff
- Parm `trading_pair`: trade pair, **must be specified**
- Parm `one_off`
- Parm `callback_function`  

Success sample result:

```python
> socket_instance.fetch_market_diff_stream(trading_pairs='100K-9BC_BNB',
                                           one_off=False,
                                           callback_function=customized_msg_handler)

{
    "stream": "marketDiff",
    "data": {
        "e": "depthUpdate",                  # Event type
        "E": 1554964484,                     # Event tim
        "s": "100K-9BC_BNB",                 # Symbol
        "b": [                               # Bids to be updated
            ["3333.00000000",                # Price level to be updated
             "0.07398900"                    # Quantity
            ]  
        ],
        "a": [                               # Asks to be updated
                                             # Price level to be updated and Quantity
        ]                              
    }
}
```


#### `fetch_market_depth_stream(trading_pair, one_off, callback_function)`  -> `Book Depth Streams`
- Summary: Top 20 levels of bids and asks.
- Description: NA
- Topic Name: marketDepth
- Stream: \<symbol>@marketDepth
- Parm `trading_pair`: trade pair, **must be specified**
- Parm `one_off`
- Parm `callback_function`  

Success sample result:

```python
> socket_instance.fetch_market_depth_stream(trading_pairs='100K-9BC_BNB',
                                            one_off=False,
                                            callback_function=customized_msg_handler)
                                            
{
    "stream": "marketDepth",
    "data": {                           
        "lastUpdateId": 7551469,       # Last update ID
        "symbol": "100K-9BC_BNB",      # symbol
        "bids": [                      # Bids to be updated
            ["3333.00000000",          # Price level to be updated
            "0.07398900"]              # Quantity        
        ],
        "asks": [                      # Asks to be updated
            ["66666.00000000",         # Price level to be updated
            "1.68270010"],             # Quantity 
            ["70000.00000000", 
            "1.00000000"],
            ["90000000000.00000000", 
            "40.05079290"]
        ]
    }
}
```


#### `fetch_kline_updates(trading_pair, interval, one_off, callback_function)`  -> `Kline/Candlestick Streams`
- Summary: The kline/candlestick stream pushes updates to the current klines/candlestick every second.
- Description: NA
- Topic Name: kline_\<interval>
- Stream: \<symbol>@kline_\<interval>
- Parm `trading_pair`: trade pair, **must be specified**
- Parm `interval`: interval of the kline chart
- Parm `one_off`
- Parm `callback_function`  

Allowed Kline/Candlestick chart intervals are described in `class KLine(object)` in `/binance-dex/api.py`:    
- interval_1min -> '1m'
- interval_3min -> '3m'
- interval_5min -> '4m'
- interval_15min -> '15m'
- interval_1hour -> '1h'
- interval_2hour -> '2h'
- interval_4hour -> '4h'
- interval_6hour -> '6h'
- interval_8hour -> '8h'
- interval_12hour -> '12h'
- interval_1day -> '1d'
- interval_3day -> '3d'
- interval_1week -> '1w'
- interval_1month -> '1M'    

Success sample result:

```python
> from binance_dex.api import api_types_instance
  kline_intervals = api_types_instance.KLine()
  socket_instance.fetch_kline_updates(trading_pair='BNB_BTC',
                                      interval=kline_intervals.interval_1hour,
                                      callback_function=customized_msg_handler)

{
  "stream": "kline_1m",
  "data": {
    "e": "kline",         # Event type
    "E": 123456789,       # Event time
    "s": "BNBBTC",        # Symbol
    "k": {
      "t": 123400000,     # Kline start time
      "T": 123460000,     # Kline close time
      "s": "BNBBTC",      # Symbol
      "i": "1m",          # Interval
      "f": "100",         # First trade ID
      "L": "200",         # Last trade ID
      "o": "0.0010",      # Open price
      "c": "0.0020",      # Close price
      "h": "0.0025",      # High price
      "l": "0.0015",      # Low price
      "v": "1000",        # Base asset volume
      "n": 100,           # Number of trades
      "x": false,         # Is this kline closed?
      "q": "1.0000",      # Quote asset volume
    }
  }
}
```                                            


#### `fetch_ticker_streams(trading_pair, is_full_data, one_off, callback_function)`  ->     `Individual Symbol Ticker Streams/ All Symbols Ticker Streams/ Individual Symbol Mini Ticker Streams/ All Symbols Mini Ticker Streams`
- Summary: 24hr Ticker statistics for a single symbol are pushed every second.
- Description: NA
- Topic Name: ticker/allTickers/miniTicker/allMiniTickers
- Stream: \<symbol>@ticker / $all@allTickers / \<symbol>@miniTicker / $all@allMiniTickers
- Param `trading_pair`: Specific trading pair, default is `None`, if not provide will return all trade pair data
- Param `is_full_data`: default is `True`, returns `ticker` format data, if `False`, returns `miniticker` format data    
- Parm `one_off`
- Parm `callback_function`    

Success sample result:

- Ticker sample return (notice `"stream" == "ticker"`):
```python
socket_instance.fetch_ticker_streams(trading_pair='BNB_BTC.B-918',
                                     is_full_data=True,
                                     one_off=False,
                                     callback_function=customized_msg_handler)
                                                                        
{
    "stream": "ticker",             
    "data": {
        "e": "24hrTicker",          # Event type
        "E": 1555425469,            # Event time
        "s": "BNB_BTC.B-918",       # Symbol
        "p": "0.00000000",          # Price change
        "P": "0.00000000",          # Price change percent
        "w": "0.00373109",          # Weighted average price
        "x": "0.00373109",          # Previous day's close price
        "c": "0.00373109",          # Current day's close price
        "Q": "1.00000000",          # Close trade's quantity
        "b": "0.00379908",          # Best bid price
        "B": "58.00000000",         # Best bid quantity
        "a": "0.00381643",          # Best ask price
        "A": "91.00000000",         # Best ask quantity
        "o": "0.00373109",          # Open price
        "h": "0.00373109",          # High price
        "l": "0.00373109",          # Low price
        "v": "0.00000000",          # Total traded base asset volume
        "q": "0.00000000",          # Total traded quote asset volume
        "O": 1555339051274,         # Statistics open time
        "C": 1555425451274,         # Statistics close time
        "F": "8349745-0",           # First trade ID
        "L": "8349745-0",           # Last trade Id
        "n": 0                      # Total number of trades
    }
}
```

- AllTickers sample return (notice `"stream" == "allTickers"`):
```python
socket_instance.fetch_ticker_streams(is_full_data=True,
                                     one_off=False,
                                     callback_function=customized_msg_handler)
                                                                        
{
    "stream": "allTickers",             
    "data": [{
        "e": "24hrTicker",          # Event type
        "E": 1555426679,            # Event time
        "s": "83SHUIHU-AC4_BNB",    # Symbol
        "p": "0.00000000",          # Price change
        "P": "0.00000000",          # Price change percent
        "w": "0.07995000",          # Weighted average price
        "x": "0.07995000",          # Previous day's close price
        "c": "0.07995000",          # Current day's close price
        "Q": "30000.00000000",      # Close trade's quantity
        "b": "0.00000000",          # Best bid price
        "B": "0.00000000",          # Best bid quantity
        "a": "0.00000000",          # Best ask price
        "A": "0.00000000",          # Best ask quantity
        "o": "0.07995000",          # Open price
        "h": "0.07995000",          # High price
        "l": "0.07995000",          # Low price
        "v": "0.00000000",          # Total traded base asset volume
        "q": "0.00000000",          # Total traded quote asset volume
        "O": 1555340275037,         # Statistics open time
        "C": 1555426675037,         # Statistics close time
        "F": "3036396-1",           # First trade ID
        "L": "3036396-1",           # Last trade Id
        "n": 0                      # Total number of trades
    },{
    '...OMIT...'
    }]
}
```

- MiniTicker sample return (notice `"stream" == "miniTicker"`):
```python
socket_instance.fetch_ticker_streams(trading_pair='BNB_BTC.B-918',
                                     is_full_data=False,
                                     one_off=False,
                                     callback_function=customized_msg_handler)
                                                                        
{
    "stream": "miniTicker",             
    "data": {
        "e": "24hrTicker",          # Event type
        "E": 1555425469,            # Event time
        "s": "BNB_BTC.B-918",       # Symbol
        "c": "0.00373109",          # Current day's close price
        "o": "0.00373109",          # Open price
        "h": "0.00373109",          # High price
        "l": "0.00373109",          # Low price
        "v": "0.00000000",          # Total traded base asset volume
        "q": "0.00000000",          # Total traded quote asset volume
    }
}

```

- AllMiniTicker sample return (notice `"stream" == "allMiniTickers"`):
```python
socket_instance.fetch_ticker_streams(is_full_data=False,
                                     one_off=False,
                                     callback_function=customized_msg_handler)
                                                                        
{
    "stream": "allMiniTickers",             
    "data": [{
        "e": "24hrTicker",          # Event type
        "E": 1555428570,            # Event time
        "s": "MBNB-113_BNB",        # Symbol
        "c": "0.00010000",          # Current day's close price
        "o": "0.00010000",          # Open price
        "h": "0.00010000",          # High price
        "l": "0.00010000",          # Low price
        "v": "3.00000000",          # Total traded base asset volume
        "q": "0.00030000",          # Total traded quote asset volume
    },{
    '...OMIT...'
    }]
}

```


#### `fetch_block_height_updates()`  -> `Blockheight`
- Summary: Streams the latest block height.
- Description: NA
- Topic Name: blockheight
- Stream: $all@blockheight
- Parm `one_off`
- Parm `callback_function`  

Success sample result:

```python
> socket_instance.fetch_block_height_updates(one_off=False, 
                                             callback_function=customized_msg_handler)

{   
    "stream": "blockheight",
    "data": {
        "h":8699895        # Block height
    }
}

```


### Additional Info
#### Why Socket?

A WebSocket connection allows full-duplex communication between a client and server so that either side can push data 
to the other through an established connection. The reason why WebSockets, along with the related technologies of 
Server-sent Events (SSE) and WebRTC data channels, are important is that HTTP is not meant for keeping open a connection
 for the server to frequently push data to a web browser. Previously, most web applications would implement long polling
  via frequent Asynchronous JavaScript and XML (AJAX) requests as shown in the below diagram.

For more information: https://www.fullstackpython.com/websockets.html

