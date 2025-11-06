# 单有四大基本操作还不够, 这里要定义一些筛选(过滤)函数.

# 这里先讲解一下 "链式调用" 的概念.
# 如果一个类 A 下定义了方法 foo1, foo2, 此外 foo1 和 foo2 的返回值都是类 A, 如下:
# class A:
#     def foo1(self):
#         ...
#         return self
# 
#     def foo2(self):
#         ...
#         return self
# 那么既然 A.foo1() 返回的还是 A, A 又有 foo2() 方法, 那么就可以进行链式调用:
# A.foo1().foo2()
# 这就是链式调用的概念.

# 下面定义一个 Filter 类, 并定义各种筛选方法, 每个方法都返回 self, 以支持链式调用.
# 这样可以写出如下代码:
# Filter(data).by_status(TaskStatus.PENDING).by_starred(True).order(date).first()
# 表示先筛选出待处理任务, 再从中筛选出加星标的任务, 然后按日期排序, 最后取第一个任务.
# 这些函数中, by_status(), by_starred(), order() 都要返回 Filter.
# 最后一个函数 first() 才返回 Task 示例或空(None).

# 你的 Filter 类要定义如下函数, 简单起见, 我们不实现那么多功能..
# __init__(): 构造函数, 接收一个任务列表作为参数.
# by_status(status: TaskStatus) -> Filter: 按状态筛选任务.
# by_starred(starred: bool) -> Filter: 按是否加星标筛选任务.
# order_by_create(order: Order) -> Filter: 按创建时间排序任务, 支持升序降序两种方式.
# order_by_deadline(order: Order) -> Filter: 按截止时间排序任务, 支持升序降序两种方式.
# first() -> Task | None: 取第一个任务, 如果没有任务则返回 None.
# all() -> List[Task]: 取所有任务, 返回任务列表.
# 注意: 前面几个函数都返回 Filter, 以支持链式调用; first() 和 all() 才返回具体的任务或任务列表, 因此它们放在链式调用的最后.


from enum import Enum
from typing import List
from app.model import Task, TaskStatus


class Order(Enum):
    ASC = "升序"
    DESC = "降序"


class Filter:
    def __init__(self, task_list: List[Task]):
        self.task_list = task_list
    
    def by_status(self, status: TaskStatus):
        select_tasks = []
        for task in self.task_list:
            if task.status == status:
                select_tasks.append(task)
            self.task_list = select_tasks
        return self
    
    def by_starred(self, starred: bool):
        select_tasks = []
        for task in self.task_list:
            if task.starred == starred:
                select_tasks.append(task)
            self.task_list = select_tasks
        return self
    
    def order_by_create(self, order: Order):
        if order == Order.ASC:
            self.task_list.sort(key=lambda task: task.created_at, reverse=False)
        elif order == Order.DESC:
            self.task_list.sort(key=lambda task: task.created_at, reverse=True)
        return self
    
    def order_by_deadline(self, order: Order):
        if order == Order.ASC:
            self.task_list.sort(key=lambda task: task.deadline, reverse=False)
        elif order == Order.DESC:
            self.task_list.sort(key=lambda task: task.deadline, reverse=True)
        return self
    
    def first(self) -> Task | None:
        if self.task_list:
            return self.task_list[0]
        else:
            return None
    
    def all(self) -> List[Task]:
        return self.task_list
