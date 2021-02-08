name = 11
age=18
sex='girl'
if name <= 11 and age != 20:
    print('welcome to here')
    if sex == 'boy':               # if里嵌套if
        print('good strong~!')
    else:
        print('beautiful')
else:
    print('get out~!')          #python靠缩进来控制结构。


a= input('请输入一个数字：')
if int(a)<10:
    print('haha')
elif int(a)<20:                 # elif的用法。
    print('go to school')
else:
    print(a,type(a))
    b=int(a)
    print(b,type(b))
