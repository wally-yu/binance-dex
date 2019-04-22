## NodeRPC Lib 

The Binance DEX Python NodeRPC Package provides method to ues Node RPC service.
Using RPC, you may perform low-level operations like executing ABCI queries,
viewing network/consensus state or broadcasting a transaction.    
Official suggested 3 methodologies for RPC:
- `URI over HTTP`
- `JSONRPC over HTTP`
- `JSONRPC over websockets`

This SDK using `JSONRPC over HTTP` methodology.

The original JSONRPC requests can be POST'd to the root RPC endpoint via HTTP (e.g. `http://localhost:27147`).
```python
{
 "method": "broadcast_tx_sync",
 "jsonrpc": "2.0",
 "params": [ "abc" ],
 "id": "dontcare"
}
```
    
Node RPC Service Official Document: https://binance-chain.github.io/api-reference/node-rpc.html

### Usage
`Step1:` Create NodeRPC instance

```python
from binance_dex.node_rpc import BinanceChainNodeRPC

node_rpc_instance = BinanceChainNodeRPC(is_test_net, node_rpc_url)
```
***NOTES:***  
`class BinanceChainNodeRPC` has two positional arguments during initializing:
   - `node_rpc_url` parameter has higher priority, if specified, peer list URL will be `node_rpc_url`
   -  If `node_rpc_url` is `None` and `is_test_net` is `True`, peer list URL will link to 
   `'https://testnet-dex.binance.org/api/v1/peers'`, otherwise `'https://dex.binance.org/api/v1/peers'`   
   
***Tricks:***  
During initializing, you can specify node server by yourself(as mentioned above):
   - If you `specify` the node server, package will check its' healthy state first (Raise `Exception` if unhealthy)
   - If `not specified`, package will automatically detect the first healthy node RPC server in chain (returned from peer list URL)


`Step2:` call the specific function

```python
node_rpc_instance.XXX()
```

#### Service availability:
|Service Name      |JSONRPC over HTTP(Current) |
|---               |:---:                      |
|ABCIInfo          |&radic;                    |
|ABCIQuery         |&bigcirc;                  |
|Block             |&radic;                    |
|BlockResults      |&radic;                    | 
|BlockChainInfo    |&radic;                   |
|BroadcastTxAsync  |&radic;                    |
|BroadcastTxCommit |&radic;                    |
|BroadcastTxSync   |&radic;                    |
|Commit            |&radic;                    |
|ConsensusParams   |&radic;                    |
|ConsensusState    |&ominus;                   |
|DumpConsensusState|&radic;                  |
|Genesis           |&radic;                    |
|Health            |&radic;                  |
|NetInfo           |&radic;                    |
|NumUnconfirmedTxs |&radic;                 |
|Status            |&radic;                    |
|Subscribe         |&times;                    |
|Tx                |&radic;                    |
|TxSearch          |&radic;                  |
|UnconfirmedTxs    |&radic;                    |
|UnsafeDialPeers   |&times;                    |
|UnsafeDialSeeds   |&times;                    |
|Unsubscribe       |&times;                    |
|UnsubscribeAll    |&times;                    |
|Validators        |&radic;                    |
    
    
&ensp;     &radic;: Able to Use  &ensp;&ensp;     &bigcirc;: Unfinished   &ensp;&ensp;    &ominus;:Unstable &ensp;&ensp;  &times;: Unable to supported 

### Referance
The following document list the funcs in `class BinanceChainNodeRPC`. The subheads will appear like that: 
 `RPC service func`  ->  `raw RPC service`, which declare the mapping relationships between Python RPC Package service
 function and raw RPC service type.

#### `get_list()`  -> `Get the list`
- Summary: Show a list of available endpoints.
- Description: An HTTP Get request to the root RPC endpoint shows a list of available endpoints.
- Destination: NA.
- Rate Limit: NA.

Success sample result:

