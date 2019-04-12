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

from websocket import create_connection


class BinanceChainSocketConn(object):
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
        self.on_error_func = _on_error

    def long_conn(self, func, *args):

        self.ws = websocket.WebSocketApp(self.ws_url,
                                         on_message=func,
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

    def __del__(self):
        try:
            self.ws.close()
        except Exception:
            pass  # already closed connection, quit silent


# --------------------------------------------
# Below are default behavior to be used for websocket, feel free to override by yourself
def _on_message(*args):
    print('!!! Here is default callback function, '
          'please pass in your own customized callback function to handle received data !!!')
    print(args[1])


def _on_error(ws, error):
    print(error)


def _on_close(ws):
    print("### closed ###")


def _on_open(ws):
    def run(*args):
        pass
    thread.start_new_thread(run, ())
# --------------------------------------------
