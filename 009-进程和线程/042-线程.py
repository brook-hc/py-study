import threading
from time import sleep


def download(n):
    images = ['boy.jpg', 'girl.jpg', 'man.jpg']
    for i in images:
        print('正在下载：{}'.format(i))
        sleep(n)
        print('下载完成：{}'.format(i))

def listenmusic(m):
    music=['大碗宽面','土耳其冰淇淋','九转肥肠','射雕英雄传']
    for mus in music:
        print('正在听\'{}\''.format(mus))
        sleep(m)

if __name__ == '__main__':

    t = threading.Thread(target=download, args=(1.5,))
    t.start()

    c=threading.Thread(target=listenmusic,args=(1,))
    c.start()

    n = 1
    while True:
        print(n)
        n += 1
        sleep(2)