```python
> node_rpc_instance.get_list()

{'status': True, 
 'result': 
    '<html>
        <body><br>
            Available endpoints:<br>
            <a href="//seed-pre-s3.binance.org/abci_info">//seed-pre-s3.binance.org/abci_info</a></br>
            <a href="//seed-pre-s3.binance.org/consensus_state">//seed-pre-s3.binance.org/consensus_state</a></br>
            <a href="//seed-pre-s3.binance.org/dump_consensus_state">//seed-pre-s3.binance.org/dump_consensus_state</a></br>
            <a href="//seed-pre-s3.binance.org/genesis">//seed-pre-s3.binance.org/genesis</a></br>
            <a href="//seed-pre-s3.binance.org/health">//seed-pre-s3.binance.org/health</a></br>
            <a href="//seed-pre-s3.binance.org/net_info">//seed-pre-s3.binance.org/net_info</a></br>
            <a href="//seed-pre-s3.binance.org/num_unconfirmed_txs">//seed-pre-s3.binance.org/num_unconfirmed_txs</a></br>
            <a href="//seed-pre-s3.binance.org/status">//seed-pre-s3.binance.org/status</a></br>
        <br>
            Endpoints that require arguments:<br>
            <a href="//seed-pre-s3.binance.org/abci_query?path=_&data=_&height=_&prove=_">//seed-pre-s3.binance.org/abci_query?path=_&data=_&height=_&prove=_</a></br>
            <a href="//seed-pre-s3.binance.org/block?height=_">//seed-pre-s3.binance.org/block?height=_</a></br>
            <a href="//seed-pre-s3.binance.org/block_results?height=_">//seed-pre-s3.binance.org/block_results?height=_</a></br>
            <a href="//seed-pre-s3.binance.org/blockchain?minHeight=_&maxHeight=_">//seed-pre-s3.binance.org/blockchain?minHeight=_&maxHeight=_</a></br>
            <a href="//seed-pre-s3.binance.org/broadcast_tx_async?tx=_">//seed-pre-s3.binance.org/broadcast_tx_async?tx=_</a></br>
            <a href="//seed-pre-s3.binance.org/broadcast_tx_commit?tx=_">//seed-pre-s3.binance.org/broadcast_tx_commit?tx=_</a></br>
            <a href="//seed-pre-s3.binance.org/broadcast_tx_sync?tx=_">//seed-pre-s3.binance.org/broadcast_tx_sync?tx=_</a></br>
            <a href="//seed-pre-s3.binance.org/commit?height=_">//seed-pre-s3.binance.org/commit?height=_</a></br>
            <a href="//seed-pre-s3.binance.org/consensus_params?height=_">//seed-pre-s3.binance.org/consensus_params?height=_</a></br>
            <a href="//seed-pre-s3.binance.org/subscribe?query=_">//seed-pre-s3.binance.org/subscribe?query=_</a></br>
            <a href="//seed-pre-s3.binance.org/tx?hash=_&prove=_">//seed-pre-s3.binance.org/tx?hash=_&prove=_</a></br>
            <a href="//seed-pre-s3.binance.org/tx_search?query=_&prove=_&page=_&per_page=_">//seed-pre-s3.binance.org/tx_search?query=_&prove=_&page=_&per_page=_</a></br>
            <a href="//seed-pre-s3.binance.org/unconfirmed_txs?limit=_">//seed-pre-s3.binance.org/unconfirmed_txs?limit=_</a></br>
            <a href="//seed-pre-s3.binance.org/unsubscribe?query=_">//seed-pre-s3.binance.org/unsubscribe?query=_</a></br>
            <a href="//seed-pre-s3.binance.org/unsubscribe_all?">//seed-pre-s3.binance.org/unsubscribe_all?</a></br>
            <a href="//seed-pre-s3.binance.org/validators?height=_">//seed-pre-s3.binance.org/validators?height=_</a></br>
        </body>
    </html>'}
```


#### `abci_info()`  -> `ABCIInfo`
- Summary: Get some info about the application.
- Description: Get some info about the application.
- Destination: NA.
- Rate Limit: NA.


Success sample result:

```python
> node_rpc_instance.abci_info()

{
    'status': True, 
    'result': {
        'jsonrpc': '2.0', 
        'id': '', 
        'result': {
            'response': {
                'data': 'BNBChain',
                'last_block_height': '7958684', 
                'last_block_app_hash': 'KI9O19xiqBUitt93GThsvYMs8UJ5fO6OcmKw+q5HQM8='
            }
        }
    }
}
```


#### `block(height)`  -> `Block`
- Summary: Get block at a given height.
- Description: Get block at a given height.
- Destination: NA.
- Rate Limit: NA.
- Param `height`: Height of the block. If no height is provided, it will fetch the latest block.

Success sample result:

