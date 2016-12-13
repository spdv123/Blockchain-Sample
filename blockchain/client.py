# -*- coding: utf-8 -*-
'''
矿工
'''

from miner import BitcoinMiner
from broadcast import Broadcaster
from readWriter import RWer
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory

count = 0
_rnd = ''
_uid = 0
_clientID = ''
_port = 0

class RClient(Protocol):
    '''
    Real client 接收操作
    '''
    def connectionMade(self):
        pass
        #print self.transport.client, '建立了连接'

    def dataReceived(self, data):
        global count, _rnd, _uid, _clientID
        try:
            cid, nounce, hashed = data.split()
        except:
            return
        print cid, '声称挖到了', nounce, hashed
        RWer(_clientID).save(cid, str(nounce), hashed)
        count += 1
        if _rnd[count % len(_rnd)] == str(_uid):
            #print 'Turn to me'
            hsh, nounce = BitcoinMiner(_clientID).miner(data, '00000') # 这里阻塞了
            Broadcaster().broadcast(_clientID + ' ' + str(nounce) + ' ' + hsh)

class Client(Protocol):
    '''
    负责一些初始化操作
    '''

    @staticmethod
    def aSillyBlockingMethod(x):
        import time
        time.sleep(2)
        print x

    def __init__(self):
        '''
        clientID 矿工的ID, SHA256的随机数
        rnd 神秘字符串
        port 监听端口
        '''
        global _port

        self.factory = Factory()
        self.factory.protocol = RClient
        reactor.listenTCP(_port, self.factory)
        #reactor.callInThread(Client.aSillyBlockingMethod, "2 seconds have passed")
        reactor.run()


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 5:
        print "Usage: python client.py clientID rnd port uid"
        exit(1)
    _clientID = str(sys.argv[1])
    _rnd = str(sys.argv[2])
    _uid = int(sys.argv[4])
    _port = int(sys.argv[3])
    client = Client()
