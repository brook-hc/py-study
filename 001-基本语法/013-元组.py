a=(1,5,3,4,2,9,6,7)          #与列表不一样，元组是不能更改的。
print(type(a))
a=1,5,3,4,2,9,6,7       #元组的2种定义方法
print(type(a))
b=1,
b=(1)    #注意当元组只含一个元素时，后面必须加个逗号，即b=(1,) 要不然会当作其本身的类型，这里会把b当做int类型。
print(type(b))

c=tuple([1,2,3])
print(type(c))
c=tuple(range(10))
print(c)                         #tuple函数，转化为元组类型。

print(sorted(a))      #注意sorted排序函数转化的结果是一个列表!