from binance_dex.lib import crypto


class BinanceChainCrypto(object):
    def __init__(self, is_test_net=False):
        crypto.IS_TEST_NET = is_test_net

    @staticmethod
    def generate_mnemonic():
        """
        Genereate Mnemonic words as string.
        Binance chain using strength=256, will return 24 words

        Sample Return <str>:
        party wear unknown cause cement select wood veteran spoon spider paddle stumble twist length fly budget helmet
        pilot robust brand public boat define battle
        """
        _, mnemonic = crypto.HDPrivateKey.master_key_from_entropy(strength=256)
        return mnemonic

    def generate_key(self):
        """
        Generate Private Key, Public Address and mnemonic

        Sample Return <dict>:
        {'private_key': '33b1ffceb5a80e4436035f71573b3198e5dff64bc1d620625d3ae94ca9ceca1e',
        'public_address': 'bnb1xzx5lungjnlc8fmx7qa7c7njxsqphcr7y9j9za',
        'mnemonic': 'world supply word message critic woman donate romance sleep safe voyage faint maid utility fish
        shuffle offer pulse tail owner burger vicious until sword'}
        """
        master_key, mnemonic = crypto.HDPrivateKey.master_key_from_entropy(strength=256)
        root_keys = crypto.HDKey.from_path(master_key, crypto.BIP_32_PATH)
        ret = self._get_keys_from_root_keys(root_keys)
        ret['mnemonic'] = mnemonic
        return ret

    def generate_key_from_mnemonic(self, mnemonic):
        """
        Generate Private Key, Public Address from mnemonic words

        :param mnemonic: Mnenonic string (24 words)

        Sample Return:
        {'private_key': '0225fb7752873b93f3bf9afc8a3bdd35e9052e04e21ffd91e42d8aa45a542459',
        'public_address': 'bnb1ejk8eah9ct5rgl3k4s4kqc3udf7jy9qvzjw56m'}
        """
        master_key = crypto.HDPrivateKey.master_key_from_mnemonic(mnemonic)
        root_keys = crypto.HDKey.from_path(master_key, crypto.BIP_32_PATH)
        return self._get_keys_from_root_keys(root_keys)

    def generate_keys_from_mnemonic(self, mnemonic, num_keys):
        """
        Generat Bunch of Private Keys, Public Address from one set of Mnemonic words

        :param mnemonic: Mnemonic string (24 words)
        :param num_keys: How many keys want to derive

        Sample Return:
        [{'private_key': 'bedd712859eb0c6c3519dcae1749088e2168b545844f5fb6a93f97fef4429b56', 'public_address': 'tbnb1uj5056ys4ssr4zdzq9c7n92yndd5e5hm5m77nl'}
        {'private_key': '0b303f09175ce3ab018cafb84caee1d15a7fc5862f40302f8a5ee181b4833ce1', 'public_address': 'tbnb1j93zkpj7u03g4s240h5n6wf8ttdesau6s2sl97'}
        {'private_key': 'a6ba3f2efbb229e774f89c8d793f1d24be8b7270e43f04d39724936cc9d89e7b', 'public_address': 'tbnb1v9unkets8tj44m075pfqeefvd0e930jm82ryl9'}
        {'private_key': '6fca86eb670703be188d6d1c8498bec634e136a1a9f478fc8e1dc9f029d01988', 'public_address': 'tbnb1d9r2cxh2fpghnt2cjk4tzmeaangmx32gfvygr6'}
        {'private_key': 'b68a67b4d891848709461d8042ea491d18ce484931b357fb6fba25051bf77f03', 'public_address': 'tbnb14uuptgy8ddajemzjv6u4lxshfmx4wfq45lrlus'}
        {'private_key': '3ed40754e508b16a21dda458e4c964072c13b853a4404e95faa8673c85ed7100', 'public_address': 'tbnb1064mallpzhu6z4g409w37fwep9l96mdws368ry'}
        {'private_key': '341a319cf35f7b06284f81fdc35b8e4000fd6e81e568102a4cc914b085b0be76', 'public_address': 'tbnb1c78d02cn0vmfd26wj4a70y2fwpns2vecq6xal9'}
        {'private_key': '47505fdd625018b0e4c4b13e8bba4209fcc093906142a23e74b40cc6bd1d4fca', 'public_address': 'tbnb1g2g94cesgvcjjv2js39lh4jrmjkkhqdpxcspvu'}
        {'private_key': '66d53d3f5dbdaa11a3987209477c679a7c2d46f595fd873c1025764f2162c66b', 'public_address': 'tbnb1ns4nhndexpve7l8nv82ajn24tk3anwsuadg6a9'}
        ... ...
        {'private_key': 'e287292e5f8c65bb59528e372bf8fe90972e02ffd3da085677140ef3e9053d29', 'public_address': 'tbnb1muln7lrsl4y7mmt07rplevzfsvkfgdunm2f42k'}]
        """
        if not isinstance(num_keys, int):
            raise Exception("num_keys must be int")
        master_key = crypto.HDPrivateKey.master_key_from_mnemonic(mnemonic)
        root_keys = crypto.HDKey.from_path(master_key, crypto.BIP_32_PATH)
        private_key = root_keys[-1]
        ret_keys = list()
        for i in range(num_keys):
            keys = crypto.HDKey.from_path(private_key, '{change}/{index}'.format(change=0, index=i))
            ret = self._get_keys_from_root_keys(keys)
            ret_keys.append(ret)
        return ret_keys

    @staticmethod
    def _get_keys_from_root_keys(root_keys):
        private_key = root_keys[-1]
        public_key = private_key.public_key
        return {
            'private_key': private_key._key.to_hex(),
            'public_address': public_key.address()
        }
