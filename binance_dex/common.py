import requests


def binance_api_request(url, method, body=None):
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
        return std_ret(False, 'Only "GET" or "POST" is allowed for Binance Request')
    if ret.status_code == 200:
        return std_ret(True, ret.json())
    else:
        try:
            return std_ret(False, ret.json()['message'])
        except Exception as err:
            return std_ret(False, '%s, exception: %s' % (ret, err))


def std_ret(status, data):
    if status:
        return {'status': True,
                'result': data}
    else:
        return {'status': False,
                'message': str(data)}