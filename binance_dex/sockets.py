"""
Wrapper for Binance Sockets
"""

from binance_dex.lib.sockets import BinanceChainSocketConn


IS_TEST_NET = False  # A varialbe to switch test net / main net, default would be MAIN-NET
SOCKET_BASE_ADDR_TEST_NET = 'wss://testnet-dex.binance.org/api/ws/'
SOCKET_BASE_ADDR_MAIN_NET = 'wss://dex.binance.org/api/ws/'


# Default Call back sample function to alert user to create own customized function
def _default_on_message(*args):
    print('Here is default callback function, '
          'please pass in your own customized callback function to handle received data')
    print(args[1])

class BinanceChainSocket(object):
    def __init__(self, is_test_net=IS_TEST_NET):
        self.base_ws_url = SOCKET_BASE_ADDR_TEST_NET if is_test_net else SOCKET_BASE_ADDR_MAIN_NET

    def get_block_height(self, one_off=True, callback_function=None):
        ws_url = self.base_ws_url + '$all@blockheight'
        socket_obj = BinanceChainSocketConn(ws_url=ws_url)
        if one_off:
            return socket_obj.one_off()
        else:
            if callback_function:
                socket_obj.long_conn(callback_function)
            else:
                socket_obj.long_conn(_default_on_message)

