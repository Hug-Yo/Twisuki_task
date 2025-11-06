# 本项目虽然可以写出不少操作来, 但本质上都是对 "任务" 的各种操作和展示.
# 这就是面向对象, "任务" 就是一个对象, 你需要在这里定义它.
# 这个是整个项目的根基, 在设计之后进行编写, 之后所有代码都将围绕这个对象展开.
# 所以本文件最先编写, 并在后续的代码中被大量引用, 因此不再改动.

# "任务" 对象用 class 定义, 这里预先写了一部分.


from enum import Enum
from datetime import datetime


""" 任务状态枚举 """
class TaskStatus(Enum):
    # 这是继承于 Enum(枚举) 的一个类, 你不必了解枚举的具体内容, 看到代码能理解, 能照着写就行.
    # 这里定义了几个任务状态. 请尝试定义 "已取消" 和 "已逾期" 两个状态.
    
    PENDING = "待处理"
    COMPLETED = "已完成"
    CANCELED = "已取消"
    OVERDUE = "已逾期"


class Task:
    # 这里就是 "任务" 对象的定义了, 下面定义了各个字段的类型.
    # 注意: id 是一个特殊的字段, 它是任务的唯一标识符, 类型为 int(整数), 一经创建不得修改, 不得重复.
    # 特别地, status 的类型是上面定义的 TaskStatus, 表示任务状态, 它只能从 TaskStatus 枚举中取值.
    # str | None 表示这个字段可以是字符串类型, 也可以是 None(空).
    # 如 description, deadline 可以为空; closed_at 也可以为空, 表示任务还未完成.
    # 请自行编写一个 starred 字段, 表示任务是否加星标, 类型为 bool.
    def __init__(self,
                 id:int,
                 title:str,
                 description:str | None,
                 deadline: datetime | None,
                 status: TaskStatus,
                 created_at: datetime,
                 closed_at: datetime | None,
                 starred : bool):

        self.id: int = id
        self.title: str = title
        self.description: str | None = description
        self.status: TaskStatus = status
        self.deadline: datetime | None = deadline
        self.created_at: datetime = created_at
        self.closed_at: datetime | None = closed_at
        self.starred : bool = starred
