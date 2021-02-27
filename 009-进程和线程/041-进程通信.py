from multiprocessing import Queue

q= Queue(5)

q.put('a')
q.put('b')
q.put('c')
q.put('d')
q.put('e')
print(q.qsize())   # 可显示队列中已占用的容量。
if not q.full():
    q.put('f')
else:
    print('队列已满~！')

print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))     # timeout表示等待时间，时间到了就报错。