```python
> node_rpc_instance.block(height=10)

{
    'status': True,
    'result': {
        'result': {
            'block_meta': {
                'block_id': {
                    'parts': {'total': '1', 'hash': '8C63BE3E3A221B984219CFAA1C196DDF0F202D68293311BFA9EE0B7A9155EACD'}, 
                    'hash': '5701A12896315A121303A979ACB707ACC447E20EFACFCB26174E9ED3997E2F5C'
                }, 
                'header': {
                    'next_validators_hash': '80D9AB0FC10D18CA0E0832D5F4C063C5489EC1443DFB738252D038A82131B27A', 
                    'last_commit_hash': '5442553C06521016756796015AF78FCAC752FFA9E94ACAF4DAA5DF4113B4B354', 
                    'proposer_address': 'E0DD72609CC106210D1AA13936CB67B93A0AEE21', 
                    'consensus_hash': '294D8FBD0B94B767A7EBA9840F299A3586DA7FE6B5DEAD3B7EECBA193C400F93', 
                    'chain_id': 'Binance-Chain-Nile', 
                    'data_hash': '',
                    'app_hash': 'E7D96927FD82FD910624AA8034B8A527FCEB1F7AB353DE789A3ECA8D400BDE31', 
                    'time': '2019-03-07T01:57:22.135103158Z', 
                    'version': {'app': '0', 'block': '10'}, 
                    'height': '10', 
                    'total_txs': '0', 
                    'validators_hash': '80D9AB0FC10D18CA0E0832D5F4C063C5489EC1443DFB738252D038A82131B27A', 
                    'last_block_id': {
                        'parts': {'total': '1', 'hash': 'BB3C36D5BBDAB441A7339385C071C4E804C4C3DD5C7BC15D60BC658A6B261906'},
                        'hash': '1AF674F804E277354E8742176ECA74E338F52C237E6DBFF92819D75037E4F651'
                    }, 
                    'evidence_hash': '', 
                    'last_results_hash': '', 
                    'num_txs': '0'
                }
            }, 
            'block': {
                'header': {
                    'next_validators_hash': '80D9AB0FC10D18CA0E0832D5F4C063C5489EC1443DFB738252D038A82131B27A', 
                    'last_commit_hash': '5442553C06521016756796015AF78FCAC752FFA9E94ACAF4DAA5DF4113B4B354', 
                    'proposer_address': 'E0DD72609CC106210D1AA13936CB67B93A0AEE21', 
                    'consensus_hash': '294D8FBD0B94B767A7EBA9840F299A3586DA7FE6B5DEAD3B7EECBA193C400F93', 
                    'chain_id': 'Binance-Chain-Nile', 
                    'data_hash': '', 
                    'app_hash': 'E7D96927FD82FD910624AA8034B8A527FCEB1F7AB353DE789A3ECA8D400BDE31', 
                    'time': '2019-03-07T01:57:22.135103158Z', 
                    'version': {'app': '0', 'block': '10'}, 
                    'height': '10', 
                    'total_txs': '0', 
                    'validators_hash': '80D9AB0FC10D18CA0E0832D5F4C063C5489EC1443DFB738252D038A82131B27A', 
                    'last_block_id': {
                        'parts': {'total': '1', 'hash': 'BB3C36D5BBDAB441A7339385C071C4E804C4C3DD5C7BC15D60BC658A6B261906'}, 
                        'hash': '1AF674F804E277354E8742176ECA74E338F52C237E6DBFF92819D75037E4F651'
                    }, 
                    'evidence_hash': '', 
                    'last_results_hash': '', 
                    'num_txs': '0'
                }, 
                'evidence': {'evidence': None}, 
                'last_commit': {
                    'block_id': {
                        'parts': {'total': '1', 'hash': 'BB3C36D5BBDAB441A7339385C071C4E804C4C3DD5C7BC15D60BC658A6B261906'},
                        'hash': '1AF674F804E277354E8742176ECA74E338F52C237E6DBFF92819D75037E4F651'
                    }, 
                    'precommits': [ 
                        None, 
                        {   
                            'block_id': {
                                'parts': {'total': '1', 'hash': 'BB3C36D5BBDAB441A7339385C071C4E804C4C3DD5C7BC15D60BC658A6B261906'}, 
                                'hash': '1AF674F804E277354E8742176ECA74E338F52C237E6DBFF92819D75037E4F651'
                             }, 
                            'height': '9', 
                            'validator_address': '18E69CC672973992BB5F76D049A5B2C5DDF77436', 
                            'round': '0', 
                            'validator_index': '1', 
                            'timestamp': '2019-03-07T01:57:22.21160109Z', 
                            'type': 2,
                            'signature': 'WYzQMqP+BYFh5EYRXCePgUYQVV0Lor1lJ0Fhk4zW0MeFnoYo8pSE/Y7j5J0arq44eCwyYqjJQi+zByDotVYdAw=='
                        }, 
                        {
                            'block_id': {
                                'parts': {'total': '1', 'hash': 'BB3C36D5BBDAB441A7339385C071C4E804C4C3DD5C7BC15D60BC658A6B261906'}, 
                                'hash': '1AF674F804E277354E8742176ECA74E338F52C237E6DBFF92819D75037E4F651'
                            }, 
                            'height': '9', 'validator_address': '344C39BB8F4512D6CAB1F6AAFAC1811EF9D8AFDF', 
                            'round': '0', 
                            'validator_index': '2', 
                            'timestamp': '2019-03-07T01:57:22.215324364Z', 
                            'type': 2, 
                            'signature': 'hfzgbkbiTgqUWMLZIIDx+X6qj15nmIcdUvCd8dt89v9yjSsUbKRL4tn9JuympyUJ36gRA/gbMnvGwmwHRPLuCg=='
                        }, 
                        ...,
                        {
                            'block_id': {
                                'parts': {'total': '1', 'hash': 'BB3C36D5BBDAB441A7339385C071C4E804C4C3DD5C7BC15D60BC658A6B261906'},
                                'hash': '1AF674F804E277354E8742176ECA74E338F52C237E6DBFF92819D75037E4F651'
                            }, 
                            'height': '9', 
                            'validator_address': 'FC3108DC3814888F4187452182BC1BAF83B71BC9', 
                            'round': '0', 
                            'validator_index': '10', 
                            'timestamp': '2019-03-07T01:57:22.129274247Z', 
                            'type': 2, 
                            'signature': '55nxVx9iBFPTEuhuN806WyyBUwX1Hf4h24JSalcR6duQRxjFrLgm//eo7Bhh93jMikBTMA2ThQ+Mzc3A/wd8Dg=='
                        }
                    ]
                },   
                'data': {'txs': None}
            }
        }, 
        'id': '', 
        'jsonrpc': '2.0'
    }
}
```


#### `block_results(height)`  -> `BlockResults`
- Summary: Get block_results.
- Description: BlockResults gets ABCIResults at a given height. Results are for the height of the block containing the txs. 
Thus response.results[5] is the results of executing getBlock(h).Txs[5]   ***TO DO???***  
- Destination: NA.
- Rate Limit: NA.
- Param `height`: Height of the block. If no height is provided, it will fetch the latest block.

Success sample result:

```python
> node_rpc_instance.block_results(height=100)

{
    'status': True, 
    'result': {
        'result': {
            'height': '100', 
            'results': {
                'BeginBlock': {}, 
                'DeliverTx': None, 
                'EndBlock': {'validator_updates': None}
            }
        }, 
        'id': '', 
        'jsonrpc': '2.0'
    }
}
```


