# Binance DEX API implemented based on: https://testnet-dex.binance.org/doc/api-reference/dex-api/paths.html
import requests
import datetime
from binance_dex.lib.common import binance_api_request, std_ret

IS_TEST_NET = False

API_BASE_URL_TEST_NET = 'https://testnet-dex.binance.org/'
API_BASE_URL_MAIN_NET = 'https://dex.binance.org/'


class BinanceChainClient(object):
    """
    API Client for Binance DEX
    Official Document: https://binance-chain.github.io/api-reference/dex-api/paths.html
    """

    def __init__(self, is_test_net=IS_TEST_NET, api_base_url_with_port=None):
        """
        API Client
        :param api_base_url_with_port:
        """

        # "api_base_url_with_port" parameter has higher priority
        if api_base_url_with_port:
            self.api_base_url_with_port = api_base_url_with_port \
                if api_base_url_with_port[-1] == '/' else api_base_url_with_port + '/'
        else:
            self.api_base_url_with_port = API_BASE_URL_TEST_NET if is_test_net else API_BASE_URL_MAIN_NET

    def get_block_time(self):
        """
         - Summary: Get the block time.
         - Description: Gets the latest block time and the current time according to the HTTP service.
         - Destination: Validator node.
         - Rate Limit: 1 request per IP per second.
         - Return:
            Success sample results:
            {'ap_time': '2019-03-06T04:23:45Z', 'block_time': '2019-03-06T04:23:44Z'}
        """
        url = '%sapi/v1/time' % (self.api_base_url_with_port)
        ret = binance_api_request(url=url,
                                  method='GET')
        return ret

    def get_node_info(self):
        """
         - Summary: Get node information.
         - Description: Gets runtime information about the node.
         - Destination: Validator node.
         - Rate Limit: 1 request per IP per second.
         - Return:
            Sample success result:
            {'status': True, 'result': {'node_info': {'id': 'dd2adba52ad9c830fe16a53fe81dac6880a91218',
            'listen_addr': '10.203.42.14:27146', 'network': 'Binance-Chain-Nile', 'version': '0.30.1',
            'channels': '3540202122233038', 'moniker': 'Aconcagua',
            'other': {'amino_version': '', 'p2p_version': '', 'consensus_version': '', 'rpc_version': '',
            'tx_index': 'on', 'rpc_address': 'tcp://0.0.0.0:27147'}}, 'sync_info': {
            'latest_block_hash': '7CBCCF0980B6A9D7B988199FEAF7E01FB02668ED192397198013194D8F311EC2',
            'latest_app_hash': '193A0D5399A6FF77F0DB5543C6FAC367451DF42C506C9B63DF200F3DEC78D89D',
            'latest_block_height': 8275, 'latest_block_time': '2019-03-07T02:49:52.843793234Z', 'catching_up': False},
            'validator_info': {'address': '344C39BB8F4512D6CAB1F6AAFAC1811EF9D8AFDF', 'pub_key': [
            77, 66, 10, 234, 132, 62, 146, 160, 207, 230, 157, 137, 105, 109, 255, 104, 39, 118, 159, 156, 181, 42, 36,
            154, 245, 55, 206, 137, 191, 42, 75, 116], 'voting_power': 100000000000}}}
        """
        url = '%sapi/v1/node-info' % (self.api_base_url_with_port)
        ret = binance_api_request(url=url,
                                  method='GET')
        return ret

    def get_validators(self):
        """
         - Summary: Get validators.
         - Description: Gets the list of validators used in consensus.
         - Destination: Witness node.
         - Rate Limit: 10 requests per IP per second.
         - Return:
            Sample success result:
            {'status': True, 'result': {'block_height': 6935724,
            'validators': [{'address': '06FD60078EB4C2356137DD50036597DB267CF616',
            'pub_key': [22, 36, 222, 100, 32, 225, 124, 190, 156, 32, 205, 207, 223, 135, 107, 59, 18,
            151, 141, 50, 100, 160, 7, 252, 170, 167, 28, 76, 219, 112, 29, 158, 188, 3, 35, 244, 79],
            'voting_power': 100000000000}, {'address': '18E69CC672973992BB5F76D049A5B2C5DDF77436',
            'pub_key': [22, 36, 222, 100, 32, 24, 78, 123, 16, 61, 52, 196, 16, 3, 249, 184, 100, 213,
            248, 193, 173, 218, 155, 208, 67, 107, 37, 59, 179, 200, 68, 188, 115, 156, 30, 119, 201],
            'voting_power': 100000000000}, {'address': '344C39BB8F4512D6CAB1F6AAFAC1811EF9D8AFDF',
            'pub_key': [22, 36, 222, 100, 32, 77, 66, 10, 234, 132, 62, 146, 160, 207, 230, 157, 137,
            105, 109, 255, 104, 39, 118, 159, 156, 181, 42, 36, 154, 245, 55, 206, 137, 191, 42, 75, 116],
            'voting_power': 100000000000}, {'address': '37EF19AF29679B368D2B9E9DE3F8769B35786676',
            'pub_key': [22, 36, 222, 100, 32, 189, 3, 222, 159, 138, 178, 158, 40, 0, 9, 78, 21, 63,
            172, 111, 105, 108, 250, 81, 37, 54, 201, 194, 248, 4, 220, 178, 194, 196, 228, 174, 214],
            'voting_power': 100000000000}, {'address': '62633D9DB7ED78E951F79913FDC8231AA77EC12B',
            'pub_key': [22, 36, 222, 100, 32, 143, 74, 116, 160, 115, 81, 137, 93, 223, 55, 48, 87,
            185, 143, 174, 109, 250, 242, 205, 33, 243, 122, 6, 62, 25, 96, 16, 120, 254, 71, 13, 83],
            'voting_power': 100000000000}, {'address': '7B343E041CA130000A8BC00C35152BD7E7740037',
            'pub_key': [22, 36, 222, 100, 32, 74, 93, 71, 83, 235, 121, 249, 46, 128, 239, 226, 45, 247,
            172, 164, 246, 102, 164, 244, 75, 248, 28, 83, 108, 74, 9, 212, 185, 197, 182, 84, 181],
            'voting_power': 100000000000}, {'address': '91844D296BD8E591448EFC65FD6AD51A888D58FA',
            'pub_key': [22, 36, 222, 100, 32, 200, 14, 154, 190, 247, 255, 67, 156, 16, 198, 143, 232,
            241, 48, 61, 237, 223, 197, 39, 113, 140, 59, 55, 216, 186, 104, 7, 68, 110, 60, 130, 122],
            'voting_power': 100000000000}, {'address': 'B3727172CE6473BC780298A2D66C12F1A14F5B2A',
            'pub_key': [22, 36, 222, 100, 32, 145, 66, 175, 204, 105, 27, 124, 192, 93, 38, 199, 176,
            190, 12, 139, 70, 65, 130, 148, 23, 23, 48, 224, 121, 243, 132, 253, 226, 250, 80, 186, 252],
            'voting_power': 100000000000}, {'address': 'B6F20C7FAA2B2F6F24518FA02B71CB5F4A09FBA3',
            'pub_key': [22, 36, 222, 100, 32, 73, 178, 136, 228, 235, 187, 58, 40, 28, 45, 84, 111, 195,
            2, 83, 213, 186, 240, 137, 147, 182, 229, 210, 149, 251, 120, 122, 91, 49, 74, 41, 142],
            'voting_power': 100000000000}, {'address': 'E0DD72609CC106210D1AA13936CB67B93A0AEE21',
            'pub_key': [22, 36, 222, 100, 32, 4, 34, 67, 57, 104, 143, 1, 46, 100, 157, 228, 142, 36, 24,
            128, 9, 46, 170, 143, 106, 160, 244, 241, 75, 252, 249, 224, 199, 105, 23, 192, 182],
            'voting_power': 100000000000}, {'address': 'FC3108DC3814888F4187452182BC1BAF83B71BC9',
            'pub_key': [22, 36, 222, 100, 32, 64, 52, 179, 124, 237, 168, 160, 191, 19, 177, 171, 174,
            238, 122, 143, 147, 131, 84, 32, 153, 165, 84, 210, 25, 185, 61, 12, 230, 158, 57, 112, 232],
            'voting_power': 100000000000}]}}
        """
        url = '%sapi/v1/validators' % (self.api_base_url_with_port)
        ret = binance_api_request(url=url,
                                  method='GET')
        return ret

    def get_peers(self):
        """
         - Summary: Get network peers.
         - Description: Gets the list of network peers.
         - Destination: Witness node.
         - Rate Limit: 1 requests per IP per second.
         - Return:
            Sample success result:
            {'status': True, 'result': [
                {'accelerated': True, 
            'access_addr': 'https://testnet-dex.binance.org:443', 
            'capabilities': ['qs', 'ap', 'ws'], 'id': 'gateway-ingress', 
            'listen_addr': 'https://testnet-dex.binance.org:443', 
            'moniker': 'gateway-ingress', 'network': 'gateway', 
            'stream_addr': 'wss://testnet-dex.binance.org', 'version': '1.0.0'}, 
            {'access_addr': 'http://seed-pre-s1.binance.org:80', 
            'capabilities': ['node'], 'id': 'aea74b16d28d06cbfbb1179c177e8cd71315cce4', 
            'listen_addr': 'http://seed-pre-s1.binance.org:80', 
            'moniker': 'seed', 'network': 'Binance-Chain-Nile', 
            'original_listen_addr': 'ac6d84c3f243a11e98ced0ac108d49f7-704ea117aa391bbe.elb.ap-northeast-1.amazonaws.com:27146', 
            'version': '0.30.1'}, 
            {'access_addr': 'https://data-seed-pre-0-s1.binance.org:443', 
            'capabilities': ['node'], 'id': '9612b570bffebecca4776cb4512d08e252119005', 
            'listen_addr': 'https://data-seed-pre-0-s1.binance.org:443', 'moniker': 'data-seed-0', 
            'network': 'Binance-Chain-Nile', 
            'original_listen_addr': 'a0b88b324243a11e994280efee3352a7-96b6996626c6481d.elb.ap-northeast-1.amazonaws.com:27146', 
            'version': '0.30.1'}, 
            {'access_addr': 'https://data-seed-pre-1-s1.binance.org:443', 
            'capabilities': ['node'], 'id': '8c379d4d3b9995c712665dc9a9414dbde5b30483', 
            'listen_addr': 'https://data-seed-pre-1-s1.binance.org:443', 
            'moniker': 'data-seed-1', 'network': 'Binance-Chain-Nile', 
            'original_listen_addr': 'aa1e4d0d1243a11e9a951063f6065739-7a82be90a58744b6.elb.ap-northeast-1.amazonaws.com:27146', 
            'version': '0.30.1'}, 
            {'access_addr': 'https://data-seed-pre-2-s1.binance.org:443', 'capabilities': ['node'], 
            'id': '7156d461742e2a1e569fd68426009c4194830c93', 
            'listen_addr': 'https://data-seed-pre-2-s1.binance.org:443', 
            'moniker': 'data-seed-2', 'network': 'Binance-Chain-Nile', 
            'original_listen_addr': 'aa841c226243a11e9a951063f6065739-eee556e439dc6a3b.elb.ap-northeast-1.amazonaws.com:27146', 
            'version': '0.30.1'}]}
        """
        url = '%sapi/v1/peers' % (self.api_base_url_with_port)
        ret = binance_api_request(url=url,
                                  method='GET')
        return ret

    def get_tokens(self):
        """
         - Summary: Get tokens list.
         - Description: Gets a list of tokens that have been issued.
         - Destination: Witness node.
         - Rate Limit: 1 request per IP per second.
        :return:
         {'status': True, 'result': [{'name': 'ANN Network', 'symbol': 'ANN-457', 'original_symbol': 'ANN',
         'total_supply': '100000000.00000000', 'owner': 'tbnb14zguq8gf58ms07npae7pluqxm27xvvgftmhsxz', 'mintable': True},
         {'name': 'Zilliqa', 'symbol': 'ZIL-C5D', 'original_symbol': 'ZIL', 'total_supply': '1000000000.00000000',
         'owner': 'tbnb1hzm72ffar7f57jtx9k70jukqydchvwck469ya4', 'mintable': True}]}
        """

        url = '%sapi/v1/tokens' % (self.api_base_url_with_port)
        ret = binance_api_request(url=url,
                                  method='GET')
        return ret

    def get_account_info_by_address(self, address):
        """
         - Summary: Get an account.
         - Description: Gets account metadata for an address.
         - Destination: Witness node.
         - Rate Limit: 5 requests per IP per second.

        :param address: <Public address>
        :return:
        {'status': True, 'result': {'address': 'tbnb1fn9z9vn4f44ekz0a3pf80dcy2wh4d5988phjds', 'public_key': None,
        'account_number': 666547, 'sequence': 0, 'balances': [{'symbol': 'BNB', 'free': '1399.99250000',
        'locked': '0.00000000', 'frozen': '0.00000000'}]}}
        """
        url = '%sapi/v1/account/%s' % (self.api_base_url_with_port, address)
        ret = binance_api_request(url=url,
                                  method='GET')
        return ret

    def get_account_sequence_by_address(self, address):
        """
         - Summary: Get an account sequence.
         - Description: Gets an account sequence for an address.
         - Destination: Validator node.
         - Rate Limit: 5 requests per IP per second.

        :param address: <Public address>
        :return:
        {'status': True, 'result': {'sequence': 17}}
        """
        url = '%sapi/v1/account/%s/sequence' % (self.api_base_url_with_port, address)
        ret = binance_api_request(url=url,
                                  method='GET')
        return ret

    def get_transaction(self, tx_hash):
        """
         - Summary: Get a transaction.
         - Description: Gets transaction metadata by transaction ID. By default, transactions are returned in a raw format. You may add ?format=json to the end of the path to obtain a more readable response.
         - Destination: Seed node.
         - Rate Limit: 10 requests per IP per second.
        :param tx_hash: <Transaction Hash>
        :return:
        {'status': True, 'result': {'hash': '35B8D4070200FFBE045432AC9D87232BEC1FFAD9E6A6C8979CE2FE631B644B9E',
        'height': '4112785', 'tx': {'type': 'auth/StdTx', 'value': {'data': None, 'memo': 'hello', 'msg': [
        {'type': 'cosmos-sdk/Send', 'value': {'inputs': [{'address': 'tbnb1aeptz56sjep4j2uxt03rcqcp03s9mjgcyex9le',
        'coins': [{'amount': '19999875000', 'denom': 'BNB'}]}], 'outputs': [{'address':
        'tbnb1fn9z9vn4f44ekz0a3pf80dcy2wh4d5988phjds', 'coins': [{'amount': '19999875000', 'denom': 'BNB'}]}]}}],
        'signatures': [{'account_number': '666557', 'pub_key': {'type': 'tendermint/PubKeySecp256k1', 'value':
        'AkrIfMumvYIRaNizdcDjnohIwkNyHjl8K7WNbXXL3W16'}, 'sequence': '0',
        'signature': '3iijgGYTIROtPHAXKrPiHGgbyhv3ZsW23FOcorvKO7kEoDl6lWaxQk1zMGwdTjBpgU6CCkYRhIj4AnbzozW1xQ=='}],
        'source': '1'}}}}
        """
        url = '%sapi/v1/tx/%s?format=json' % (self.api_base_url_with_port, tx_hash)
        ret = binance_api_request(url=url,
                                  method='GET')
        return ret

    def get_markets(self):
        """
         - Summary: Get market pairs.
         - Description: Gets the list of market pairs that have been listed.
         - Destination: Witness node.
         - Rate Limit: 1 request per IP per second.
        :return:
        {'status': True, 'result': [
        {'base_asset_symbol': '000-0E1', 'quote_asset_symbol': 'BNB', 'price': '1.00000000', 'tick_size': '0.00100000',
        'lot_size': '0.00001000'},
        {'base_asset_symbol': '100K-9BC', 'quote_asset_symbol': 'BTC.B-918', 'price': '1.00000000',
        'tick_size': '0.00000001', 'lot_size': '1.00000000'},
        {'base_asset_symbol': '100K-9BC', 'quote_asset_symbol': 'USDT.B-B7C', 'price': '1.00000000',
        'tick_size': '0.00000100', 'lot_size': '0.01000000'},
         ... ...]}
        """
        url = '%sapi/v1/markets' % (self.api_base_url_with_port)
        ret = binance_api_request(url=url,
                                  method='GET')
        return ret

    def get_fees(self):
        url = '%sapi/v1/fees' % (self.api_base_url_with_port)
        ret = binance_api_request(url=url,
                                  method='GET')
        return ret

    def get_depth(self, symbol, limit=None):
        """
         - Summary: Get the order book.
         - Description: Gets the order book depth data for a given pair symbol.
         - The given limit must be one of the allowed limits below.
         - Destination: Validator node.
         - Rate Limit: 10 requests per IP per second.

        :param symbol: Market pair symbol, e.g. NNB-0AD_BNB
        :param limit:
        limited to: [5, 10, 20, 50, 100, 500, 1000]

        :return:
        {'status': True, 'result': {'asks': [], 'bids': [], 'height': 8034721}}
        """
        # inputs Validation
        if limit and limit not in api_types_instance.allowed_depth_limit:
            return std_ret(False, 'Limit must be in: %s' % api_types_instance.allowed_depth_limit)

        url = '%sapi/v1/depth?symbol=%s' % (self.api_base_url_with_port, symbol)
        url = url + '&limit=%s' % limit if limit else url
        ret = binance_api_request(url=url,
                                  method='GET')
        return ret

    def get_klines(self, trading_pair, interval='4h', start_time=None, end_time=None, limit=300):
        """
         - Summary: Get candlestick bars.
         - Description: Gets candlestick/kline bars for a symbol. Bars are uniquely identified by their open time.
         - If the time window is larger than limits, only the first n klines will return. In this case, please either shrink the window or increase the limit to get proper amount of klines.
         - Rate Limit: 10 requests per IP per second.

        :param trading_pair: <Trading Pair> example: 'BEY-8C6_BNB'
        :param interval:
        limited to: ['1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M']
        :param start_time: start time in Milliseconds
        :param end_time: end time in Milliseconds
        :param limit: default 300; max 1000.

        :return:
        {'status': True, 'result': [
        {'open_time_stamp': 1552161600000, 'open_time_datetime': datetime.datetime(2019, 3, 9, 20, 0),
        'price_open': '1.00000000', 'price_high': '14.90000000', 'price_low': '0.00001000',
        'price_close': '6.10000000', 'volume': '3.13200000', 'close_time_stamp': 1552175999999,
        'close_time_datetime': datetime.datetime(2019, 3, 9, 23, 59, 59), 'quote_asset_volume': '2.22192000',
        'num_trades': 135},
        ... ...]}
        """
        # inputs Validation
        if interval not in api_types_instance.allowed_kline_interval:
            return std_ret(False, 'Interval but be in: %s' % api_types_instance.allowed_kline_interval)
        url = '%sapi/v1/klines?interval=%s&limit=%s&symbol=%s' % (self.api_base_url_with_port,
                                                                  interval,
                                                                  limit,
                                                                  trading_pair)
        url = url + '&startTime=%s' % start_time if start_time else url
        url = url + '&endTime=%s' % end_time if end_time else url
        res = requests.get(url)
        status_code = res.status_code
        if status_code == 200:
            ret = res.json()
            ret = [{'open_time_stamp': elem[0],
                    'open_time_datetime': datetime.datetime.utcfromtimestamp(int(str(elem[0])[:-3])),
                    'price_open': elem[1],
                    'price_high': elem[2],
                    'price_low': elem[3],
                    'price_close': elem[4],
                    'volume': elem[5],
                    'close_time_stamp': elem[6],
                    'close_time_datetime': datetime.datetime.utcfromtimestamp(int(str(elem[6])[:-3])),
                    'quote_asset_volume': elem[7],
                    'num_trades': elem[8]
                    } for elem in ret]
            return std_ret(True, ret)
        else:
            return std_ret(False, 'Server Error, status_code=%s' % status_code)

    def get_order_by_id(self, order_id):
        """
         - Summary: Get an order.
         - Description: Gets metadata for an individual order by its ID.
         - Rate Limit: 5 requests per IP per second.

        :return:
        """
        url = '%sapi/v1/orders/%s' % (self.api_base_url_with_port, order_id)
        ret = binance_api_request(url=url,
                                  method='GET')
        return ret

    def get_order_open(self, address, symbol=None, limit=500, offset=0, total=0):
        """
         - Summary: Get open orders.
         - Description: Gets open orders for a given address.
         - Rate Limit: 5 requests per IP per second.

        :return:
        """
        url = '%sapi/v1/orders/open?address=%s&limit=%s&offset=%s&total=%s' % \
              (self.api_base_url_with_port, address, limit, offset, total)
        url = url + '&symbol=%s' % symbol if symbol else url
        ret = binance_api_request(url=url,
                                  method='GET')
        return ret

    def get_order_closed(self, address, end=None, side=None, start=None,
                         status=None, symbol=None, limit=500, offset=0, total=0):
        """
         - Summary: Get closed orders.
         - Description: Gets closed (filled and cancelled) orders for a given address.
         - Query Window: Default query window is latest 7 days; The maximum start - end query window is 3 months.
         - Rate Limit: 5 requests per IP per second.

        :return:
        """

        if status and status not in api_types_instance.allowed_order_status:
            return std_ret(False, 'Status should be in: %s' % api_types_instance.allowed_order_status)

        url = '%sapi/v1/orders/closed?address=%s&limit=%s&offset=%s&total=%s' % \
              (self.api_base_url_with_port, address, limit, offset, total)
        url = url + '&symbol=%s' % symbol if symbol else url
        url = url + '&start=%s' % start if start else url
        url = url + '&end=%s' % end if end else url
        url = url + '&side=%s' % side if side else url
        url = url + '&status=%s' % status if status else url
        ret = binance_api_request(url=url,
                                  method='GET')
        return ret

    def post_broadcast(self, transaction, sync=None):
        """
         - Summary: Get closed orders.
         - Description: Gets closed (filled and cancelled) orders for a given address.
         - Query Window: Default query window is latest 7 days; The maximum start - end query window is 3 months.
         - Rate Limit: 5 requests per IP per second.

        :return:
        """
        url = '%sapi/v1/broadcast' % (self.api_base_url_with_port)
        url = url + '?sync=%s' % sync if sync else url
        ret = binance_api_request(url=url,
                                  method='POST', body=transaction)
        return ret

    def transactions(self, address, block_height=None, start_time=None, end_time=None, limit=None, offset=None,
                     side=None, tx_asset=None, tx_type=None):
        """
        Gets a list of transactions
        :param address: Required parameter, to indicate address
        :param non-mandatory parameters, can pass in:
         - block_height: block height, <long type>
         - start_time: start time, The maximum query window is 3 months, <date time type>
         - end_time: end time, The maximum query window is 3 months, <date time type>
         - limit: limits <int type>
         - offset: offset <int type>
         - side: transaction side. Allowed value: [RECEIVE, SEND], <string type>
         - tx_asset: txAsset, <string type>
         - tx_type: transaction type. Allowed value: [ NEW_ORDER,ISSUE_TOKEN,BURN_TOKEN,LIST_TOKEN,CANCEL_ORDER,
         FREEZE_TOKEN,UN_FREEZE_TOKEN,TRANSFER,PROPOSAL,VOTE,MINT,DEPOSIT], <string type>
        :return:
        """
        url = '%sapi/v1/transactions/?address=%s' % (self.api_base_url_with_port, address)

        # compose url
        if block_height:
            url += '&blockHeight=' + str(block_height)
        if start_time:
            url += '&startTime=' + str(int(start_time.timestamp())) + '000'
        if end_time:
            url += '&endTime=' + str(int(end_time.timestamp())) + '000'
        if limit:
            url += '&limit=' + str(limit)
        if offset:
            url += '&offset=' + str(offset)
        if side:
            # input data validation
            if side not in Types().allowed_transactions_side:
                raise Exception('side only allow: %s' % Types().allowed_transactions_side)
            url += '&side=' + str(side)
        if tx_asset:
            url += '&txAsset=' + str(tx_asset)
        if tx_type:
            # input data validation
            if tx_type not in Types().allowed_transactions_type:
                raise Exception('type only allow: %s' % Types().allowed_transactions_type)
            url += '&txType' + str(tx_type)
        # perform query
        ret = binance_api_request(url=url,
                                  method='GET')
        return ret


