class person:
    def __init__(self, name):
        self.name = name  # 只有实例化的时候才确定的值，这个值只在实例上存在，在class类中没有这个变量。
        print('{}来到人间~！'.format(name))

    def eat(self):
        print('{}寻找可以吃的东西'.format(self.name))

    def __run(self):
        print('{}岁的{}像野马一样狂奔'.format(self.age, self.name))
        print('跑累了之后')
        self.eat()

    def __del__(self):
        print('尘归尘，土归土~！')

    age = 10        # 类变量，实例里也有age，但实例里改动不会影响模板。创建实例后，在模板里改动不会影响实例。
    __age = 15      # 私有变量，外面直接person.__age访问不到，实例p.__age也访问不到。必须通过类里的函数间接访问。

    @classmethod  # 加了这个的函数就是class函数，只属于class，不属于某个实例。
    def make_love(cls):
        print('很舒服~！')

    def show(self):         # 为了显示私有变量
        print(person.__age)

    def show_method(self):  # 为了显示私有函数
        self.__run()

# print(person.__age)    私有变量访问不到。
p = person('辜鸿铭')
# print(p.__age)       私有变量不论是用person.__age和实例化的p.__age都访问不到。必须由内置函数来间接访问。
p.show()
p.show_method()

