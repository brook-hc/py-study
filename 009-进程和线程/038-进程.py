import os
import time
from multiprocessing import Process

def task1(s):
    while True:
        time.sleep(s)
        print('任务1111',os.getpid(),'----------',os.getppid())


def task2(s,a1):
    while True:
        time.sleep(s)
        print('任务2222',os.getpid(),'----------',os.getppid(),a1)

num=0
if __name__ == '__main__':
    p1=Process(target=task1,name='任务1',args=(1,))    # 只有一个元素的元组，要加逗号。
    p1.start()
    p2=Process(target=task2,name='任务2',args=(1,'bb'))
    p2.start()
    # target= 表示要把什么函数变为进程，这是最关键的参数。
    # name=是给进程取名的，是Process自带的一个属性。
    # args是给target的函数传参的。用可迭代的元组或列表形式传参。上例(1,)是给task1(s)传的值，也可这样(1,'bb')传多个值，用task2(s,a1)来接。

    while True:
        num +=1
        time.sleep(0.1)
        if num == 100:
            print('执行完毕~！')
            p1.terminate()      # 该命令可以终结进程
            p2.terminate()
            break
