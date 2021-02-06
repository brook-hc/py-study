name = "叶红鱼"
age = 18
money = 520.1314

print(name, age, money, sep="*")
# 当打印多个变量时，逗号本来是默认一个空格的，用sep=""可以自定义中间插入什么。如：sep="*"  sep="&"

print('aaa', end='')
print('bbb', end='')
print('ccc', end='')
'''
首先三个单引号是多行注释！！！原本print会默认换行的，也就是末尾隐藏了end='\n'，
现在end里面什么都不加，就不会换行了。
'''

message = '''
淘宝
账户名：坐忘一生
购物车：外星人电脑
'''
print(message)    # 简直是神操作，三个引号就可以按照原样格式输出！！！
