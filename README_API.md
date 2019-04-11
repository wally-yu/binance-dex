## API Lib 

The Binance DEX Python API Package provides access to official HTTP API for getting Binance Chain node deployment and 
market data services.    

Official API Site `https://testnet-dex.binance.org/api/v1/`
### Usage
`Step1:` Create API Client instance

```python
from binance_dex.api import BinanceChainClient

api_client = BinanceChainClient(is_test_net, api_base_url_with_port)
```
***NOTES***:  
`class BinanceChainClient` has two positional arguments during initializing:
   - `api_base_url_with_port` parameter has higher priority, if specified,  API base URL will be `api_base_url_with_port`
   -  If `api_base_url_with_port` is `None` and `is_test_net = True` , API base URL will link to `'https://testnet-dex.binance.org/'`, otherwise `'https://dex.binance.org/'`


`Step2:` call the specific API

```python
api_client.get_XXX()
```

***NOTES***:   
All the APIs have the `same` return message format, which means if `no error` happens, message return will be：
 ```python
 {'status': True, 'result': ret_data}
 ```

If `any error` occurred, message return will be：
 ```python
 {'status': False, 'message': error_type}
  ```

### Referance
The following document subhead will appear like that: 
 `API service func`  ->  `raw HTTP API type`, which declare the mapping relationships between Python API Package service
 function and raw HTTP API type. ~~Also, the success return of API will be simplified as `ret_data` for description 
 convenience.~~

#### `get_block_time()`  -> `/api/v1/time`
- Summary: Get the block time.
- Description: Gets the latest block time and the current time according to the HTTP service.
- Destination: Validator node.
- Rate Limit: 1 request per IP per second.

Success sample result:

```python
> api_client.get_block_time()

{'status': True,
 'result': {'block_time': '2019-04-11T07:26:46Z',
            'ap_time': '2019-04-11T07:26:47Z'
            },
 }
```

#### `get_node_info()`  -> `/api/v1/node-info`
- Summary: Get node information.
- Description: Gets runtime information about the node.
- Destination: Validator node.
- Rate Limit: 1 request per IP per second.

Success sample result:

```python
> api_client.get_node_info()

{'status': True,
 'result': {'node_info': {'id': 'dd2adba52ad9c830fe16a53fe81dac6880a91218',
                          'listen_addr': '10.203.42.14:27146', 
                          'network': 'Binance-Chain-Nile', 
                          'version': '0.30.1',
                          'channels': '3540202122233038', 
                          'moniker': 'Aconcagua',
                          'other': {'amino_version': '',
                                  'p2p_version': '', 
                                  'consensus_version': '', 
                                  'rpc_version': '',
                                  'tx_index': 'on', 
                                  'rpc_address': 'tcp://0.0.0.0:27147'
                                  }
                          }, 
             'sync_info': {'latest_block_hash': '7CBCCF0980B6A9D7B988199FEAF7E01FB02668ED192397198013194D8F311EC2',
                           'latest_app_hash': '193A0D5399A6FF77F0DB5543C6FAC367451DF42C506C9B63DF200F3DEC78D89D',
                           'latest_block_height': 8275, 
                           'latest_block_time': '2019-03-07T02:49:52.843793234Z', 
                           'catching_up': False
                           },
             'validator_info': {'address': '344C39BB8F4512D6CAB1F6AAFAC1811EF9D8AFDF', 
                                'pub_key': [77, 66, 10, 234, 132, 62, 146, 160, 207, 230, 157, 137, 105, 109,
                                            255, 104, 39, 118, 159, 156, 181, 42, 36, 154, 245, 55, 206, 137, 
                                            191, 42, 75, 116], 
                                'voting_power': 100000000000
                                }
             }
 }
```

#### `get_validators()`  -> `/api/v1/validators`
- Summary: Get validators.
- Description: Gets the list of validators used in consensus.
- Destination: Witness node.
- Rate Limit: 10 requests per IP per second.

Sample success result:
```python
> api_client.get_validators()

{'status': True,
 'result': {'block_height': 6935724,
            'validators': [{'address': '06FD60078EB4C2356137DD50036597DB267CF616',
                            'pub_key': [22, 36, 222, 100, 32, 225, 124, 190, 156, 32, 205, 207, 
                                        223, 135, 107, 59, 18,151, 141, 50, 100, 160, 7, 252, 170, 
                                        167, 28, 76, 219, 112, 29, 158, 188, 3, 35, 244, 79],
                            'voting_power': 100000000000
                            }, 
                           {'address': '18E69CC672973992BB5F76D049A5B2C5DDF77436',
                            'pub_key': [22, 36, 222, 100, 32, 24, 78, 123, 16, 61, 52, 196, 
                                        16, 3, 249, 184, 100, 213, 248, 193, 173, 218, 155, 
                                        208, 67, 107, 37, 59, 179, 200, 68, 188, 115, 156, 30, 119, 201],
                            'voting_power': 100000000000
                            }, 
                            ...
                            ]
            }
 }
```

