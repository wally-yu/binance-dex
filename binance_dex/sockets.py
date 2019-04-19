"""
Wrapper for Binance Sockets, details can be found from:
https://binance-chain.github.io/api-reference/dex-api/ws-streams.html
"""
import inspect
from binance_dex.lib.sockets import BinanceChainSocketConn


IS_TEST_NET = False  # A varialbe to switch test net / main net, default would be MAIN-NET
SOCKET_BASE_ADDR_TEST_NET = 'wss://testnet-dex.binance.org/api/ws/'
SOCKET_BASE_ADDR_MAIN_NET = 'wss://dex.binance.org/api/ws/'


# Default Call back sample function to alert user to create own customized function
def _default_call_back(*args):
    print('Here is default callback function, '
          'please pass in your own customized callback function to handle received data')
    print(args[1])


WS_ENTRY_POINTS = {
    'fetch_block_height_updates': '$all@blockheight',
    'fetch_account_updates': '',
    'fetch_trades_updates': '',
    'fetch_market_diff_stream': '',
    'fetch_market_depth_stream': '',
    'fetch_kline_updates': '',
    'fetch_ticker_streams': '',
}


class BinanceChainSocket(object):
    """
    Web Socket Implementation
    Official Document: https://binance-chain.github.io/api-reference/dex-api/ws-connection.html
    """
    def __init__(self, is_test_net=IS_TEST_NET):
        self.base_ws_url = SOCKET_BASE_ADDR_TEST_NET if is_test_net else SOCKET_BASE_ADDR_MAIN_NET

    def fetch_account_updates(self, user_address, one_off=True, callback_function=None):
        """
        This function may receive serveral kinds of data, distinguished by "stream" from returned data

        :param user_address: Address

        Sample Return:
         - Account sample return (notice "stream" == "accounts"):
         {"stream":"accounts","data":{"e":"outboundAccountInfo","E":7364509,"B":[{"a":"BNB","f":"1371.08750000",
         "r":"0.00000000","l":"0.00000000"},{"a":"DEX.B-C72","f":"999999791.11200000","r":"0.00000000",
         "l":"0.00000000"}]}}

         - Transfer sample return (notice "stream" == "transfers"):
         {"stream":"transfers","data":{"e":"outboundTransferInfo","E":7364509,
         "H":"08B71F862CDB820AF499D6E4FB34494CA163EBDADD5DC5D0A61EB1A0725BB4F4",
         "f":"tbnb1r4gc5ftrkr9ez2khph4h5xxd0mf0hd75jf06gw","t":[{"o":"tbnb1fn9z9vn4f44ekz0a3pf80dcy2wh4d5988phjds",
         "c":[{"a":"DEX.B-C72","A":"8.88800000"}]}]}}

         - Orders
         {"stream":"orders","data":[{"e":"executionReport","E":7366949,"s":"100K-9BC_BNB","S":1,"o":2,"f":1,
         "q":"0.00001500","p":"66666.00000000","x":"NEW","X":"Ack","i":"1D518A2563B0CB912AD70DEB7A18CD7ED2FBB7D4-10",
         "l":"0.00000000","L":"0.00000000","z":"0.00001500","n":"","T":1554890366040313451,"t":"",
         "O":1554890366040313451},{"e":"executionReport","E":7366949,"s":"100K-9BC_BNB","S":1,"o":2,"f":1,
         "q":"0.00001500","p":"66666.00000000","x":"NEW","X":"FullyFill",
         "i":"1D518A2563B0CB912AD70DEB7A18CD7ED2FBB7D4-10","l":"0.00001500","L":"66666.00000000","z":"0.00001500",
         "n":"BNB:0.00039999","T":1554890366040313451,"t":"7366949-0","O":1554890366040313451}]}

        """
        return self._standard_binance_change_socket_handler(one_off=one_off,
                                                            callback_function=callback_function,
                                                            parameter=user_address)

    def fetch_block_height_updates(self, one_off=True, callback_function=None):
        return self._standard_binance_change_socket_handler(one_off=one_off, callback_function=callback_function)

    def fetch_trades_updates(self, trading_pairs, one_off=True, callback_function=None):
        """
        Returns individual trade updates by trading pair name

        :param trading_pairs: Trading Pair

        Sample Return:
        {"stream":"trades","data":[{"e":"trade","E":7549438,"s":"100K-9BC_BNB","t":"7549438-0","p":"3333.00000000",
        "q":"0.02611100","b":"1D518A2563B0CB912AD70DEB7A18CD7ED2FBB7D4-11",
        "a":"EA1AE716501D1DB0B9F295A30891D9E562828678-12","T":1554964166437515341,
        "sa":"tbnb1agdww9jsr5wmpw0jjk3s3yweu43g9pnc4p5kg7","ba":"tbnb1r4gc5ftrkr9ez2khph4h5xxd0mf0hd75jf06gw"}]}
        """
        postfix_url = trading_pairs + '@trades'
        return self._standard_binance_change_socket_handler(one_off=one_off,
                                                            callback_function=callback_function,
                                                            parameter=postfix_url)

    def fetch_market_diff_stream(self, trading_pairs, one_off=True, callback_function=None):
        """
        Order book price and quantity depth updates used to locally keep an order book.

        :param trading_pairs: Trading Pair

        Sample Return:
        {"stream":"marketDiff","data":{"e":"depthUpdate","E":1554964484,"s":"100K-9BC_BNB",
        "b":[["3333.00000000","0.07398900"]],"a":[]}}
        """
        postfix_url = trading_pairs + '@marketDiff'
        return self._standard_binance_change_socket_handler(one_off=one_off,
                                                            callback_function=callback_function,
                                                            parameter=postfix_url)

    def fetch_market_depth_stream(self, trading_pairs, one_off=True, callback_function=None):
        """
        Fetch Market Top 20 Levels of Bids and Asks

        :param trading_pairs: Trading Pair

        Sample Return:
        {"stream":"marketDepth","data":{"lastUpdateId":7551469,"symbol":"100K-9BC_BNB",
        "bids":[["3333.00000000","0.07398900"]],"asks":[["66666.00000000","1.68270010"],["70000.00000000","1.00000000"],
        ["90000000000.00000000","40.05079290"]]}}
        """
        postfix_url = trading_pairs + '@marketDepth'
        return self._standard_binance_change_socket_handler(one_off=one_off,
                                                            callback_function=callback_function,
                                                            parameter=postfix_url)

    def fetch_kline_updates(self, trading_pair, interval, one_off=True, callback_function=None):
        postfix_url = '%s@kline_%s' % (trading_pair, interval)
        return self._standard_binance_change_socket_handler(one_off=one_off,
                                                            callback_function=callback_function,
                                                            parameter=postfix_url)

    def fetch_ticker_streams(self, trading_pair=None, is_full_data=True, one_off=True, callback_function=None):
        """
        24hr Ticker statistics for a single symbol are pushed every second

        :param trading_pair: Trading Pair, if not provide will return all data
        :param is_full_data: will return full data?

        Sample Return:
        {"stream":"ticker","data":{"e":"24hrTicker","E":1554966678,"s":"100K-9BC_BNB","p":"0.00000000",
        "P":"0.00000000","w":"5023.09923713","x":"3333.00000000","c":"66666.00000000","Q":"0.00010000","b":"0.00000000",
        "B":"0.00000000","a":"66666.00000000","A":"1.68260010","o":"66666.00000000","h":"66666.00000000",
        "l":"3333.00000000","v":"0.02784240","q":"139.85513820","O":1554880245974,"C":1554966645974,"F":"7366949-0",
        "L":"7554709-0","n":23}}
        """
        if trading_pair:
            if is_full_data:
                postfix_url = '%s@ticker' % trading_pair
            else:
                postfix_url = '%s@miniTicker' % trading_pair
        else:
            if is_full_data:
                postfix_url = '$all@allTickers'
            else:
                postfix_url = '$all@allMiniTickers'

        return self._standard_binance_change_socket_handler(one_off=one_off,
                                                            callback_function=callback_function,
                                                            parameter=postfix_url)

    def _standard_binance_change_socket_handler(self, one_off, callback_function, parameter=None):
        # Get caller function name
        caller_func_name = inspect.stack()[1].function
        # todo:
        # refer to: https://stackoverflow.com/questions/900392/getting-the-caller-function-name-inside-another-function-in-python/900413
        # seems caller_func_name is different from python 3 and python 2, need to test on python 2

        # Get ws name from Mapper
        ws_api_name = WS_ENTRY_POINTS[caller_func_name]

        # Compose whole ws url
        ws_url = self.base_ws_url + ws_api_name
        if parameter:
            ws_url += parameter
        print('WebSocket URL:' + ws_url)

        # Create Socket instance
        socket_obj = BinanceChainSocketConn(ws_url=ws_url)

        # Stream data
        if one_off:  # short-live-call, just return
            return socket_obj.one_off()
        else:  # long-live-call, keep getting data
            if callback_function:
                socket_obj.long_conn(callback_function)
            else:
                socket_obj.long_conn(_default_call_back)