class Types(object):
    """
    In case of mis-spell or other wrong strings, let's pre-define some strings here to consume
    """

    def __init__(self):
        self.allowed_transactions_side = [self.Transactions.side_receive,
                                          self.Transactions.side_send]
        self.allowed_transactions_type = [self.Transactions.type_new_order,
                                          self.Transactions.type_issue_token,
                                          self.Transactions.type_burn_token,
                                          self.Transactions.type_list_token,
                                          self.Transactions.type_cancel_order,
                                          self.Transactions.type_freeze_token,
                                          self.Transactions.type_un_freeze_token,
                                          self.Transactions.type_transfer,
                                          self.Transactions.type_proposal,
                                          self.Transactions.type_vote]

        self.allowed_kline_interval = ['1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h',
                                       '1d', '3d', '1w', '1M']

        self.allowed_depth_limit = [5, 10, 20, 50, 100, 500, 1000]

        self.allowed_order_status = ['Ack', 'PartialFill', 'IocNoFill', 'FullyFill', 'Canceled', 'Expired',
                                     'FailedBlocking', 'FailedMatching']

    class Transactions(object):
        side_receive = 'RECEIVE'
        side_send = 'SEND'

        type_new_order = 'NEW_ORDER'
        type_issue_token = 'ISSUE_TOKEN'
        type_burn_token = 'BURN_TOKEN'
        type_list_token = 'LIST_TOKEN'
        type_cancel_order = 'CANCEL_ORDER'
        type_freeze_token = 'FREEZE_TOKEN'
        type_un_freeze_token = 'UN_FREEZE_TOKEN'
        type_transfer = 'TRANSFER'
        type_proposal = 'PROPOSAL'
        type_vote = 'VOTE'

    class TxType(object):
        msg_send = 'MsgSend'
        new_order_msg = 'NewOrderMsg'
        cancel_order_msg = 'CancelOrderMsg'
        std_tx = 'StdTx'
        pubkey_secp_256k1 = 'PubKeySecp256k1'
        signature_secp_256k1 = 'SignatureSecp256k1'

    class KLine(object):
        # KLine intervals
        interval_1min = '1m'
        interval_3min = '3m'
        interval_5min = '4m'
        interval_15min = '15m'
        interval_30min = '30m'
        interval_1hour = '1h'
        interval_2hour = '2h'
        interval_4hour = '4h'
        interval_6hour = '6h'
        interval_8hour = '8h'
        interval_12hour = '12h'
        interval_1day = '1d'
        interval_3day = '3d'
        interval_1week = '1w'
        interval_1month = '1M'


# Singleton for Types
api_types_instance = Types()
