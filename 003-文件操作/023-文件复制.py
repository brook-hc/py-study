# 第一，图片，word等二进制文件要加'b'模式
# 第二，b或r模式都是在open的时候加的，因为open相当于开辟一块内存，要实现告诉编译器，这块内存用于干什么。
import builtins
# 按住ctrl再点击builtins就可以打开这个py文件，里面列出了python可以自动加载的函数。
import os

with open(r'C:\Users\paulh\Desktop\qq头像.png', 'rb') as stream:
    pot = stream.read()
    with open('E:\pycharm\AI_study\qq头像.png', 'wb') as streamm:
        streamm.write(pot)

print('复制完成~！')

'''
os模块：
    os.path:常用函数
        dirname()   # 获取指定文件的目录
        join()      # 拼接获取新的路径
        split()     # 分割（文件目录，文件名）
        splitext()  # 分割（文件目录\文件名，文件扩展名）
        getsize()   # 获取文件大小
        
        
        isabs()     # 判断是否是绝对路径
        isfile()    # 是否是文件
        isdir()     # 是否是文件夹
        
    os常用函数：
        os.getcwd()     # 获取当前目录
        os.listdir()    # 显示文件夹内的文件和文件夹
        os.mkdir()      # 创建文件夹
        os.rmdir()      # 删除空的文件夹
        os.remove()     # 删除文件
        os.chdir        # 切换目录
'''

a= os.getcwd()
print(a)
b= os.listdir()
print(b)