#### `get_tokens()`  -> `/api/v1/tokens`
- Summary: Get tokens list.
- Description: Gets a list of tokens that have been issued.
- Destination: Witness node.
- Rate Limit: 1 request per IP per second.

Sample success result:

```python
> api_client.get_tokens()

{'status': True, 
 'result': [{'name': 'ANN Network', 
             'symbol': 'ANN-457', 
             'original_symbol': 'ANN',
             'total_supply': '100000000.00000000',
             'owner': 'tbnb14zguq8gf58ms07npae7pluqxm27xvvgftmhsxz', 
             'mintable': True
             },
            {'name': 'Zilliqa', 
             'symbol': 'ZIL-C5D', 
             'original_symbol': 'ZIL', 
             'total_supply': '1000000000.00000000',
             'owner': 'tbnb1hzm72ffar7f57jtx9k70jukqydchvwck469ya4', 
             'mintable': True
             }]
 }
```

#### `get_account_info_by_address(address)`  -> `/api/v1/account/{address}`
- Summary: Get an account.
- Description: Gets account metadata for an address.
- Destination: Witness node.
- Rate Limit: 5 requests per IP per second.
- Param `address`: Public address

Sample success result:

```python
> api_client.get_account_info_by_address(address='tbnb1r4gc5ftrkr9ez2khph4h5xxd0mf0hd75jf06gw')

{'status': True, 
 'result': {'address': 'tbnb1fn9z9vn4f44ekz0a3pf80dcy2wh4d5988phjds', 
            'public_key': None,
            'account_number': 666547, 
            'sequence': 0, 
            'balances': [{'symbol': 'BNB', 
                          'free': '1399.99250000',
                          'locked': '0.00000000', 
                          'frozen': '0.00000000'
                          }]
            }
 }
```

#### `get_transaction(tx_hash)`  -> `/api/v1/tx/{hash}`
- Summary: Get a transaction.
- Description: Gets transaction metadata by transaction ID. By default, transactions are returned in a raw format. You may add ?format=json to the end of the path to obtain a more readable response.
- Destination: Seed node.
- Rate Limit: 10 requests per IP per second.
- Param `tx_hash`: Transaction Hash   

Sample success result:

```python
> api_client.get_account_info_by_address(tx_hash='35B8D4070200FFBE045432AC9D87232BEC1FFAD9E6A6C8979CE2FE631B644B9E')

{'status': True, 
 'result': {'address': 'tbnb1fn9z9vn4f44ekz0a3pf80dcy2wh4d5988phjds', 
            'public_key': None,
            'account_number': 666547, 
            'sequence': 0, 
            'balances': [{'symbol': 'BNB', 
                          'free': '1399.99250000',
                          'locked': '0.00000000', 
                          'frozen': '0.00000000'
                          }]
            }
 }
```

#### `get_markets()`  -> `/api/v1/markets`
- Summary: Get market pairs.
- Description: Gets the list of market pairs that have been listed.
- Destination: Witness node.
- Rate Limit: 1 request per IP per second.

Sample success result:

```python
> api_client.get_markets()

{'status': True, 
'result': [{'base_asset_symbol': '000-0E1', 
            'quote_asset_symbol': 'BNB', 
            'price': '1.00000000', 
            'tick_size': '0.00100000',
            'lot_size': '0.00001000'
            },
            {'base_asset_symbol': '100K-9BC', 
            'quote_asset_symbol': 'BTC.B-918', 
            'price': '1.00000000',
            'tick_size': '0.00000001', 
            'lot_size': '1.00000000'
            },
            {'base_asset_symbol': '100K-9BC', 
            'quote_asset_symbol': 'USDT.B-B7C', 
            'price': '1.00000000',
            'tick_size': '0.00000100', 
            'lot_size': '0.01000000'
            },
            ...
           ]
 }
```

#### `get_fees()`  -> `/api/v1/fees`
- Summary: Obtain trading fees information.
- Description: Gets the current trading fees settings.
- Destination: Witness node.
- Rate Limit: 1 request per IP per second.

Sample success result:

```python
> api_client.get_fees()

{'status': True,
 'result': [{'fee': 1000000000, 'msg_type': 'submit_proposal', 'fee_for': 1}, 
            {'fee': 125000, 'msg_type': 'deposit', 'fee_for': 1}, 
            {'fee': 0, 'msg_type': 'vote', 'fee_for': 3}, 
            {'fee': 80000000000, 'msg_type': 'dexList', 'fee_for': 2}, 
            {'fee': 0, 'msg_type': 'orderNew', 'fee_for': 3}, 
            {'fee': 0, 'msg_type': 'orderCancel', 'fee_for': 3}, 
            {'fee': 40000000000, 'msg_type': 'issueMsg', 'fee_for': 2}, 
            {'fee': 20000000000, 'msg_type': 'mintMsg', 'fee_for': 2}, 
            {'fee': 100000000, 'msg_type': 'tokensBurn', 'fee_for': 1}, 
            {'fee': 1000000, 'msg_type': 'tokensFreeze', 'fee_for': 1}, 
            {'multi_transfer_fee': 100000, 'lower_limit_as_multi': 2, 'fixed_fee_params': {'fee': 125000, 
                                                                                           'msg_type': 'send', 
                                                                                           'fee_for': 1}}, 
            {'dex_fee_fields': [{'fee_name': 'ExpireFee', 'fee_value': 100000}, 
                                {'fee_name': 'ExpireFeeNative', 'fee_value': 20000}, 
                                {'fee_name': 'CancelFee', 'fee_value': 100000}, 
                                {'fee_name': 'CancelFeeNative', 'fee_value': 20000}, 
                                {'fee_name': 'FeeRate', 'fee_value': 1000}, 
                                {'fee_name': 'FeeRateNative', 'fee_value': 400}, 
                                {'fee_name': 'IOCExpireFee', 'fee_value': 50000}, 
                                {'fee_name': 'IOCExpireFeeNative', 'fee_value': 10000}]}, 
            {'fee': 1000000000, 'msg_type': 'create_validator', 'fee_for': 1}, 
            {'fee': 100000000, 'msg_type': 'remove_validator', 'fee_for': 1}
            ], 
}
```

#### `get_klines(trading_pair, interval, start_time, end_time, limit)`  -> `/api/v1/klines`
- Summary: Get candlestick bars.
- Description: Gets candlestick/kline bars for a symbol. Bars are uniquely identified by their open time.
- If the time window is larger than limits, only the first n klines will return. In this case, please either shrink the window or increase the limit to get proper amount of klines.
- Rate Limit: 10 requests per IP per second.
-  Param `trading_pair`: <Trading Pair> example: 'BEY-8C6_BNB'     
   Param `interval`: limited to: ['1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M']     
   Param `start_time`: start time in Milliseconds    
   Param `end_time`: end time in Milliseconds    
   Param `limit`: default 300; max 1000.    

Sample success result:

```python
> from binance_dex.api import api_types_instance
> api_client.get_klines(trading_pair=trading_pair,
                        interval=api_types_instance.KLine.interval_4hour,
                        limit=100)

{'status': True, 
 'result': {'hash': '35B8D4070200FFBE045432AC9D87232BEC1FFAD9E6A6C8979CE2FE631B644B9E',
            'height': '4112785', 
            'tx': {'type': 'auth/StdTx', 
                   'value': {'data': None, 
                             'memo': 'hello', 
                             'msg': [{'type': 'cosmos-sdk/Send', 
                                      'value': {'inputs': [{'address': 'tbnb1aeptz56sjep4j2uxt03rcqcp03s9mjgcyex9le',
                                                            'coins': [{'amount': '19999875000', 'denom': 'BNB'}]
                                                            }], 
                                                'outputs': [{'address': 'tbnb1fn9z9vn4f44ekz0a3pf80dcy2wh4d5988phjds', 
                                                             'coins': [{'amount': '19999875000', 'denom': 'BNB'}]
                                                             }]
                                                }
                                      }],
                             'signatures': [{'account_number': '666557', 
                                             'pub_key': {'type': 'tendermint/PubKeySecp256k1', 
                                                         'value': 'AkrIfMumvYIRaNizdcDjnohIwkNyHjl8K7WNbXXL3W16'}, 
                                                         'sequence': '0',
                                                         'signature': '3iijgGYTIROtPHAXKrPiHGgbyhv3ZsW23FOcorvKO7kEoDl6lWaxQk1zMGwdTjBpgU6CCkYRhIj4AnbzozW1xQ=='
                                            }],
                             'source': '1'
                             }
                    }
            }
 }
```