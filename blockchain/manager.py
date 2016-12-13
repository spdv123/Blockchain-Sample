# -*- coding: utf-8 -*-

def main():
    '''
    操作矿工
    '''
    import random, sys, fns, hashlib, time
    from broadcast import Broadcaster
    if len(sys.argv) < 2:
        print "Usage: python manager.py clientNum"
        print "clientNum should in range(1, 10)"
        exit(1)
    try:
        num = int(sys.argv[1])
        assert num < 10
        assert num > 0
    except:
        print "Usage: python manager.py clientNum"
        print "clientNum should in range(1, 10)"
        exit(1)
    cid = []
    for i in range(num):
        cid.append(hashlib.sha256(str(random.randint(0,600000)+i*600001)).hexdigest())
    rnd = ''
    for i in range(100):
        rnd += str( random.randint(0, 100) % num )
    import os
    path = os.path.abspath('.')
    for i in range(num):
        fns.runNewCmd('python '+path+'/client.py ' + cid[i] + ' ' + rnd + ' ' + str(22000+i) + ' ' + str(i))
    time.sleep(1)
    Broadcaster().broadcast('deadbeef'*8 + ' ' + str(888888) + ' ' + 'deadbeef'*8)

if __name__ == '__main__':
    main()
