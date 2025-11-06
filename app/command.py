# 你要编写的是个命令行程序, 因此在这里控制输入输出.
# 这里要实现 app() 函数, 打印功能列表, 等待用户输入命令编号, 然后调用相应的功能函数.
# 注意: 不要在这里实现具体的功能函数, 这些函数应该在 controller.py 中实现.


# 分析你的需求, 大分类是筛选并展示任务列表, 展示单一任务, 操作单一任务, 创建任务.
# 因此可以在这里实现 show_task_list(tasks: List(Task)) 等函数.
# 至于具体的功能实现, 比如筛选星标任务, 应在 controller.py 中实现 get_starred_tasks() -> List(Task) 函数, 之后交给 show_task_list(tasks: List(Task)) 来展示.
# 简单来说, controller.py 操作数据, command.py 操作输入输出.

from typing import List

from app.crud import update_task, save_data, delete_task
from app.model import Task
from app.controller import *

def show_task_list(tasks: List[Task]):
    # 打印任务列表
    print(
"""
title          status             starred        id
""")
    for task in tasks:
        print(
f"""
{task.title}            {task.status.value}            {task.starred}             {task.id}
""")

def show_task_detail(task: Task):
    # 打印单一任务详情
    print(
"""
title           status          starred         created_at          closed_at           deadline        description
""")
    print(
f"""
{task.title}        {task.status.value}        {task.starred}     {task.created_at.strftime('%Y-%m-%d %H:%M')}       {task.closed_at.strftime('%Y-%m-%d %H:%M')}       {task.deadline.strftime('%Y-%m-%d %H:%M')}      {task.description}
""")

def create_task():
    # 创建新任务
    # 注意这里只负责输入输出, 因此这里只进行引导用户输入各种信息.
    # 然后把信息传给 controller.py 的 create_task(...) 函数, 由它验证信息, 调用 crud.py 创建任务.
    print("create new task")
    title = input("title: ")
    deadline = input("deadline(example:2024-01-15 14:30): ")
    description = input("description: ")
    starred = input("starred: ")
    return title,deadline,description,eval(starred)

def edit_task(task: Task, title: str | None , deadline: datetime | None, status : TaskStatus | None , description: str | None, starred: bool | None):
    # 编辑任务
    if title is str:
        task.title = title
    if deadline is datetime:
        task.deadline = deadline
    if status is str:
        task.status = status
    if description is str:
        task.description = description
    if starred is bool:
        task.starred = starred

def app():
    is_over = True
    while is_over:
        # 打印功能列表
        # 等待用户输入命令编号
        # 调用相应的功能函数
        ans = input(
"""
show all tasks(input 'show')
create new task(input 'create')
query starred task(input 'starred')
query completed task(input 'completed)
query newest task(input 'newest')
query task details(input the task id)
update task(input 'update')
exit(press 0)
input:
""")
        # 以查询星标任务为例:
        if ans == 'starred':
            tasks = get_starred_tasks()
            show_task_list(tasks)
            
        # 一些其他的例子
        if ans == 'completed':
            tasks = get_completed_tasks()
            show_task_list(tasks)
            
        if ans == 'newest':
            task = get_newest_task()
            show_task_detail(task)

        if ans == 'create':
            task_info = create_task()
            create_task_info(*task_info)
            show_task_list(data)
            save_data()

        if ans == 'update':
            for task in data:
                update_task(task)
            show_task_list(data)

        if ans == 'show':
            show_task_list(data)

        if ans == '0':
            is_over = False
        # 退出程序
        if not is_over:
            break


#将内存中的数据写入data.json
save_data()