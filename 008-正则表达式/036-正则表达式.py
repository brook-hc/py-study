
# python自带正则表达式包，导入的方法为：import re
#正则表达式是为了匹配字符串的，且只能匹配字符串。

import re
s='我翻开历史一查，这历史没有年代，歪歪斜斜的每页上都写着仁义道德几个字，我横竖睡不着，仔细看了半夜，才从字缝里看出字来，满本都写着2个字是吃人！'
result= re.match('我翻开历史',s)     # 只匹配开头
print(result)

result=re.search('仁义道德',s)      # 可以匹配查找‘仁义道德’在s中的位置，匹配不成功返回none。
print(result)
print(result.span())        # result里面也显示位置，但span可以只显示位置。
print(result.group())       # group可以提取匹配成功的内容。

d='a week has 7 days,a year has 4 seasons'
consequence = re.search('[a-z] [0-9] [a-z]',d)
print(consequence)

outcome=re.findall('[a-z] [0-9] [a-z]',d)
print(outcome)
# print(outcome.span())

f='a9879bjhlk68755h6khlh26ih2oh6'
result=re.findall('[a-z][0-9]+[a-z]',f)     # [0-9]+ 这里+表示出现次数>=1，连起来表示0-9的数字可以有>=1个。
print(result)

qq='84523452'       # qq号要求5到15位，第一位不能是0.
result= re.search('^[1-9][0-9]{4,14}$',qq)      # ^表示从头开始匹配，$表示匹配到目标最后一个字符。
print(result)                                   # {4}表示有且只有4个，{4，}表示大于等于4个，{4,9}表示大于等于4且小于等于9个。

usename='001admin'
result = re.search('^[0-9][0-9a-zA-Z]{5,}',usename)     # [0-9a-zA-Z]表示数字和小写，大写字母全包括。
print(result)

outcome= re.search('\d\w{5,}',usename)      # \d等价与[0-9]，\w等价于数字，大小写字母，下划线。
print(outcome)                              # \D表示不是[0-9]，\W表示不是数字，大小写字母，下划线，总之大写的命令就是取反。
print(outcome.group())

text='aa*py sadf.py re.py zoi.txt .py adg.py svbspyo.txt'
result=re.findall(r'\w+.py\b',text) # 这里是+所以匹配不到.py，如果是*就可以，因为*表示>=0,也就是可有可无。
print(result)                       # \b表示边界匹配，也就是当py出现在边界才匹配，出现在字符串中间则不匹配，如svbspyo.txt则不匹配，但apy.txt会匹配，.也算边界。
                                    # .在正则表达式里也是命令，表示匹配除换行符\n之外的所有字符(字母和数字)，故aa*py也匹配上了。
                                    # 要想过滤掉aa*py，用\.
                                    # \s表示空格。
                                    # ？表示0或1

email='23d43@gmail.net'
result=re.match(r'\w{5,15}@(qq|163|outlook|yeah|gmail)\.(com|net|cn)$',email)
print(result)       # (qq|163|outlook|yeah|gmail)表示或者qq或者162等，注意不能用[qq|163|outlook|yeah|gmail]这个表示或者q或者q或者|
                                    

phone='346-34523459'
result=re.match(r'(\d{3,4})-(\d{8})$',phone)    # ()起到分组作用，还可以分组获取值。
print(result.group())
print(result.group(1))      # 取第一个小括号的值
print(result.group(2))      # 取第二个小括号的值

msg ='<html><h1>abc</h1></html>'
outcome = re.match(r'<(.+)><([0-9a-zA-Z]+)>(.*)</\2></\1>$',msg)
print(outcome)
# ()里面要放变量，固定的如<>不能放圆括号里。 \1 表示和第一个括号内的内容一样，\2 同理。