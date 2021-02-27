#集合的本质是字典，但是它只有键没有值。
a={1,2,3,4,5,6,'hahah'}
b={3,5,7,9,'heihei'}
print(a)
print(a|b)          #求并集
print(a&b)        #求交集
print(a-b)          #求差集

c=[1,2,3,4,5]
d=(3,4,5,6,7)
print(set(c))        #set函数，把列表，元组都定义为集合。
print(set(d))

a.remove('hahah')
print(a)
a.clear()
print('--------------------------')
print(a)
#a.remove（）删除，a.clear（）清空