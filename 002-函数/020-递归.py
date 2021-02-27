def test01(n):
    print("hello python!:",n)
    if n==0:
        print("over")
    else:
        test01(n-1)
    print("heihei python!:",n)


test01(3)                #每次调用自己相当于新建了一个栈，经典递归，不谈！

print('---------------------------------------')
# 算阶乘
def test01(n):
    if n==1:
        return 1
    else:
        return n*test01(n-1)

a=test01(5)
print(a)