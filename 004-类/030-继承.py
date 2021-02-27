
class car:
    def __init__(self, name, mode, year):
        self.name = name
        self.mode = mode
        self.year = year

    def display(self):
        print('这是一辆:', self.name, '型号:', self.mode, '生产于:', self.year)

    init_oil = 0

    def addoil(self, oil):
        self.init_oil += oil

    def showoil(self):
        print('当前油量为：',self.init_oil)

mycar=car('宝马','x6','2018')
print(mycar.name)
print(mycar.mode)
print(mycar.year)
mycar.display()
mycar.showoil()
mycar.addoil(100)
mycar.showoil()

print('---------------------------------------------------')
# 下面是继承
class electricCar(car):
    def __init__(self,name,mode,year):
        super().__init__(name,mode,year)
        self.battery=100
    def addoil(self, oil):
        print('电动车不需要加油~！')
tesla=electricCar('tesla','mode3',2018)
tesla.display()
print(tesla.battery)
tesla.battery=150
print(tesla.battery)

tesla.addoil(80)        # 重写父类函数，使其优先调用子类的函数，这样就可以去除父类糟粕，用其经典。
print(tesla.init_oil)   # 并没有加油成功，因为他是调用的子类这个函数。
# 注意，子类不能直接调用父类的私有属性和私有方法，须通过父类普通方法间接访问私有属性和方法。