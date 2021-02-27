# 为了解决上述的global interpret lock问题，我们可以手动上锁。
# 操作系统里学的原语操作就是解决对共享数据访问的问题，这里的手动上锁就是写互斥原语。

import threading

n = 0
lock = threading.Lock()


def add1():
    lock.acquire()
    global n
    for i in range(10000000):  # 这里设置一千万时，python就会打开安全锁，导致数据出错。
        n += 1
    lock.release()


def add2():
    lock.acquire()
    global n
    for j in range(10000000):
        n += 1
    lock.release()


p = threading.Thread(target=add1)
q = threading.Thread(target=add2)

p.start()

q.start()
q.join()

print(n)
