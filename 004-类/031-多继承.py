
class a():
    def demo(self):
        print('this is a\'s demo method')

    def test(self):
        print('this is a\'s test method')

class b():
    def demo(self):
        print('this is b\'s demo method')

    def test(self):
        print('this is b\'s test method')

class c(b,a):   # b在a前面，所以优先搜索b。
    pass

d=c()
print(dir(c))       # dir函数可以查看当前类自带的一些方法。
print(c.__mro__)    # mro可以查询类执行代码的搜索顺序，只能用类来查，不能用实例来查，如d.__mro_是错的。
d.demo()
d.test()


