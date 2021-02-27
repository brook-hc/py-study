#   []是列表推导式，()是生成器。这是全完不同的2个概念，生成器不会一下产生全部内存，调一次才会申请一次内存
a = (i for i in range(10))

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

print('-----------------------------------------------')


# 生成器第二种写法

def abc(n):
    i = 0
    while i < n:
        i += 1
        yield i  # yield一出现，这个函数就变成生成器了。


g = abc(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print('-----------------------------------------------')


def fib(length):
    a, b = 0, 1
    n = 0
    while n < length:
       # print(b)
        yield b
        a, b = b, a + b
        n+=1
    return '没有更多元素了'        # 当生成器越界了，会报错，可以用return来说明。

g=fib(6)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))