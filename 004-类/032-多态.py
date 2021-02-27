class dog():
    def __init__(self,name):
        self.name=name
    def game(self):
        print('{}蹦蹦跳跳的玩耍~！'.format(self.name))

class xiaotiandog(dog):

    def game(self):    # 发生了重写
        print('{}飞到天上去玩耍~！'.format(self.name))

class person():
    def __init__(self,name):
        self.name=name
    def play_with_dog(self,instan):
        print('{}与{}蹦蹦跳跳的玩耍~！'.format(self.name,instan.name))
        instan.game()

p=person('小明')
p.play_with_dog(xiaotiandog('哮天犬'))   # 就近原则，会优先调用哮天犬的game
p.play_with_dog(dog('旺财'))      # 优先调用dog里的game

# 多态就是就近原则，当出现重写情况，采取就近原则调用。