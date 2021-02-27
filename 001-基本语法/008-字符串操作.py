a = 'abcd'
b = 'abcd'
c = '''
abcd
'''
print(id(a))  # a和b内容一样，所以地址一样
print(id(b))
print(id(c))  # c的格式不一样，所以地址不一样

print(a == c)  # ==是判断值是否相等
print(a is b)  # is是判断地址是否相等。

# a=input()
# b=input()
print(id(a))  # 直接赋值地址是一样的，但input赋同样的值地址是不一样的。
print(id(b))

a = 'abc'
print(a * 5)  # 字符串可以乘倍数，就是重复打印。

name = 'paul-is-tiger'
result = 'ul-' in name       # 判断字符是否在字符串中，返回的是true和false。
print(result)               #  not in 判断字符不在字符串里面，返回的也是true和false，相反的意思，略。


print(r'我说\'哈哈哈\',可笑')  # 前面加了r，转义字符就不转义了。

he= 'fgherfhge'
ha= he.capitalize()     # 使字符串首字母大写。
print(ha)

she='i love you'
sh=she.title()          # 所有单词首字母大写，应该是以空格来判断是否为一个单词。
print(sh)

big=she.upper()         # 全部大写
print(big)
small=she.lower()       # 全部小写
print(small)

s='asdfas4'
a=s.isalpha()           # 判断字符串是否全是字母
print(a)

b='123f4'
c=b.isdigit()           # 判断字符串是否全是数字
print(c)

new='*'.join('abcd')    # join可以指定内容拼接字符串
print(new)

list=['a','b','c','d']
abc= '-'.join(list)
print(abc)

s='     hello      '
n=s.lstrip()            # lstrip,rstrip 用于去除左边和右边的空格。。
print(n+'8')
n=n.rstrip()
print(n+'8')

s='hello world hello kitty'     # 以指定的内容来分割字符串，第二个参数表示切几刀。
new=s.split('o',2)
print(new)
print(type(new))                # 以列表形式返回





import random
a=random.randint(1,20)  # 取随机数，括号里面可以指出所取随机数的范围。
print(a)
