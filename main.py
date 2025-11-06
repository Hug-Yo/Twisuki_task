# 你的代码主要应该在 app 文件夹里.
# 实际上这是一个 python 包, 包有包自己的运行方式, 也就是 `python -m app.main`.
# 为了方便, 这个文件完成了这项工作, 你只需要运行该文件即可.
# 这里已经写好了, 不必修改.

import subprocess
import sys

if __name__ == "__main__":
    subprocess.run([sys.executable, "-m", "app.main"])

