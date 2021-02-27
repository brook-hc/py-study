def find_max(a,b):
    '''比较2个数的大小，并返回最大值。'''     #函数里面的”号不是定义字符串了，而是函数注释。
    if(a>b):
        print(a,"a较大")
    else:
        print(b,"b较大")

find_max(10,20)
find_max(30,5)
help(find_max)          #该语句可以查看函数里面的注释文档。

print('----------------------------')
def hello(a,b):
    if a>b:
        print("hello")
    else:
        print("fuck")
    return [a,b]        #当需要返回多个数值或结果时，可以考虑返回列表，元组，字典等容器。

c=hello(24,16)
print(c)

print('----------------------------')

def sex(a,b,c=5,d=8):
    print("{i}-{j}-{k}-{p}".format(i=a,j=b,k=c,p=d))      #format前面是点而不是逗号！
sex(1,2,3,4)
sex(1,2)          #有默认值的形参，一定要放在普通形参的后面，要不然会报错。

print('----------------------------')
#可变参数，有2种：1，*param，表示将多个参数放在一个元组中。2，**param，表示将多个参数放在一个字典里。
def passion(a,b,*c,**d):
    print(a ,b ,c ,d)
passion(10,20,30,40,sex="man",age=18)

print('----------------------------')
def love(*a,b,c):
    print(a,b,c)
love(1,2,3,4,b=9,c=17)    #如果可变参数在前面，那么就需要给普通参数强制命名，要不然会报错，因为系统不知道要赋值多少个数。
