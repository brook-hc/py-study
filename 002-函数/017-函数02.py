

# python可以直接把函数赋给一个变量，本质是把地址给另一个变量。
def func(a,b):
    print('a+b=',a+b)

func(3,4)
c=func                  # 把函数赋给变量不能加括号，python默认加（）就是调用。
c(4,5)
print(id(func))
print(id(c))            # c=func就是赋地址给c，故c和func的地址都是一样的。

print('----------------------------')
# 函数外面的变量是全局变量，我们要在函数内部访问全局变量时要加global
a=10
def fierce(b):
    #global a
    b=a
    print(b)
fierce(20)
print(a)


print('----------------------------')
# 函数传递可变对象(列表，字典)
a=[1,2,3,4]
def love(m):
    print(id(m))
    m.append(9)
    print(id(m))

love(a)
print(id(a))
print(a)

print('----------------------------')
# 函数传递不可变对象（int，float，string，元组等）
a=10
def goto(b):
    print(id(b))
    b=20            # b本来是指向a的地址的，一旦给b赋值，b就会重新开辟一块地址来赋值，因为a是int型，为不可变对象。
    print(id(b))    # 想改变a的值，可以用上面学的global技术

goto(a)
print(id(a))
print(a)

print('----------------------------')
# 注意：深拷贝和浅拷贝很重要，直接看尚学堂视频吧。

a=10
b=20
def swap():
    global a,b
    temp = a
    a=b
    b=temp

swap()
print(a,b)