#### `broadcast_tx_async(tx_id)`  -> `BroadcastTxAsync`
- Summary: Returns right away, with no response.
- Description: Returns right away, with no response.
- Destination: NA.
- Rate Limit: NA.
- Param `tx_id`: The transaction.

Success sample result:

```python
> node_rpc_instance.broadcast_tx_async(tx_id='123')

{   
    'status': True,
    'result': {
        'result': {
            'code': 0, 
            'log': '', 
            'hash': 'A665A45920422F9D417E4867EFDC4FB8A04A1F3FFF1FA07E998E86F7F7A27AE3', 
            'data': ''
        }, 
        'id': '', 
        'jsonrpc': '2.0'
    }
}
```


#### `broadcast_tx_sync(tx_id)`  -> `BroadcastTxSync`
- Summary: Returns with the response from CheckTx.
- Description: Returns with the response from CheckTx.
- Destination: NA.
- Rate Limit: NA.
- Param `tx_id`: The transaction.

Success sample result:

```python
> node_rpc_instance.broadcast_tx_sync(tx_id='123')

{   
    'status': True,
    'result': {
        'result': {
            'code': 65538, 
            'log': '{"codespace":1,"code":2,"abci_code":65538,"message":"tx parse error"}', 
            'hash': 'A665A45920422F9D417E4867EFDC4FB8A04A1F3FFF1FA07E998E86F7F7A27AE3', 
            'data': ''
        }, 
        'id': '', 
        'jsonrpc': '2.0'
    }
}
```


#### `broadcast_tx_commit(tx_id)`  -> `BroadcastTxCommit`
- Summary: CONTRACT: only returns error if mempool.CheckTx() errs or if we timeout waiting for tx to commit.
- Description: If CheckTx or DeliverTx fail, no error will be returned, 
but the returned result will contain a non-OK ABCI code.
- Destination: NA.
- Rate Limit: NA.
- Param `tx_id`: The transaction.

Success sample result:

```python
> node_rpc_instance.broadcast_tx_commit(tx_id='123')

{
    'status': True,
    'result': {
        'result': {
            'check_tx': {
                'code': 65538, 
                'log': '{"codespace":1,"code":2,"abci_code":65538,"message":"tx parse error"}'
            }, 
            'height': '0', 
            'hash': 'A665A45920422F9D417E4867EFDC4FB8A04A1F3FFF1FA07E998E86F7F7A27AE3', 
            'deliver_tx': {}
        }, 
        'id': '', 
        'jsonrpc': '2.0'
    }
}
```


#### `get_commit(height)`  -> `Commit`
- Summary: Get block commit at a given height.
- Description: Get block commit at a given height.
- Destination: NA.
- Rate Limit: NA.
- Param `height`: Height of the block. If no height is provided, it will fetch the latest block.

Success sample result:

```python
> node_rpc_instance.get_commit(tx_id='123')

{	
    'status': True, 
    'result': {
        'result': {
            'canonical': True,
            'signed_header': {
                'header': {
                    'next_validators_hash': '80D9AB0FC10D18CA0E0832D5F4C063C5489EC1443DFB738252D038A82131B27A',
                    'last_commit_hash': '5442553C06521016756796015AF78FCAC752FFA9E94ACAF4DAA5DF4113B4B354',
                    'proposer_address': 'E0DD72609CC106210D1AA13936CB67B93A0AEE21',
                    'consensus_hash': '294D8FBD0B94B767A7EBA9840F299A3586DA7FE6B5DEAD3B7EECBA193C400F93',
                    'chain_id': 'Binance-Chain-Nile',
                    'data_hash': '',
                    'app_hash': 'E7D96927FD82FD910624AA8034B8A527FCEB1F7AB353DE789A3ECA8D400BDE31',
                    'time': '2019-03-07T01:57:22.135103158Z',
                    'version': {'app': '0', 'block': '10'},
                    'height': '10',
                    'total_txs': '0',
                    'validators_hash': '80D9AB0FC10D18CA0E0832D5F4C063C5489EC1443DFB738252D038A82131B27A',
                    'last_block_id': {
                        'parts': {
                            'total': '1',
                            'hash': 'BB3C36D5BBDAB441A7339385C071C4E804C4C3DD5C7BC15D60BC658A6B261906'
                        },
                        'hash': '1AF674F804E277354E8742176ECA74E338F52C237E6DBFF92819D75037E4F651'
                    },
                    'evidence_hash': '',
                    'last_results_hash': '',
                    'num_txs': '0'
                },
                'commit': {
                    'block_id': {
                        'parts': {
                            'total': '1',
                            'hash': '8C63BE3E3A221B984219CFAA1C196DDF0F202D68293311BFA9EE0B7A9155EACD'
                        },
                        'hash': '5701A12896315A121303A979ACB707ACC447E20EFACFCB26174E9ED3997E2F5C'
                    },
                    'precommits': [
                        None, 
                        {
                            'block_id': {
                                'parts': {
                                    'total': '1',
                                    'hash': '8C63BE3E3A221B984219CFAA1C196DDF0F202D68293311BFA9EE0B7A9155EACD'
                                },
                                'hash': '5701A12896315A121303A979ACB707ACC447E20EFACFCB26174E9ED3997E2F5C'
                            },
                            'height': '10',
                            'validator_address': '18E69CC672973992BB5F76D049A5B2C5DDF77436',
                            'round': '1',
                            'validator_index': '1',
                            'timestamp': '2019-03-07T01:57:27.663157746Z',
                            'type': 2,
                            'signature': 'ZrnapmTAiJrhm0DVIoTzRbJG+FDCAxBpfamYxZj2eg0+wY0+KDg48sDPlD+chk97ti01PukuVsftn4U6HXbkCA=='
                        }, 
                        {
                            'block_id': {
                                'parts': {
                                    'total': '1',
                                    'hash': '8C63BE3E3A221B984219CFAA1C196DDF0F202D68293311BFA9EE0B7A9155EACD'
                                },
                                'hash': '5701A12896315A121303A979ACB707ACC447E20EFACFCB26174E9ED3997E2F5C'
                            },
                            'height': '10',
                            'validator_address': '344C39BB8F4512D6CAB1F6AAFAC1811EF9D8AFDF',
                            'round': '1',
                            'validator_index': '2',
                            'timestamp': '2019-03-07T01:57:27.669872809Z',
                            'type': 2,
                            'signature': 'VRB1MYpxCCA8EnjWSRl4cTMP9P7uBEvkPRtSr7grgpPEERfc6J5/gySD6LKkOe1nNpyeYi1RU/vqAibSEnMNDQ=='
                        }, 
                        '...OMIT...',
                        {
                            'block_id': {
                                'parts': {
                                    'total': '1',
                                    'hash': '8C63BE3E3A221B984219CFAA1C196DDF0F202D68293311BFA9EE0B7A9155EACD'
                                },
                                'hash': '5701A12896315A121303A979ACB707ACC447E20EFACFCB26174E9ED3997E2F5C'
                            },
                            'height': '10',
                            'validator_address': 'FC3108DC3814888F4187452182BC1BAF83B71BC9',
                            'round': '1',
                            'validator_index': '10',
                            'timestamp': '2019-03-07T01:57:27.738256001Z',
                            'type': 2,
                            'signature': 'Hw1BdfL79cLsTJhb406k+1MvU27zL1pdehLBHqkzF5NNOn/LrL4+u3t2ANwHaxX5OFijgZW5P1T7ECVrvJr0CQ=='
                        }
                    ]
                }
            }
        },
        'id': '',
        'jsonrpc': '2.0'
    }
}

```


