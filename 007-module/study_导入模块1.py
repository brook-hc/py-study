# import study_测试模块1
# import study_测试模块2
# import study_测试模块1 as abc
# import study_测试模块2 as cbd
# as可以取别名
import random
from study_测试模块2 import receive   # 这里千万不要有括号！！！这种方式可以省略模块名。
from study_测试模块2 import say
from study_测试模块1 import say     # 当导入的2个模块有同名的函数，后导入的会覆盖先导入的函数。
                                   # 如果硬要导入2个相同名的函数，可以运用上面所学的取别名方式。
# from study_测试模块2 import *       # 加*可以导入模块中所有的内容。但是不推荐，出现同名不好排查。
# abc.send('hello')
receive()  #调的时候加括号。

say()

# 对导入的模块优先在当前文件夹下搜索，如果import random，但当前文件夹下也有个random文件，那就出错了。
print(random.__file__)      # __file__可以查询文件绝对路径。

# python中每个文件都可以当作模块被导入。当一个文件被导入时，该文件里所有没有缩进的代码都会被执行一遍。

