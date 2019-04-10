"""
Investigated python websockets packages including:
 - websocket： https://github.com/websocket-client/websocket-client
 - websockdets
 - ws4py
All above works fine
decided to adopt "websocket" because its simple as per zen of python: "Simple is better than complex"
"""

import ssl
import asyncio
import websocket
try:
    import thread
except ImportError:
    import _thread as thread

DEFAULT_SOCKET_BASE_ADDR_TEST = 'wss://testnet-dex.binance.org/api/ws/'


#
#
#
# class SocketAccount(BaseSocketConn):
#     def __init__(self, address):
#         socket_url = DEFAULT_SOCKET_BASE_ADDR_TEST + address
#         self.ws_long_lived_conn(socket_url)
#
#
# class SocketTrades(BaseSocketConn):
#     def __init__(self, trading_pair):
#         socket_url = DEFAULT_SOCKET_BASE_ADDR_TEST + trading_pair
#         self.ws_long_lived_conn(socket_url)
#
#
# class SocketChain(BaseSocketConn):
#     def __init__(self):
#         self.socket_url = DEFAULT_SOCKET_BASE_ADDR_TEST + '$all'
#
#
#     def get_block_height(self):
#         ws_url = self.socket_url + '@blockheight'
#         return self.ws_long_lived_conn(ws_url)


# socket_chain_instance = SocketChain()
# socket_chain_instance.get_block_height()

from websocket import create_connection
# ws = create_connection("wss://testnet-dex.binance.org/api/ws/$all@blockheight",
#                        sslopt={"cert_reqs": ssl.CERT_NONE})
# while(1):
#     result =  ws.recv()
#     print(result)
# ws.close()

class BinanceChainSocketConnBase(object):
    """
    Binance Chain Abstract Base Socket Connections,
    As per https://github.com/websocket-client/websocket-client, provide 2 ways to connect to socket:
     - Long-lived connection
     - Short-lived one-off send-receive
    """
    def __init__(self, ws_url):
        websocket.enableTrace(True)
        self.ws = None
        self.ws_url = ws_url

    def long_conn(self):
        self.ws = websocket.WebSocketApp(self.ws_url,
                                         on_message=_on_message,
                                         on_error=_on_error,
                                         on_close=_on_close)
        self.ws.on_open = _on_open
        self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    def one_off(self):
        self.ws = create_connection(self.ws_url,
                                    sslopt={"cert_reqs": ssl.CERT_NONE})
        result = self.ws.recv()
        self.ws.close()
        return result

    # def __del__(self):
    #     self.ws.close()


# --------------------------------------------
# Below are default behavior to be used for websocket, feel free to override by yourself
def _on_message(ws, message):
    print('msg')
    print(message)


def _on_error(ws, error):
    print(error)


def _on_close(ws):
    print("### closed ###")


def _on_open(ws):
    def run(*args):
        pass
    thread.start_new_thread(run, ())
# --------------------------------------------


ojb = BinanceChainSocketConnBase("wss://testnet-dex.binance.org/api/ws/$all@blockheight")
# ojb.long_conn()
print(ojb.one_off())