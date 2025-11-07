# 这里实现所有函数的具体功能.

from typing import List
from app.model import Task, TaskStatus
from app.crud import data
from app.filter import Filter, Order
from datetime import datetime
from app.crud import create_task as ct

# 以查询星标任务为例.
def get_starred_tasks() -> List[Task]:
    # 从数据库获取所有星标任务
    # 因为我们已经实现了数据加载方法和筛选方法, 因此具体操作时不需要关注过程.
    # 此外, 虽然未要求, 但我们应该按创建时间降序排列星标任务, 以便最新的任务排在最前面.
    return Filter(data).by_starred(True).order_by_create(Order.DESC).all()


# 此外, 如果命名足够清晰, 可以不写注释来说明功能
def get_completed_tasks() -> List[Task]:
    return Filter(data).by_status(TaskStatus.COMPLETED).order_by_create(Order.DESC).all()


def get_newest_task() -> Task | None:
    return Filter(data).order_by_create(Order.DESC).first()

#验证数据
def create_task_info(title: str, deadline: str, description: str, starred: bool):
    try:
        datetime.strptime(deadline, "%Y-%m-%d %H:%M")
    except BaseException:
        print('deadline格式有误！')
        return None
    if starred != True and starred != False:
        raise TypeError("starred请输入'False' or 'True'")
    else:
        task = Task(id = 0,
             title = title,
             description = description,
             deadline = datetime.strptime(deadline, "%Y-%m-%d %H:%M"),
             status = TaskStatus.PENDING,
             created_at = datetime.now(),
             closed_at = None,
             starred = starred)
        ct(task)
        return None

