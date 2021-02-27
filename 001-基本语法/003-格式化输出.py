name = '叶孤城'
age = 45
address = '青城山'
num = 13826160127

print('他的名字叫:'+name+',年龄大概:'+str(age)+',居住在:'+address+',联系方式'+str(num) )
#字符串只能拼接字符串,如果要拼接int等别的类型需要强制类型转换，str(xxx)

print('他的名字叫:%s,年龄大概:%d,居住在:%s,联系方式为：%d' % (name, age, address, num))
print('他的名字叫:%s\n年龄大概:%s\n居住在:%s\n联系方式为：%s' % (name, age, address, num))
# 其实%s在底层是强行把别的类型转换为string，如果这里想以int类型输出则替换为%d

salary=8899.2534523
print('你的薪水为：%.3f' %salary)       #%f是浮点型，%后面加.3表示精确到小数点3位。

name='西门吹雪'
age= 42
fight=95.97834
message='''
他的名字叫{},
他看上去大概{}岁，
其战斗力高达{}'''.format(name,age,fight)
print(message)       # format格式化输出，这样就不用分%s，%d了。。。

