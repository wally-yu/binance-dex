# Binance DEX API implemented based on: https://testnet-dex.binance.org/doc/api-reference/dex-api/paths.html
import requests

DEFAULT_API_BASE_URL = 'https://testnet-dex.binance.org/'

class Client():
    """
    API Client for Binance DEX
    """
    def __init__(self, api_base_url_with_port=DEFAULT_API_BASE_URL):
        """
        API Client
        :param api_base_url_with_port:
        """
        self.api_base_url_with_port = api_base_url_with_port \
            if api_base_url_with_port[-1] == '/' else api_base_url_with_port + '/'

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
        ret = _binance_api_request(url=url,
                                   method='GET')
        return ret


def _binance_api_request(url, method, body=None):
    """
     - DESCRIPTION:
        Wrapper for Binance Request and official "Error" struct
        https://testnet-dex.binance.org/doc/api-reference/dex-api/paths.html#error

     - RETURN:
     {"status": <bool>,
      "message": <str>,                 # if error occur
      "result": <python data struct>}   # if status_code = 200, no error
    """
    if method.upper() == 'GET':
        ret = requests.get(url=url)
    elif method.upper == 'POST':
        ret = requests.post(url=url, json=body)
    else:
        return {'status': False,
                'message': 'Only "GET" or "POST" is allowed for Binance Request'}
    if ret.status_code == 200:
        return {'status': True,
                'result': ret.json()}
    else:
        try:
            return {'status': False,
                    'message': ret.json()['message']}
        except Exception as err:
            return {'status': False,
                    'message': str(ret)}
