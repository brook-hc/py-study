

class person:
    def __init__(self, name):
        self.name = name  # 难道类的变量都要在构造函数里定义吗？
        print('{}来到人间~！'.format(name))

    def eat(self):
        print('{}寻找可以吃的东西'.format(self.name))

    def run(self):
        print('{}岁的{}像野马一样狂奔'.format(self.age,self.name))
        print('跑累了之后')
        person.eat(self)

    def __del__(self):
        print('尘归尘，土归土~！')

    age=10

    @classmethod        # 加了这个的函数就是class函数，只属于class，不属于某个实例。
    def make_love(cls):
        print('很舒服~！')

p=person('周树人')
p.age=28
p.run()
print(person.age)
p.make_love()
# person是class，是模板，person.age是模板class的age，而P是某一个实例，p.age是实例化上的age。
# person.age=10,是改变模板的值，而p.age是改变实例上age的值，也就是age有两份，要操作age要注意区分。