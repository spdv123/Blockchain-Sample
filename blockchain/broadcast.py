# -*- coding: utf-8 -*-

class Broadcaster:
    '''
    This is the broadcast module of blockchain-sample
    '''

    def __init__(self):
        pass

    def broadcast(self, message):
        '''
        Broadcast message to 127.0.0.1:22000-23000
        '''
        import socket
        s = socket.socket()
        for i in range(22000, 23000):
            if True:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect(('127.0.0.1', i))
                    s.send(message)
                    print '向#', i - 22000, '发送了消息'
                except socket.error:
                    pass
                finally:
                    s.close()

if __name__ == '__main__':
    br = Broadcaster()
    br.broadcast('1 2 3')
