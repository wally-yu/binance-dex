import requests
import inspect
from binance_dex.lib.common import std_ret

IS_TEST_NET = False
PEER_LIST_TEST_NET = 'https://testnet-dex.binance.org/api/v1/peers'
PEER_LIST_MAIN_NET = 'https://dex.binance.org/api/v1/peers'

NODE_RPC_ENTRY_POINT_MAPPING = {
    '_helth_check': '/health',
    'get_list': '',
    'abci_info': '/abci_info',
    'block': '/block',
    'block_results': '/block_results',
    'broadcast_tx_async': '/broadcast_tx_async',
    'broadcast_tx_sync': '/broadcast_tx_sync',
    'broadcast_tx_commit': '/broadcast_tx_commit',
    'get_commit': '/commit',
    'consensus_params': '/consensus_params',
    'consensus_state': '/consensus_state',
    'genesis': '/genesis',


}

class BinanceChainNodeRPC(object):
    """
    Node RPC Service
    Official Document: https://binance-chain.github.io/api-reference/node-rpc.html
    Official suggested 3 methodologies for RPC:
     - URI over HTTP
     - JSONRPC over HTTP
     - JSONRPC over websockets

    This SDK using "JSONRPC over HTTP" methodology
    """

    def __init__(self, node_rpc_url=None, is_test_net=False):
        # Customized RPC node
        if node_rpc_url:
            self.node_url = node_rpc_url

            # Check node server health
            print('Using customized RPC server: %s\nChecking Health...' % node_rpc_url)
            if self._helth_check(node_rpc_url):
                # healthy, init done
                print('Customized RPC server is healthy\n')
            else:
                # not healthy
                raise Exception('Node %s is not healthy')
        else:
            # Binance RPC node
            print('Using Binance RPC server, trying to find a healthy node server...')
            peer_list_url = PEER_LIST_TEST_NET if is_test_net else PEER_LIST_MAIN_NET
            # Find one healthy node
            self.node_url = self._find_healthy_node(peer_list_url)
            print('Successfully found healthy node RPC server: %s\n' % self.node_url)

    def _find_healthy_node(self, peer_list_url):
        req = requests.get(peer_list_url)
        req.raise_for_status()  # raise exception if calling peer list wrong
        ret = req.json()
        for node in ret:
            # Check capabilities
            capabilities = node['capabilities']
            if 'node' in capabilities:
                # Check Health
                listen_addr = node['listen_addr']
                self.node_url = listen_addr
                if self._helth_check(listen_addr):
                    # Found the healthy one, return its listen address
                    return listen_addr
                else:
                    # not healthy, find next node
                    continue
            else:
                continue
        # didn't find any, return None
        return None

    def _helth_check(self, node_url):
        req = self._wrapped_request()
        if req.status_code == 200:
            return True
        else:
            return False

    def get_list(self):
        """
        shows a list of available endpoints
        Sample Return:
        {'status': True, 'result': '<html><body><br>Available endpoints:<br><a href="//seed-pre-s3.binance.org/
        abci_info">//seed-pre-s3.binance.org/abci_info</a></br><a href="//seed-pre-s3.binance.org/consensus_state">
        //seed-pre-s3.binance.org/consensus_state</a></br><a href="//seed-pre-s3.binance.org/dump_consensus_state">
        //seed-pre-s3.binance.org/dump_consensus_state</a></br><a href="//seed-pre-s3.binance.org/genesis">
        //seed-pre-s3.binance.org/genesis</a></br><a href="//seed-pre-s3.binance.org/health">//seed-pre-s3.binance.org
        /health</a></br><a href="//seed-pre-s3.binance.org/net_info">//seed-pre-s3.binance.org/net_info</a></br>
        <a href="//seed-pre-s3.binance.org/num_unconfirmed_txs">//seed-pre-s3.binance.org/num_unconfirmed_txs</a></br>
        <a href="//seed-pre-s3.binance.org/status">//seed-pre-s3.binance.org/status</a></br>
        <br>Endpoints that require arguments:<br><a href="//seed-pre-s3.binance.org/abci_query?path=_&data=_&height=
        _&prove=_">//seed-pre-s3.binance.org/abci_query?path=_&data=_&height=_&prove=_</a></br>
        <a href="//seed-pre-s3.binance.org/block?height=_">//seed-pre-s3.binance.org/block?height=_</a></br>
        <a href="//seed-pre-s3.binance.org/block_results?height=_">
        ... ...
        //seed-pre-s3.binance.org/validators?height=_</a></br></body></html>'}

        """
        return std_ret(status=True,
                       data=self._wrapped_request().text)

    def abci_info(self):
        """
        Get some info about the application

        Sample Return:
        {'status': True, 'result': {'jsonrpc': '2.0', 'id': '', 'result': {'response': {'data': 'BNBChain',
        'last_block_height': '7958684', 'last_block_app_hash': 'KI9O19xiqBUitt93GThsvYMs8UJ5fO6OcmKw+q5HQM8='}}}}
        """
        return std_ret(status=True,
                       data=self._wrapped_request().json())

    def block(self, height=None):
        """
        Get block at a given height
        :param height: If no height is provided, it will fetch the latest block

        Sample Return:
        {'status': True, 'result': {'jsonrpc': '2.0', 'id': '', 'result': {'block_meta': {'block_id':
        {'hash': '5701A12896315A121303A979ACB707ACC447E20EFACFCB26174E9ED3997E2F5C', \
        'parts': {'total': '1', 'hash': '8C63BE3E3A221B984219CFAA1C196DDF0F202D68293311BFA9EE0B7A9155EACD'}},
        'header': {'version': {'block': '10', 'app': '0'}, 'chain_id': 'Binance-Chain-Nile',
        'height': '10', 'time': '2019-03-07T01:57:22.135103158Z', 'num_txs': '0', 'total_txs': '0',
        'last_block_id': {'hash': '1AF674F804E277354E8742176ECA74E338F52C237E6DBFF92819D75037E4F651', 'parts':
        {'total': '1', 'hash': 'BB3C36D5BBDAB441A7339385C071C4E804C4C3DD5C7BC15D60BC658A6B261906'}},
        'last_commit_hash': '5442553C06521016756796015AF78FCAC752FFA9E94ACAF4DAA5DF4113B4B354', 'data_hash': '',
        'validators_hash': '80D9AB0FC10D18CA0E0832D5F4C063C5489EC1443DFB738252D038A82131B27A',
        'next_validators_hash': '80D9AB0FC10D18CA0E0832D5F4C063C5489EC1443DFB738252D038A82131B27A',
        'consensus_hash': '294D8FBD0B94B767A7EBA9840F299A3586DA7FE6B5DEAD3B7EECBA193C400F93',
        'app_hash': 'E7D96927FD82FD910624AA8034B8A527FCEB1F7AB353DE789A3ECA8D400BDE31',
        'last_results_hash': '', 'evidence_hash': '', 'proposer_address': 'E0DD72609CC106210D1AA13936CB67B93A0AEE21'}},
         ... ...
        {'type': 2, 'height': '9', 'round': '0', 'block_id':
         {'hash': '1AF674F804E277354E8742176ECA74E338F52C237E6DBFF92819D75037E4F651', 'parts': {'total': '1',
         'hash': 'BB3C36D5BBDAB441A7339385C071C4E804C4C3DD5C7BC15D60BC658A6B261906'}},
         'timestamp': '2019-03-07T01:57:22.129274247Z',
         'validator_address': 'FC3108DC3814888F4187452182BC1BAF83B71BC9', 'validator_index': '10',
         'signature': '55nxVx9iBFPTEuhuN806WyyBUwX1Hf4h24JSalcR6duQRxjFrLgm//eo7Bhh93jMikBTMA2ThQ+Mzc3A/wd8Dg=='}]}}}}}
        """

        para = '?height=%s' % height if height else ''
        return std_ret(status=True,
                       data=self._wrapped_request(para=para).json())

    def block_results(self, height=None):
        """
        BlockResults gets ABCIResults at a given height.
        Results are for the height of the block containing the txs. Thus response.results[5] is the results of executing getBlock(h).Txs[5

        :param height:  If no height is provided, it will fetch results for the latest block.

        Sample Return:
        {'status': True, 'result': {'jsonrpc': '2.0', 'id': '', 'result': {'height': '100', 'results':
        {'DeliverTx': None, 'EndBlock': {'validator_updates': None}, 'BeginBlock': {}}}}}
        """
        para = '?height=%s' % height if height else ''
        return std_ret(status=True,
                       data=self._wrapped_request(para=para).json())

    def broadcast_tx_async(self, tx_id):
        """
        Broadcase Transaction (Async), returns right away, with no response
        :param tx_id: Transaction id

        Sample Return:
        {'status': True, 'result': {'jsonrpc': '2.0', 'id': '', 'result': {'code': 0, 'data': '', 'log': '',
        'hash': 'A665A45920422F9D417E4867EFDC4FB8A04A1F3FFF1FA07E998E86F7F7A27AE3'}}}
        """
        para = '?tx="%s"' % tx_id
        return std_ret(status=True,
                       data=self._wrapped_request(para=para).json())

    def broadcast_tx_sync(self, tx_id):
        """
        Broadcase Transaction, teturns with the response from CheckTx.
        :param tx_id: Transaction id

        Sample Return:
        {'status': True, 'result': {'jsonrpc': '2.0', 'id': '', 'result': {'code': 65538, 'data': '',
        'log': '{"codespace":1,"code":2,"abci_code":65538,"message":"tx parse error"}',
        'hash': 'A665A45920422F9D417E4867EFDC4FB8A04A1F3FFF1FA07E998E86F7F7A27AE3'}}}\
        """
        para = '?tx="%s"' % tx_id
        return std_ret(status=True,
                       data=self._wrapped_request(para=para).json())

    def broadcast_tx_commit(self, tx_id):
        """
        CONTRACT: only returns error if mempool.CheckTx() errs or if we timeout waiting for tx to commit.
        If CheckTx or DeliverTx fail, no error will be returned, but the returned result will contain a non-OK ABCI code.
        :param tx_id: Transaction id

        Sample Return:
        {'status': True, 'result': {'jsonrpc': '2.0', 'id': '', 'result': {'check_tx': {'code': 65538,
        'log': '{"codespace":1,"code":2,"abci_code":65538,"message":"tx parse error"}'}, 'deliver_tx': {},
        'hash': 'A665A45920422F9D417E4867EFDC4FB8A04A1F3FFF1FA07E998E86F7F7A27AE3', 'height': '0'}}}
        """
        para = '?tx="%s"' % tx_id
        return std_ret(status=True,
                       data=self._wrapped_request(para=para).json())

    def get_commit(self, height=None):
        """
        Get block commit at a given height.

        :param height: If no height is provided, it will fetch the commit for the latest block.

        Sample Return:
        {'status': True, 'result': {'jsonrpc': '2.0', 'id': '', 'result': {'signed_header': {'header': {'version':
        {'block': '10', 'app': '0'}, 'chain_id': 'Binance-Chain-Nile', 'height': '10', 'time':
        '2019-03-07T01:57:22.135103158Z', 'num_txs': '0', 'total_txs': '0', 'last_block_id':
        {'hash': '1AF674F804E277354E8742176ECA74E338F52C237E6DBFF92819D75037E4F651', 'parts': {'total': '1',
        'hash': 'BB3C36D5BBDAB441A7339385C071C4E804C4C3DD5C7BC15D60BC658A6B261906'}},
        'last_commit_hash': '5442553C06521016756796015AF78FCAC752FFA9E94ACAF4DAA5DF4113B4B354', 'data_hash': '',
        'validators_hash': '80D9AB0FC10D18CA0E0832D5F4C063C5489EC1443DFB738252D038A82131B27A',
        'next_validators_hash': '80D9AB0FC10D18CA0E0832D5F4C063C5489EC1443DFB738252D038A82131B27A',
        'consensus_hash': '294D8FBD0B94B767A7EBA9840F299A3586DA7FE6B5DEAD3B7EECBA193C400F93',
        'app_hash': 'E7D96927FD82FD910624AA8034B8A527FCEB1F7AB353DE789A3ECA8D400BDE31', 'last_results_hash': '',
        'evidence_hash': '', 'proposer_address': 'E0DD72609CC106210D1AA13936CB67B93A0AEE21'}, 'commit':
        {'block_id': {'hash': '5701A12896315A121303A979ACB707ACC447E20EFACFCB26174E9ED3997E2F5C',
        'parts': {'total': '1', 'hash': '8C63BE3E3A221B984219CFAA1C196DDF0F202D68293311BFA9EE0B7A9155EACD'}},
        'precommits': [None, {'type': 2, 'height': '10', 'round': '1', 'block_id':
        {'hash': '5701A12896315A121303A979ACB707ACC447E20EFACFCB26174E9ED3997E2F5C', 'parts': {'total': '1',
        'hash': '8C63BE3E3A221B984219CFAA1C196DDF0F202D68293311BFA9EE0B7A9155EACD'}},
        'timestamp': '2019-03-07T01:57:27.663157746Z', 'validator_address': '18E69CC672973992BB5F76D049A5B2C5DDF77436',
        'validator_index': '1', 'signature': 'ZrnapmTAiJrhm0DVIoTzRbJG+FDCAxBpfamYxZj2eg0+wY0+KDg48sDPlD+chk97ti01PukuVs
        ftn4U6HXbkCA=='},
        ... ...
         'timestamp': '2019-03-07T01:57:27.738256001Z', 'validator_address': 'FC3108DC3814888F4187452182BC1BAF83B71BC9',
        'validator_index': '10', 'signature': 'Hw1BdfL79cLsTJhb406k+1MvU27zL1pdehLBHqkzF5NNOn/LrL4+u3t2ANwHaxX5OFijg
        ZW5P1T7ECVrvJr0CQ=='}]}}, 'canonical': True}}}\
        """
        para = '?height=%s' % height if height else ''
        return std_ret(status=True,
                       data=self._wrapped_request(para=para).json())

    def consensus_params(self, height=None):
        """
        Get the consensus parameters at the given block height.
        :param height:  If no height is provided, it will fetch the current consensus params

        Sample Return:
        {'status': True, 'result': {'jsonrpc': '2.0', 'id': '', 'result': {'block_height': '100', 'consensus_params':
        {'block_size': {'max_bytes': '1048576', 'max_gas': '-1'}, 'evidence': {'max_age': '100000'},
        'validator': {'pub_key_types': ['ed25519']}}}}}
        """

        para = '?height=%s' % height if height else ''
        return std_ret(status=True,
                       data=self._wrapped_request(para=para).json())

    def consensus_state(self):
        """
        ConsensusState returns a concise summary of the consensus state.
        Please note: when i am writting this SDK now, official site say this is UNSTABLE

        Sample Return:
        {'status': True, 'result': {'jsonrpc': '2.0', 'id': '', 'result': {'round_state':
        {'height/round/step': '7967291/0/4', 'start_time': '2019-04-13T05:30:11.319742433Z',
        'proposal_block_hash': 'E0488FF746BFD917C1F2A11C9AC15ACC50381275CF985D2356A8DBF85291F8A8',
        'locked_block_hash': '', 'valid_block_hash': '', 'height_vote_set': [{'round': '0',
        'prevotes': ['Vote{0:06FD60078EB4 7967291/00/1(Prevote)
        E0488FF746BF 0F15F05DAAE3 @ 2019-04-13T05:30:10.275300968Z}', 'Vote{1:18E69CC67297 7967291/00/1(Prevote)
        E0488FF746BF 33D396EF0423 @ 2019-04-13T05:30:10.327996565Z}', 'Vote{2:344C39BB8F45 7967291/00/1(Prevote)
        E0488FF746BF 7C71204358A5 @ 2019-04-13T05:30:10.323741771Z}', 'Vote{3:37EF19AF2967 7967291/00/1(Prevote)
        E0488FF746BF 7560AE249E1F @ 2019-04-13T05:30:10.290388253Z}', 'nil-Vote', 'nil-Vote', 'Vote{6:91844D296BD8
        ... ...
        E0488FF746BF 15C6E26CCBB9 @ 2019-04-13T05:30:10.290430937Z}', 'nil-Vote', 'nil-Vote'], 'prevotes_bit_array':
        'BA{11:xxxx__xxx__} 700000000000/1100000000000 = 0.64', 'precommits': ['nil-Vote', 'nil-Vote', 'nil-Vote',
        'nil-Vote', 'nil-Vote', 'nil-Vote', 'nil-Vote', 'nil-Vote', 'nil-Vote', 'nil-Vote', 'nil-Vote'],
        'precommits_bit_array': 'BA{11:___________} 0/1100000000000 = 0.00'}, {'round': '1',
        'prevotes': ['nil-Vote', 'nil-Vote', 'nil-Vote', 'nil-Vote', 'nil-Vote', 'nil-Vote', 'nil-Vote', 'nil-Vote',
        'nil-Vote', 'nil-Vote', 'nil-Vote'], 'prevotes_bit_array': 'BA{11:___________} 0/1100000000000 = 0.00',
        'precommits': ['nil-Vote', 'nil-Vote', 'nil-Vote', 'nil-Vote', 'nil-Vote', 'nil-Vote', 'nil-Vote', 'nil-Vote',
        'nil-Vote', 'nil-Vote', 'nil-Vote'], 'precommits_bit_array': 'BA{11:___________} 0/1100000000000 = 0.00'}]}}}}
        """
        return std_ret(status=True,
                       data=self._wrapped_request().json())

    def genesis(self):
        """
        Get genesis file.
        Sample Return:
        {'status': True, 'result': {'jsonrpc': '2.0', 'id': '', 'result': {'genesis': {'genesis_time':
        '2019-03-07T01:52:07.500913003Z', 'chain_id': 'Binance-Chain-Nile', 'consensus_params': {'block_size':
        {'max_bytes': '1048576', 'max_gas': '-1'}, 'evidence': {'max_age': '100000'}, 'validator':
        {'pub_key_types': ['ed25519']}}, 'app_hash': '', 'app_state': {'tokens': [{'name': 'Binance Chain Native Token',
        'symbol': 'BNB', 'total_supply': '20000000000000000', 'owner': 'tbnb12hlquylu78cjylk5zshxpdj6hf3t0tahwjt3ex',
        'mintable': False}], 'accounts': [{'name': 'Fuji', 'address': 'tbnb12hlquylu78cjylk5zshxpdj6hf3t0tahwjt3ex',
        'valaddr': '7B343E041CA130000A8BC00C35152BD7E7740037'},
        ... ...
        {'type': 'auth/StdTx', 'value': {'msg': [{'type': 'cosmos-sdk/MsgCreateValidatorProposal',
        'value': {'MsgCreateValidator': {'Description': {'moniker': 'Zugspitze', 'identity': '', 'website': '',
        'details': ''}, 'Commission': {'rate': '0', 'max_rate': '0', 'max_change_rate': '0'},
        'delegator_address': 'tbnb108drn8exhv72tp40e6lq9z949nnjj54yzqrr2f', 'validator_address':
        'bva108drn8exhv72tp40e6lq9z949nnjj54yvfth5u', 'pubkey': {'type': 'tendermint/PubKeyEd25519',
        'value': 'yA6avvf/Q5wQxo/o8TA97d/FJ3GMOzfYumgHRG48gno='}, 'delegation': {'denom': 'BNB',
        'amount': '100000000000'}}, 'proposal_id': '0'}}], 'signatures': [{'pub_key': {'type':
        'tendermint/PubKeySecp256k1', 'value': 'A28N2eZXepmh+2enXvdAPqbbPf9yFCqYZleFjUMRJe0g'}, 'signature':
        'egp4GjM/8PEVeFJiopen35eZzy/5NKjGKmK3MGpfmAFGQvjN6G4HyGX+6eigOuw40qpMdT9HYmvzSoa+jgXURQ==', 'account_number':
        '0', 'sequence': '0'}], 'memo': 'c4d94f29e765ecfe81c940e11c2e997321aa8e0f@172.18.10.213:26656', 'source': '0',
        'data': None}}, {'type': 'auth/StdTx', 'value': {'msg': [{'type': 'cosmos-sdk/MsgCreateValidatorProposal',
        'value': {'MsgCreateValidator': {'Description': {'moniker': 'Gahinga', 'identity': '', 'website': '',
        'details': ''}, 'Commission': {'rate': '0', 'max_rate': '0', 'max_change_rate': '0'}, 'delegator_address':
        'tbnb1vehecekrsks5sshcwvxyeyrd469j9wvcqm37yu', 'validator_address': 'bva1vehecekrsks5sshcwvxyeyrd469j9wvcwj26f',
        'pubkey': {'type': 'tendermint/PubKeyEd25519', 'value': 'kUKvzGkbfMBdJsewvgyLRkGClBcXMOB584T94vpQuvw='},
        'delegation': {'denom': 'BNB', 'amount': '100000000000'}}, 'proposal_id': '0'}}], 'signatures': [{'pub_key':
         {'type': 'tendermint/PubKeySecp256k1', 'value': 'AsS8HffgT0IIai/sesaWtW5wurpu7eBDkhu0esmwjsnc'},
         'signature': 'k6LegehVpGnjQ4ePBwJajrbKlPg5tXQMkBtIZ+nbMNAHp4Z2IihYrUGMAoKu0B0LJbbNH/7Gq7b0AK5HfYEByg==',
         'account_number': '0', 'sequence': '0'}], 'memo': '4119f9f689f62734bcf3757f916639bc480bb8ce@172.18.10.214:256',
          'source': '0', 'data': None}}]}}}}}
        """
        return std_ret(status=True,
                       data=self._wrapped_request().json())

    def _wrapped_request(self, para=None):

        # Get caller function name
        caller_func_name = inspect.stack()[1].function
        # todo:
        # refer to: https://stackoverflow.com/questions/900392/getting-the-caller-function-name-inside-another-function-in-python/900413
        # seems caller_func_name is different from python 3 and python 2, need to test on python 2

        # Get ws name from Mapper
        node_rpc_entry_point = NODE_RPC_ENTRY_POINT_MAPPING[caller_func_name]

        # Perform Request
        request_url = self.node_url + node_rpc_entry_point
        if para:
            request_url += para
        print('Request URL: %s' % request_url)
        try:
            req_ret = requests.get(request_url)
            return req_ret
        except Exception as err:
            return std_ret(status=False,
                           data='%s' % err)
