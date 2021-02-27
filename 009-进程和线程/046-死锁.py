from threading import Thread, Lock
import time

locka = Lock()
lockb = Lock()


class mythread1(Thread):
    def run(self):
        if locka.acquire():       # 该函数有bool类型的返回值
            print(self.name, '获取了a锁')
            time.sleep(0.1)
            if lockb.acquire(timeout=2):   # lockb.acquire是申请锁的函数，如果没申请到，会自动阻塞等待，同时返回false，如果成功拿到，返回ture。
               # 解决死锁的办法，可以加timeout参数，即如果申请不到，等待的时间，时间结束就放弃申请，同时解除阻塞，继续执行后面代码。
                print(self.name, '又获取了b锁')
                lockb.release()
            locka.release()


class mythread2(Thread):
    def run(self):
        if lockb.acquire():
            print(self.name, '获取了b锁')
            time.sleep(0.1)
            if locka.acquire():
                print(self.name, '又获取了a锁')
                locka.release()
            lockb.release()


if __name__ == '__main__':
    p = mythread1()
    q = mythread2()

    p.start()
    q.start()

# 解决方法可以在acquire里面加参数timeout。