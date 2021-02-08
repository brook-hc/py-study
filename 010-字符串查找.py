

temp = 'what are you going to do?'
s1 = temp.find('a')  # 找到第一个与其匹配的，并返回该位址。若找不到，返回-1
print(s1)

s2 = temp.find('y', 10, 15)  # 从下标10到15内寻找。
print(s2)

s3 = temp.rfind('g')  # 从右开始找。
print(s3)

s4 = temp.replace('g','o',1)   # 替换，把字符串中的g替换为o，第3个位置的数字为替换几个。
print(s4)

s5= temp.endswith('o?')         #查看是否以什么字符结尾。
print(s5)
s6=temp.startswith('what')      #查看是否以什么字符开始。
print(s6)