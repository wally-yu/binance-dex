import requests
import inspect

IS_TEST_NET = False
PEER_LIST_TEST_NET = 'https://testnet-dex.binance.org/api/v1/peers'
PEER_LIST_MAIN_NET = 'https://dex.binance.org/api/v1/peers'

NODE_RPC_ENTRY_POINT_MAPPING = {
    '_helth_check': '/health'
}

class BinanceChainNodeRPC(object):
    """
    Node RPC Service
    Official Document: https://binance-chain.github.io/api-reference/node-rpc.html
    Official suggested 3 methodologies for RPC:
     - URI over HTTP
     - JSONRPC over HTTP
     - JSONRPC over websockets

    this SDK using "JSONRPC over HTTP" methodology
    """

    def __init__(self, node_rpc_url=None, is_test_net=False):
        # Customized RPC node
        if node_rpc_url:
            # Check node server health
            print('Using customized RPC server: %s' % node_rpc_url)
            if self._helth_check(node_rpc_url):
                # healthy, init done
                self.node_url = node_rpc_url
            else:
                # not healthy
                raise Exception('Node %s is not healthy')
            print('Customized RPC server is healthy\n')
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
        req_ret = requests.get(request_url)
        return req_ret