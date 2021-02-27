#   线程可以共享全局变量，但是进程不行~！！！

import threading
import time

num=1000

def reduce1():
    for i in range(100):
        global num
        num-=1
        print(num)
        time.sleep(0.2)

def reduce2():
    for j in range(100):
        global num
        num-=1
        print(num)
        time.sleep(0.2)

p1=threading.Thread(target=reduce1)
p2=threading.Thread(target=reduce2)
p1.start()
p2.start()
p2.join()
print(num)
