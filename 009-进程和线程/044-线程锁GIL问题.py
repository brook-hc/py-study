# python默认会有把锁，当一个线程访问共享数据时，只要该线程没有结束，别的线程是不能访问该共享数据的。
# 只有当这个线程操作完成退出时，另一个线程才能访问该共享数据。
# 但是当数据量过大时，python会自动打开数据安全锁，导致对共享数据修改不安全，最终导致数据错误。
import threading

n=0

def add1():
   global n
   for i in range(1000):    # 这里设置一千万时，python就会打开安全锁，导致数据出错。
        n+=1

def add2():
    global n
    for j in range(1000):
        n+=1

p=threading.Thread(target=add1)
q=threading.Thread(target=add2)

p.start()

q.start()
q.join()

print(n)