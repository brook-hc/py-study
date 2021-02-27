#
# num= int(input('请输入一个整数：'))
# result= 10/num
# print(result)
# 运行上面的代码时，会出现2个错误情况，1，输入的不是整数，编译器提示valueerror。2，输入的值为0，提示zerodivisionerror错误。
# 如果我们不用try-except来处理，遇到这2个错误程序会终止运行。

num= int(input('请输入一个整数：'))
result= 10/num
print(result)
print('------------------------------------------')
# 当输入字母a或数字0时，这行横线是不会打印的，故不使用异常处理，出现错误会终止程序运行。


print('------------------------------------------')
# 使用异常处理，遇到错误，程序仍可继续进行。
try:
    num= int(input('请输入一个整数：'))
    result= 10/num
    print(result)

except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('请输出一个数字')
