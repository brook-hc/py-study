from multiprocessing import Pool
import time
import random
import os

def task(name):
    print('开始做任务啦',name)
    start = time.time()
    time.sleep(random.random()*2)
    end = time.time()
    print('完成任务：{}，用时{}，进程ID：{}'.format(name,(end-start),os.getpid()))

# p.apply_async(func,args,kwargs,callback=函数)
# 这里的callback是指当前进程运行结束时，要做的动作。传给callback的一般是函数。

if __name__ == '__main__':
    p = Pool(3)  # 括号里填数字，表示允许多少个进程同时占用cpu，如果不填，默认的数量和cpu核数一致。
    tasks=['food','sleep','sing','smoking','perm','drink','exercise']
    for i in tasks:
        p.apply_async(task,args=(i,))   # 相当于创建一个进程放进pool里运行，但pool能容纳的数量为上面代码定义的，容纳不了的进程在外面排队。

    p.close()
    p.join()        # join要写在close后面，这是固定写法。




