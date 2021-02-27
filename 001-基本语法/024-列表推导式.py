

#[表达式 for 变量 in 旧列表 if 判断条件]

name=['asdf','jfogdo','ds','sdfgsd','sdfe','sgsgfg']
a=[i for i in name if len(i)<5]     # 表示把长度小于5的字符串找出来放到table变量里。
b=[i.capitalize() for i in name if len(i)<5]    # 首字母大写
print(a)
print(b)

print('----------------------------------------------')
# 类似笛卡尔积，把每个偶数与其他奇数组成元组
a=[(i,j) for i in range(8) if i%2==0 for j in range(8) if j%2!=0]   #注意这里第二个for是在if里面嵌套的。
print(a)

# 这种方法了解即可