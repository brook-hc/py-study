def send(name):
    print('准备发送：{}'.format(name))

def say():
    print('module1---hello world~!')

if __name__ == '__main__':
    print(__name__)     # 当前文件执行这句代码，永远显示__main__

    print('pual开发的代码')

# 判断__name__的目的是为了让模块里一些测试代码，不被别人导入。

print('hello')
print(__name__)