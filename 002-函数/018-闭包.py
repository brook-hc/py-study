

# 闭包就是解决如何调用一个函数内部的函数
def fun(a,b):
    c=20
    def goto():     # 这是定义，并没有调用
        d=a+b+c
        print(d/3)
   # return goto
fun(5,5)
#abc()

print('----------------------------')
def fun1():
    a=100
    def fun2():     # 这是定义，并没有调用
        b=90
        s=a+b
        print(s)
    def fun3():     # 这是定义，并没有调用
        fun2()
        #print(b)   # 只能调用另一个函数，但不能直接访问另一个函数内部的数据。
    fun3()          # 这才是调用
    return fun3

f=fun1()
f()

print('----------------------------')
# 闭包例子
def count():
    a=[0]
    def addone():
        a[0]=a[0]+1
        print('这是第{}次访问~!'.format(a[0]))
    return addone

f=count()
f()
f()
f()
f()
print('hello')
f()
f()