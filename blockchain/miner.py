import hashlib

class BitcoinMiner:
    """
    bitcoin miner
    """

    def __init__(self, clientID):
        self.clientID = clientID

    def miner(self, data, target):
        nonce = 0;

        while True:
            hexDig = hashlib.sha256(data + self.clientID + str(nonce)).hexdigest()
            if hexDig.startswith(target):
                return hexDig, nonce
            nonce += 1

if __name__ == '__main__':
    client = BitcoinMiner('deadbeef')
    hashedValue, nonce = client.miner('This is a string', '00000')
    print(hashedValue)
    print(nonce)