#### `consensus_params(height)`  -> `ConsensusParams`
- Summary: Get the consensus parameters at the given block height.
- Description: Get the consensus parameters at the given block height.  
- Destination: NA.
- Rate Limit: NA.
- Param `height`: Height of the block. If no height is provided, it will fetch the latest block.

Success sample result:

```python
> node_rpc_instance.consensus_params(height=100)

{
    'status': True, 
    'result': {
        'result': {
            'consensus_params': {
                'validator': {
                    'pub_key_types': ['ed25519']
                }, 
                'block_size': {
                    'max_bytes': '1048576', 
                    'max_gas': '-1'
                }, 
                'evidence': {'max_age': '100000'}
            }, 
            'block_height': '100'
        }, 
        'id': '', 
        'jsonrpc': '2.0'
    }
}
```


#### `consensus_state()`  -> `ConsensusState`      *UNSTABLE*
- Summary: ConsensusState returns a concise summary of the consensus state.
- Description: ConsensusState returns a concise summary of the consensus state.  
- Destination: NA.
- Rate Limit: NA.

Success sample result:  

```python
> node_rpc_instance.consensus_state()

{
    'status': True, 
    'result': {
        'result': {
            'round_state': {
                'locked_block_hash': 'D18F0591B541756B057B3B9615DEEF29CDA80405459C9374E9B66D7A26FE0D6B', 
                'proposal_block_hash': 'D18F0591B541756B057B3B9615DEEF29CDA80405459C9374E9B66D7A26FE0D6B', 
                'valid_block_hash': 'D18F0591B541756B057B3B9615DEEF29CDA80405459C9374E9B66D7A26FE0D6B', 
                'start_time': '2019-04-15T05:15:38.972350822Z', 
                'height/round/step': '8393276/0/6'
                'height_vote_set': [
                    {
                        'prevotes_bit_array': 'BA{11:_xx_xxxx_xx} 800000000000/1100000000000 = 0.73', 
                        'prevotes': [
                            'nil-Vote', 
                            '...OMIT...',
                            'Vote{10:FC3108DC3814 8393276/00/1(Prevote) D18F0591B541 C43070EE0DD6 @ 2019-04-15T05:15:37.868577941Z}'
                        ], 
                        'precommits_bit_array': 'BA{11:_xx___xx___} 400000000000/1100000000000 = 0.36', 
                        'round': '0', 
                        'precommits': [
                            'nil-Vote', 
                            '...OMIT...',
                            'nil-Vote'
                        ]
                    }, 
                    {
                        'prevotes_bit_array': 'BA{11:___________} 0/1100000000000 = 0.00', 
                        'prevotes': [
                            'nil-Vote', 
                            '...OMIT...',
                            'nil-Vote'
                        ], 
                        'precommits_bit_array': 'BA{11:___________} 0/1100000000000 = 0.00',
                        'round': '1', 
                        'precommits': [
                            'nil-Vote', 
                            '...OMIT...',
                            'nil-Vote'
                        ]
                    }
                ], 
            }
        },
        'id': '', 
        'jsonrpc': '2.0'
    }
}
```


