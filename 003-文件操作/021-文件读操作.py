

file=open(r'E:\pycharm\AI_study\file_operate.txt')  # open相当于把文件放入内存了，之后所有的操作都针对file进行。
                                                    # 加r代表\不转义

# stream= file.read()
# print(stream)
while True:
    stream=file.readline()
    if not stream :             # not a 表示如果a为false返回true，如果a为true返回false。
        break
    else:
        print(stream,end='')    #由于readline默认有换行，所以我们print就不换行了


file.close()

print('--------------------------------------')
# 若文件为doc，图片，等等，里面是16进制表示的代码，如果用默认的read的话，会报错。
file1=open(r'E:\pycharm\AI_study\qq头像.png',mode='rb')    # 图片等非文本文件，要添加mode='rb'，文本是rt。
demo= file1.read()


print(demo)



file1.close()
