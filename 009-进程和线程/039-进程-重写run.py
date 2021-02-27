
from multiprocessing import Process
# 多进程无法共享全局变量，会在各自进程内部产生,实验就不做了，视频有讲解。


def run():
    n = 1
    while True:
        print('{}************'.format(n))
        n += 1

def test():
    n=1
    while True:
        if n<100000:
            print('{}------'.format(n))
            n+=1
        else:
            break

if __name__ == '__main__':
    p1=Process(target=test)
    p1.start()

    p2=Process(target=run)
    p2.start()
    p2.join()       # join可以等待子进程运行完，主进程才结束。
