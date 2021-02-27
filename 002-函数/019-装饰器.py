
# 接上一讲闭包的案例。
def func(num):
    a = 100

    def goto():
        nonlocal a
        nonlocal num
        num += 1
        for i in range(num):
            a += 1

        print('修改后的a：',a)

    return goto

f=func(5)   # 看上去像是把func(5)赋给f，但其实func函数返回的是goto函数，故其实是把goto函数的地址给了f。
f()         # 现在运行f相当于运行wrapper函数。


print('---------------------------------------')
# 装饰器的用法
def decor(fun):
    a=100
    print('即将装修')
    def wrapper():
        fun()   # 这里调用func实际上是调用house函数。
        print('搞装修')

    return wrapper

@decor          # 把@decor写在函数house声明上面，decor会自动把house函数作为参数传入decor函数并执行decor函数。
def house():
    print('毛坯房')

print(house)
house()         # 注意：上面说会自动执行decor函数，但decor函数是有返回值的，返回的是wrapper函数，
                # 那么wrapper函数返回给谁了呢？其实它又自动把wrapper的地址赋给了house，
                # 此时，house不再是原来的函数了，house指向了wrapper。



print('---------------------------------------')
# 多层装饰器,极其牛逼,要细读
def zx1(name):
    print('1号装修公司开工')
    name()          # 此时name指向house，于是这句代码就是执行house函数
    def wrapper():
        print('正在给房子刷漆')
        print('1号公司装修完毕')

    return wrapper

def zx2(name):
    name()          # 这里的name指向的是zx1传过来的wrapper，故这里执行的是zx1的wrapper函数
    print('2号公司开始装修')
    def wrapper():
        print('正在给房子铺地板')
        print('2号公司装修完毕')
    return wrapper


@zx2
@zx1
def house():            # 首先会就近带入装饰器，把house传给zx1，zx1运行完，返回wrapper给zx2，
    print('还是毛坯房')  # zx2运行完，把zx2的wrapper传给house


house()         # 上面的装饰器运行完成后，最终会把zx2的wrapper函数地址赋给house，这里运行house其实是运行zx2的wrapper函数。


# 装饰器还有带参数的，具体实例看千锋的视频。