def demo():
    '''打印一句话'''
    print('hello world~!')


print(dir(demo))  # dir函数可以查看某类型的内置方法
print(demo.__doc__)  # 如查看函数的说明文档，demo.__doc__

print('---------------------------------------')


# 类和对象
class person:
    def __init__(self, name):
        self.name = name  # 难道类的变量都要在构造函数里定义吗？
        print('{}来到人间~！'.format(name))

    def eat(self):
        print('{}寻找可以吃的东西'.format(self.name))

    def __del__(self):
        print('尘归尘，土归土~！')
    age=10 # 这属于什么变量？下一节讲。

a = person('paul')
a.eat()
a.age=50
print(a.age)
# del a    因为a是全局定义的，所以当前页面的所有代码都走完才会释放a。故析构函数会在-------的下方出现。
# 如果del不注释掉，那么就会先删除a，再打印-------
print('---------------------------------------')