#### `genesis()`  -> `Genesis`
- Summary: Get genesis file.
- Description: Get genesis file.  
- Destination: NA.
- Rate Limit: NA.

Success sample result:

```python
> node_rpc_instance.genesis()

{
    'status': True, 
    'result': {
        'result': {
            'genesis': {
                'app_hash': '', 
                'genesis_time': '2019-03-07T01:52:07.500913003Z', 
                'chain_id': 'Binance-Chain-Nile',
                'consensus_params': {
                    'validator': {'pub_key_types': ['ed25519']}, 
                    'block_size': {'max_bytes': '1048576', 'max_gas': '-1'}, 
                    'evidence': {'max_age': '100000'}
                }, 
                'app_state': {
                    'accounts': [
                        {
                            'name': 'Fuji', 
                            'address': 'tbnb12hlquylu78cjylk5zshxpdj6hf3t0tahwjt3ex', 
                            'valaddr': '7B343E041CA130000A8BC00C35152BD7E7740037'
                        }, 
                        {
                            'name': 'Kita', 
                            'address': 'tbnb167yp9jkv6uaqnyq62gfkx82xmfny0cl9xe04zj', 
                            'valaddr': 'E0DD72609CC106210D1AA13936CB67B93A0AEE21'
                        }, 
                        '...OMIT...'
                    ], 
                    'gentxs': [
                        {
                            'type': 'auth/StdTx', 
                            'value': {
                                'msg': [
                                    {
                                        'type': 'cosmos-sdk/MsgCreateValidatorProposal', 
                                        'value': {
                                            'proposal_id': '0', 
                                            'MsgCreateValidator': {
                                                'validator_address': 'bva12hlquylu78cjylk5zshxpdj6hf3t0tahqmr98n', 
                                                'Commission': {
                                                    'max_change_rate': '0', 
                                                    'max_rate': '0', 
                                                    'rate': '0'
                                                }, 
                                                'Description': {
                                                    'identity': '', 
                                                    'website': '', 
                                                    'moniker': 'Fuji', 
                                                    'details': ''
                                                }, 
                                                'delegation': {
                                                    'amount': '100000000000', 
                                                    'denom': 'BNB'
                                                }, 
                                                'delegator_address': 'tbnb12hlquylu78cjylk5zshxpdj6hf3t0tahwjt3ex', 
                                                'pubkey': {
                                                    'type': 'tendermint/PubKeyEd25519', 
                                                    'value': 'Sl1HU+t5+S6A7+It96yk9mak9Ev4HFNsSgnUucW2VLU='
                                                }
                                            }
                                        }
                                    }
                                ], 
                                'source': '0', 
                                'data': None, 
                                'signatures': [
                                    {
                                        'account_number': '0', 
                                        'sequence': '0', 
                                        'pub_key': {
                                            'type': 'tendermint/PubKeySecp256k1', 
                                            'value': 'A+gcCBsoefY1d9TnkIOPV8IX5+/i/BTrMvFU7vG9RXIk'
                                        }, 
                                        'signature': 'oWWGy2kN9yQDVJ/aLE7N/Si/lTTsce3k8VRsdtzO6doSw2eFL9v8wB3GdTaOBvuJGJti73WPGaEN8fbUjao5hw=='
                                    }
                                ], 
                                'memo': '1bca643058c56f9c20ebaaad1739522ee7d11cd6@172.18.10.204:26656'
                            }
                        }, 
                        '...OMIT...'
                    ], 
                    'stake': {
                        'pool': {
                            'loose_tokens': '4000000000000000', 
                            'bonded_tokens': '0'
                        }, 
                        'params': {
                            'unbonding_time': '604800000000000', 
                            'bond_denom': 'BNB', 
                            'max_validators': 15
                        }, 
                        'validators': None, 
                        'bonds': None
                    }, 
                    'tokens': [
                        {   
                            'name': 'Binance Chain Native Token', 
                            'owner': 'tbnb12hlquylu78cjylk5zshxpdj6hf3t0tahwjt3ex', 
                            'symbol': 'BNB', 
                            'total_supply': '20000000000000000', 
                            'mintable': False
                        }
                    ], 
                    'param': {
                        'fees': [
                            {'type': 'params/FixedFeeParams', 'value': {'msg_type': 'submit_proposal', 'fee_for': 1, 'fee': '1000000000'}}, 
                            {'type': 'params/FixedFeeParams', 'value': {'msg_type': 'deposit', 'fee_for': 1, 'fee': '125000'}},
                            {'type': 'params/FixedFeeParams', 'value': {'msg_type': 'vote', 'fee_for': 3, 'fee': '0'}}, 
                            {'type': 'params/FixedFeeParams', 'value': {'msg_type': 'dexList', 'fee_for': 2, 'fee': '80000000000'}},
                            {'type': 'params/FixedFeeParams', 'value': {'msg_type': 'orderNew', 'fee_for': 3, 'fee': '0'}}, 
                            {'type': 'params/FixedFeeParams', 'value': {'msg_type': 'orderCancel', 'fee_for': 3, 'fee': '0'}}, 
                            {'type': 'params/FixedFeeParams', 'value': {'msg_type': 'issueMsg', 'fee_for': 2, 'fee': '40000000000'}}, 
                            {'type': 'params/FixedFeeParams', 'value': {'msg_type': 'mintMsg', 'fee_for': 2, 'fee': '20000000000'}},
                            {'type': 'params/FixedFeeParams', 'value': {'msg_type': 'tokensBurn', 'fee_for': 1, 'fee': '100000000'}},
                            {'type': 'params/FixedFeeParams', 'value': {'msg_type': 'tokensFreeze', 'fee_for': 1, 'fee': '1000000'}}, 
                            {'type': 'params/TransferFeeParams', 'value': {'multi_transfer_fee': '100000', 'fixed_fee_params': {'msg_type': 'send', 'fee_for': 1, 'fee': '125000'}, 'lower_limit_as_multi': '2'}},
                            {
                                'type': 'params/DexFeeParam', 
                                    'value': {
                                    'dex_fee_fields': [
                                        {'fee_value': '100000', 'fee_name': 'ExpireFee'}, 
                                        {'fee_value': '20000', 'fee_name': 'ExpireFeeNative'}, 
                                        {'fee_value': '100000', 'fee_name': 'CancelFee'}, 
                                        {'fee_value': '20000', 'fee_name': 'CancelFeeNative'}, 
                                        {'fee_value': '1000', 'fee_name': 'FeeRate'}, 
                                        {'fee_value': '400', 'fee_name': 'FeeRateNative'}, 
                                        {'fee_value': '50000', 'fee_name': 'IOCExpireFee'}, 
                                        {'fee_value': '10000', 'fee_name': 'IOCExpireFeeNative'}
                                    ]
                                }
                            }
                        ]
                    }, 
                    'dex': {}, 
                    'gov': {    
                        'voting_period': {'voting_period': '14400000000000'}, 
                        'deposit_period': {
                            'max_deposit_period': '1209600000000000', 
                            'min_deposit': [{'amount': '200000000000', 'denom': 'BNB'}]
                        }, 
                        'tallying_procedure': {'veto': '33400000', 'threshold': '50000000', 'governance_penalty': '1000000'}, 
                        'starting_proposalID': '1'
                    }
                }
            }
        },
        'id': '', 
        'jsonrpc': '2.0'
    }
}
```


