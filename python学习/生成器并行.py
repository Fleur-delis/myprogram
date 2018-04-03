import time
def consumer(name):
    print("%s准备吃包子啦!" %name)
    while True:
        baozi=yield
        print("包子[%s]号来啦，[%s]准备吃包子！"%(baozi,name))
c = consumer("Alex")
c.__next__()
def producer(name):
    c=consumer('A')
    c1=consumer('B')
    c.__next__()
    c1.__next__()
    print("准备开始做包子啦！")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子！")
        c.send(i)     #将i的值传给yield
        c1.send(i)
producer("Alex")
