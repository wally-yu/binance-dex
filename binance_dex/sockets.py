import websocket
import time
import ssl
try:
    import thread
except ImportError:
    import _thread as thread


DEFAULT_SOCKET_BASE_ADDR_TEST = 'wss://testnet-dex.binance.org/api/ws/'


class BaseSocketConn(object):
    def ws_long_lived_conn(self, ws_url):
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(ws_url,
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close)
        ws.on_open = self.on_open

        ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    @staticmethod
    def on_message(ws, message):
        print('message: ' + message)

    @staticmethod
    def on_error(ws, error):
        print("### error ###")
        print(error)

    @staticmethod
    def on_close(ws):
        print("### closed ###")

    @staticmethod
    def on_open(ws):
        def run(*args):
            for i in range(3):
                time.sleep(1)
                ws.send("Hello %d" % i)
            time.sleep(1)
            ws.close()
            print("thread terminating...")

        thread.start_new_thread(run, ())


class SocketAccount(BaseSocketConn):
    def __init__(self, address):
        socket_url = DEFAULT_SOCKET_BASE_ADDR_TEST + address
        self.ws_long_lived_conn(socket_url)


class SocketTrades(BaseSocketConn):
    def __init__(self, trading_pair):
        socket_url = DEFAULT_SOCKET_BASE_ADDR_TEST + trading_pair
        self.ws_long_lived_conn(socket_url)


class SocketChain(BaseSocketConn):
    def __init__(self):
        self.socket_url = DEFAULT_SOCKET_BASE_ADDR_TEST + '$all'


    def get_block_height(self):
        ws_url = self.socket_url + '@blockheight'
        return self.ws_long_lived_conn(ws_url)


# socket_chain_instance = SocketChain()
# socket_chain_instance.get_block_height()

from websocket import create_connection
ws = create_connection("wss://testnet-dex.binance.org/api/ws/$all@blockheight",
                       sslopt={"cert_reqs": ssl.CERT_NONE})
while(1):
    result =  ws.recv()
    print(result)
ws.close()