#### `net_info()`  -> `NetInfo`
- Summary: Get network info.
- Description: Get network info.  
- Destination: NA.
- Rate Limit: NA.

Success sample result:

```python
> node_rpc_instance.net_info()

{
    'status': True,
    'result': {
        'result': {
            'listening': True,
            'peers': [
                {
                    'remote_ip': '3.84.71.211',
                    'is_outbound': True,
                    'connection_status': {
                        'RecvMonitor': {
                            'BytesRem': '0',
                            'Samples': '3022947',
                            'TimeRem': '0',
                            'Progress': 0,
                            'Active': True,
                            'CurRate': '19191',
                            'Idle': '0',
                            'Bytes': '8388755229',
                            'AvgRate': '19701',
                            'Duration': '425799500000000',
                            'Start': '2019-04-10T06:58:59.94Z',
                            'InstRate': '18391',
                            'PeakRate': '1135920'
                        },
                        'Channels': [
                            {
                                'SendQueueSize': '0',
                                'ID': 48,
                                'Priority': '5',
                                'RecentlySent': '84',
                                'SendQueueCapacity': '1'
                            }, 
                            '...OMIT...'
                        ],
                        'SendMonitor': {
                            'BytesRem': '0',
                            'Samples': '2871732',
                            'TimeRem': '0',
                            'Progress': 0,
                            'Active': True,
                            'CurRate': '2527',
                            'Idle': '40000000',
                            'Bytes': '1635891482',
                            'AvgRate': '3842',
                            'Duration': '425799500000000',
                            'Start': '2019-04-10T06:58:59.94Z',
                            'InstRate': '389',
                            'PeakRate': '106667'
                        },
                        'Duration': '425799543480563'
                    },
                    'node_info': {
                        'protocol_version': {
                            'app': '0',
                            'block': '10',
                            'p2p': '7'
                        },
                        'version': '0.30.1',
                        'id': '381934b9b3f862d1e81e699d8e1d38929f330cef',
                        'network': 'Binance-Chain-Nile',
                        'listen_addr': 'aa13359cd244f11e988520ad55ba7f5a-c3963b80c9b991b7.elb.us-east-1.amazonaws.com:27146',
                        'channels': '354020212223303800',
                        'other': {
                            'tx_index': 'on',
                            'rpc_address': 'tcp://0.0.0.0:27147'
                        },
                        'moniker': 'data-seed-0'
                    }
                },
                '...OMIT...'
            ],
            'n_peers': '3',
            'listeners': [
                'Listener(@a41086771245011e988520ad55ba7f5a-5f7331395e69b0f3.elb.us-east-1.amazonaws.com:27146)'
            ]
        },
        'id': '',
        'jsonrpc': '2.0'
    }
}
```


#### `num_unconfirmed_txs()`  -> `NumUnconfirmedTxs`
- Summary: Get number of unconfirmed transactions.
- Description: Get number of unconfirmed transactions.
- Destination: NA.
- Rate Limit: NA.

Success sample result:

```python
> node_rpc_instance.num_unconfirmed_txs()

{
    'status': True,
    'result': {
        'result': {
            'n_txs': '0', 
            'txs': []
        }, 
        'id': '', 
        'jsonrpc': '2.0'
    }
}
```


