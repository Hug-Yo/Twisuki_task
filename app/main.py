# 这里是包的主入口, 因为外面那个 main.py 运行的是 app.main, 指向的就是本文件.
# 你要通过 import 导入其他文件, 然后树状的启动它们.
# 注意: main 只是个入口, 不要把逻辑都堆在这里.

# 此刻你可以先不管这里, 读完其他所有文件再回来看看接下来怎么做.

# 相比已经理清了整个包的组织吧, 程序运行起来就很简单了.
# 首先初始化程序, 也就是 crud.py 的 init() 函数.
# 之后运行 command.py 的 app() 函数, 启动主循环, 与用户交互.

if __name__ == "__main__":
    from app.crud import init
    from app.command import *
    init()
    app()
    ...

