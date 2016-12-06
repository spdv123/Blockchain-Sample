import hashlib

class BitcoinMiner(object):
    """
    bitcoin miner
    """

    def miner(_self, data, target):
        nonce = 0;

        while True:
            hexDig = hashlib.sha256((data + str(nonce)).encode()).hexdigest()
            if hexDig.startswith(target):
                return hexDig, nonce
            nonce += 1

if __name__ == '__main__':
    client = BitcoinMiner()
    hashedValue, nonce = client.miner('This is a string', '0000')
    print(hashedValue)
    print(nonce)
