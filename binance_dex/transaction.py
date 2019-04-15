from binance_dex.tx_data_format import msg_freeze_pb2
tx_instance = msg_freeze_pb2.TokenFreeze()
# tx_instance.from='a'
tx_instance.symbol='f'
tx_instance.amount=100
print(tx_instance)