#### `status()`  -> `Status`
- Summary: Get Tendermint status including node info, pubkey, latest block hash, app hash, block height and time.
- Description: Get Tendermint status including node info, pubkey, latest block hash, app hash, block height and time.
- Destination: NA.
- Rate Limit: NA.

Success sample result:

```python
> node_rpc_instance.status()

{
    'status': True,
    'result': {
        'result': {
            'sync_info': {
                'catching_up': False,
                'latest_app_hash': '98180C8B988110A6307D307D9C52ED4F1BD1CADA0865F8159F3956525375764C',
                'latest_block_hash': '1B822430188075E4376BDB1179130A2811C254C0D2F06F4BBD478E756DDF7542',
                'latest_block_time': '2019-04-15T05:15:39.406162498Z',
                'latest_block_height': '8393280'
            },
            'validator_info': {
                'voting_power': '0',
                'address': 'D618BA9C703B1E2A6BC7BAB0A0E66CE5FA32BCBA',
                'pub_key': {
                    'type': 'tendermint/PubKeyEd25519',
                    'value': 'fHM2q0J/CBzMnfH1TYtKsMQ+VmJQaq5ZsMMtmT2VoFs='
                }
            },
            'node_info': {
                'protocol_version': {
                    'app': '0',
                    'block': '10',
                    'p2p': '7'
                },
                'version': '0.30.1',
                'id': '2726550182cbc5f4618c27e49c730752a96901e8',
                'network': 'Binance-Chain-Nile',
                'listen_addr': 'a41086771245011e988520ad55ba7f5a-5f7331395e69b0f3.elb.us-east-1.amazonaws.com:27146',
                'channels': '354020212223303800',
                'other': {
                    'tx_index': 'on',
                    'rpc_address': 'tcp://0.0.0.0:27147'
                },
                'moniker': 'seed'
            }
        },
        'id': '',
        'jsonrpc': '2.0'
    }
}
```


#### `transaction(hash)`  -> `Tx`
- Summary: Tx allows you to query the transaction results. 
- Description: nil could mean the transaction is in the mempool, invalidated, or was not sent in the first place.
- Destination: NA.
- Rate Limit: NA.
- Param `hash`:  hash of the transaction.

Success sample result:

```python
> node_rpc_instance.transaction(hash='C3FF309D7226768FC48B5E2D2D91719D77BAFA66DF7D3C53FCB212075DA83EA3')

{
    'status': True,
    'result': {
        'result': {
            'height': '7554709',
            'tx_result': {
                'log': 'Msg 0: ',
                'tags': [{
                    'key': 'YWN0aW9u',
                    'value': 'b3JkZXJOZXc='
                }],
                'data': 'eyJvcmRlcl9pZCI6IjFENTE4QTI1NjNCMENCOTEyQUQ3MERFQjdBMThDRDdFRDJGQkI3RDQtMTcifQ=='
            },
            'tx': '4AHwYl3uCmbObcBDChQdUYolY7DLkSrXDet6GM1+0vu31BIrMUQ1MThBMjU2M0IwQ0I5MTJBRDcwREVCN0ExOENEN0VEMkZCQjdENC0xNxoMMTAwSy05QkNfQk5CIAIoATCA4I2E3csBOJBOQAEScAom61rphyEDfd0CH3JYj3jMG0VLIE8zyIjfRNNMf7OUXk8WLuEZYRISQGu/gqP4ikvXn5mY3/EZJ2wMqbTi+guJBj7DXtGtVGBAY8LiliUE2UhD1YtBdMjgQcuGExOES1Qbuck4aB+q0U8YvtcoIBAgAQ==',
            'hash': 'C3FF309D7226768FC48B5E2D2D91719D77BAFA66DF7D3C53FCB212075DA83EA3',
            'index': 1
        },
        'id': '',
        'jsonrpc': '2.0'
    }
}
```


#### `unconfirmed_txs()`  -> `UnconfirmedTxs`
- Summary: Get unconfirmed transactions (maximum ?limit entries) including their number.
- Description: Get unconfirmed transactions (maximum ?limit entries) including their number.
- Destination: NA.
- Rate Limit: NA.

Success sample result:

```python
> node_rpc_instance.unconfirmed_txs()

{
    'status': True,
    'result': {
        'result': {
            'n_txs': '0', 
            'txs': []
        }, 
        'id': '', 
        'jsonrpc': '2.0'
    }
}
```


#### `validators(height)`  -> `Validators`
- Summary: Get the validator set at the given block height.
- Description: Get the validator set at the given block height.
- Destination: NA.
- Rate Limit: NA.
- Param `height`: Height of the block. If no height is provided, it will fetch the latest block.

Success sample result:

```python
> node_rpc_instance.validators(height=10)

{   
    'status': True,
    'result': {
        'result': {
            'block_height': '10',
            'validators': [
                {
                    'voting_power': '100000000000',
                    'address': '06FD60078EB4C2356137DD50036597DB267CF616',
                    'proposer_priority': '-100000000000',
                    'pub_key': {
                        'type': 'tendermint/PubKeyEd25519',
                        'value': '4Xy+nCDNz9+HazsSl40yZKAH/KqnHEzbcB2evAMj9E8='
                    }
                }, 
                '...OMIT...'
            ]    
        },
        'id': '',
        'jsonrpc': '2.0'
    }    
}
```
