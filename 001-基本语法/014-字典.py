
# 字典是成对出现的，不以下标索引，而是用key来索引
dic= {'name':'paul','age':32,'gender':"male"}
print(dic)
print(dic['gender'])        # name，age，gender就是key，有索引作用。

a={'name':"河川",'age':18,'job':'programmer'}
b=dict(name='河川',age=18,job="programmer")
print(a)
print(b)       #字典的2种定义方法。左边叫键，右边叫值，左边的键不能是列表，因为列表是可以改动的。右边的值可以是列表。不能出现2个一样的键。

print(a['name'])   #以列表的方括号来取值。
print(a.get('name1','不存在'))   #推荐用get来取值，如果键不存在不会报错，会返回null，也可以自定义返回值，如：不存在。

print(a.items())
print(a.keys())            #分别为显示所有内容，键，值。
print(a.values())

a['sex']='man'
print(a)                   #添加键值对，重复的将覆盖。

b=dict(habit='football',address='衡阳',name='何川')       #更新对象，把b覆盖添加到a。
a.update(b)
print(a)

del(a['name'])        #删除一个
print(a)
b=a.pop('age')    #删除并弹出一个
print(b)
print(a)

k=['name','age','job']              #通过zip函数生成字典。
v=['河川',18,'programmer']
d=dict(zip(k,v))
print(d)

g=dict.fromkeys(['name','age','job'])   #创建一个值为为空的字典。注意里面是列表形式。
print(g)

a=dict(name='何川',age=18,job='programmer',address='hengyang',hobby='football')
e,f,h,j,u=a                       #序列解包，分别赋键给各变量。
print(u)
y,i,o,r,c=a.values()          #赋值
print(o)
y,i,o,r,c=a.items()          #赋键值对
print(y)


