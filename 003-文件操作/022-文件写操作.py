

stream=open(r'E:\pycharm\AI_study\file_operate.txt','a')
# 写文件要在后面加模式，而读模式不需要，'a'是在文本末尾追加，'w'是删除原文件再重写。

s='\nlalalala'      # 加\n是为了换行再添加。


a=stream.write(s)
print(a)
stream.close()