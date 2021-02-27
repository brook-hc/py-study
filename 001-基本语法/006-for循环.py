for a in range(3, 8):
    print(a,end='\t')            # range的第一个数是多少就是多少，第二个数始终要减1

total = 0                    # 从1加到100
for num in range(101):
    total = total + num
print(total)

for a in range(6):
    for b in range(6):
        if b < 5:
            print(b, end=',')
        else:
            print(b)
    print()  # 起到换行的作用。

for m in range(1, 10):      # 乘法算术表
    for n in range(1, m + 1):
        print('{}*{}={}'.format(m, n, (m * n)), end="\t")
    print()                 # 换行作用


for i in 'hello':           # i不但可以取数，还可以取字符串
    print(i,end='\t')
print()

print('----------------------------------------------')
# 重点：这种方法可以直接取列表里面的值。
a=['a','b','c','f']

for i in a:
    print(i,end=' ')