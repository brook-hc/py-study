

# 当我们不能发现所有可能的错误时，通常用捕获未知错误的方法，让程序正常进行下去。
# 下面的代码是假设我们未发现除数为0的错误时，又想让程序继续进行下去的方法。
try:
    num= int(input('请输入一个整数：'))
    result= 10/num
    print(result)
except ValueError:
    print('请输出一个数字')
except Exception as result:
    print('出现未知错误: {}'.format(result))       #当输入0时，就可以打印这句话。