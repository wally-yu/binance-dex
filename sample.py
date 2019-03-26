from binance_dex.api import Client

# create API Client instance
api_client = Client()

# call corresponding methods
print(api_client.get_fees())
