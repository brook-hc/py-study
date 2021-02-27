# new函数是继承父类的函数，当创建类的时候，python自动继承了父类object的new函数，该函数的作用是分配内存，写入要创建的类的信息。

class musicplay(object):        # object也可以不写，默认继承
    def __init__(self):
        print('播放器初始化')

    def __new__(cls, *args, **kwargs):
        print('创建对象，分配空间')
        addres = super().__new__(musicplay)   # 继承父类object的new方法，故传进去的是当前的类名，也可用cls。
        print(addres)                         # super().__new__()函数有返回值，返回的是当前类的内存地址。
        return addres                         # 而__int__会自动接收new函数返回的地址，只有接受到内存地址，__int__才能初始化。

p=musicplay()
print(p)        # 再次打印类地址，和new函数里打印的地址相同。
