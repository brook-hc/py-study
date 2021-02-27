import re

msg = 'abc123abc'
                                                # ?可以让正则表达式匹配最少的结果。
result = re.match(r'([a-zA-Z]+?(\d+))', msg)    # 这个？不起作用是因为后面还有个（），所以会匹配abc123
                                                # 去掉后面的括号，结果是'a'
print(result)
