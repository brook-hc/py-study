

for i in 'hello':
    print(i,end=' ')
print()

a=['a','b','c','d','e','f','g']    # 列表也有和上面字符串一样的骚操作
print(type(a))

for i in a:
    print(i,end=' ')
print()

b= 'o' in a     # 查看o是否在列表里，返回的是true或false
print(b)


w=['惠普','华为','苹果','三星','小米','神舟','联想']
long=len(w)
# for i in range(long):
#     if w[i] in '华为':
#         del w[i]
#         long-=1    # 这是错误的代码，因为long传入range里就不可更改了，由于del删除了一个元素，那么实际列表个数减1，所以就越界了。
# else:
#     print('没有找到')
# print(w)

i=0                  # while循环的变量要先定义
while i<long:       # while循环的参照值long可以改变，但for循环range里的值不能修改。
    if w[i] in '华为'or w[i] in '神舟':
        del w[i]
        long-=1
        i+=1
    else:
        i+=1



#首先列表不同与字符串，列表是可以改变的，可以任意添加或删减元素。
a=list(range(4,25,2))   #list和range可以一起用，range是生成数字的函数，（起始位，结束位，每跳跨度），包头不包尾。
print(a)

b=[x*2 for x in range(10)]    #for循环，把range里面每个数乘以2。
print(b)
b=[x*2 for x in range(10) if x%3==0]  #得到上面的结果后，再判断每个数对3取余是否等于0，符合条件的才保留。
print(b)

c=[1,2,3]
c.append(5)   #末尾添加元素，只接受一个参数，这个不改变内存地址，但d=c+[6]也是在末尾加元素，它就创建了一个新对象，也就是说改变了内存地址。
print(c)

c.extend([50,60])  #可以在末尾添加多个元素，且不改变内存地址，一般推荐用这个。
print(c)

c.insert(1,7)   #在1号元素前面插入一个元素。
del c[2]      #删除指定元素。
d=c.pop(4)      # 取下标为4的元素
print(c)
print(d)

c=[1,2,1,4,1,6,7,8,9]
c.remove(1)         # 补充一个：remove(),这个括号里面操作的是元素，而不是索引，将删除该元素在列表中的第一个。
print(c)