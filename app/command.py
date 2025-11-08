# 你要编写的是个命令行程序, 因此在这里控制输入输出.
# 这里要实现 app() 函数, 打印功能列表, 等待用户输入命令编号, 然后调用相应的功能函数.
# 注意: 不要在这里实现具体的功能函数, 这些函数应该在 controller.py 中实现.


# 分析你的需求, 大分类是筛选并展示任务列表, 展示单一任务, 操作单一任务, 创建任务.
# 因此可以在这里实现 show_task_list(tasks: List(Task)) 等函数.
# 至于具体的功能实现, 比如筛选星标任务, 应在 controller.py 中实现 get_starred_tasks() -> List(Task) 函数, 之后交给 show_task_list(tasks: List(Task)) 来展示.
# 简单来说, controller.py 操作数据, command.py 操作输入输出.

from typing import List

from app.crud import update_task, save_data, delete_task,get_task
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
title           status          starred         created_at          closed_at           deadline        description        id
""")
    print(
f"""
{task.title}        {task.status.value}        {task.starred}     {task.created_at.strftime('%Y-%m-%d %H:%M')}       {task.closed_at.strftime('%Y-%m-%d %H:%M')}       {task.deadline.strftime('%Y-%m-%d %H:%M')}      {task.description}        {task.id}
""")

def create_task():
    # 创建新任务
    # 注意这里只负责输入输出, 因此这里只进行引导用户输入各种信息.
    # 然后把信息传给 controller.py 的 create_task(...) 函数, 由它验证信息, 调用 crud.py 创建任务.
    print("--------create new task--------")
    title = input("title: ")
    deadline = input("deadline(example:2024-01-15 14:30): ")
    description = input("description: ")
    starred = input("starred: ")
    return title,deadline,description,eval(starred)

def edit_task(task: Task, title: str | None , deadline: datetime | None, description: str | None, starred: bool | None):
    # 编辑任务
        task.title = title
        task.deadline = deadline
        task.description = description
        task.starred = starred

def app():
    is_over = True
    while is_over:
        # 打印功能列表
        # 等待用户输入命令编号
        # 调用相应的功能函数
        print(
f"""
--------query--------
show all tasks(input 'show')
query starred task(input 'starred')
query completed task(input 'completed)
query newest task(input 'newest')
query task details(input the task id)
query pending task(input 'pending')
query overdue task(input 'overdue')
--------edit--------
create new task(input 'create')
edit task(input 'edit')
update task(input 'update')
--------exit--------
exit(input 'exit')
input:
""",end = ' ')
        ans = input()
        # 以查询星标任务为例:
        if ans == 'starred':
            tasks = get_starred_tasks()
            for date_task in tasks:
                update_task(date_task)
            show_task_list(tasks)
            
        # 一些其他的例子
        elif ans == 'completed':
            tasks = get_completed_tasks()
            for data_task in tasks:
                update_task(data_task)
            show_task_list(tasks)
            
        elif ans == 'newest':
            task = get_newest_task()
            update_task(task)
            show_task_detail(task)

        elif ans == 'create':
            task_info = create_task()
            create_task_info(*task_info)
            #更新任务以确保状态正确后再进行输出
            for data_task in data:
                update_task(data_task)
            show_task_list(data)
            save_data()

        elif ans == 'update':
            for task in data:
                update_task(task)
            show_task_list(data)
            save_data()

        elif ans == 'show':
            #先更新任务再进行输出以保证消息正确性
            for data_task in data:
                update_task(data_task)
            show_task_list(data)

        elif ans == 'exit':
            is_over = False

        elif ans == 'pending':
            tasks = get_pending_tasks()
            for data_task in tasks:
                update_task(data_task)
            show_task_list(tasks)

        elif ans == 'overdue':
            tasks = get_overdue_tasks()
            for data_task in tasks:
                update_task(data_task)
            show_task_list(tasks)

        elif ans == 'edit':
            edit_id = input("input the task id:")
            try:
                task = get_task(int(edit_id))
                print('----------edit task----------')
                title = input("new title: ")
                deadline = input("new deadline(example:2024-01-15 14:30): ")
                description = input("new description: ")
                starred = eval(input("new starred: "))
                deadline = datetime.strptime(deadline, '%Y-%m-%d %H:%M')
                edit_task(task, title, deadline,  description, starred)
                for data_task in data:
                    update_task(data_task)
                show_task_list(data)
                save_data()
            except BaseException as e:
                print(e)
                print('输入数据有误')
                continue

        else:
            try:
                input_id = eval(ans)
                task = get_task(input_id)
                #输出前记得先更新任务
                update_task(task)
                show_task_detail(task)
            except BaseException:
                print('id错误！')
                continue
            while True :
                print(
"""
edit task(input 'edit')
cancel the task(input 'cancel')
complete task(input 'complete')
delete the task(input 'delete')
return to the previous menu(input 'back')
starred task(input 'starred')
input:
""",end = ' ')
                ans = input()
                if ans == 'edit':
                    print('----------edit task----------')
                    title = input("new title: ")
                    deadline = input("new deadline(example:2024-01-15 14:30): ")
                    description = input("new description: ")
                    starred = eval(input("new starred: "))
                    deadline = datetime.strptime(deadline, '%Y-%m-%d %H:%M')
                    edit_task(task, title, deadline, description, starred)
                    save_data()
                    show_task_detail(task)
                elif ans == 'cancel':
                    task.status = TaskStatus.CANCELED
                    #更新任务
                    for data_task in data:
                        update_task(data_task)
                    save_data()
                    show_task_detail(task)
                elif ans == 'complete':
                    task.status = TaskStatus.COMPLETED
                    #更新任务
                    for data_task in data:
                        update_task(data_task)
                    save_data()
                    show_task_detail(task)
                elif ans == 'delete':
                    delete_task(input_id)
                    save_data()
                    break
                elif ans == 'back':
                    task.closed_at = datetime.now()
                    break
                elif ans == 'starred':
                    if task.starred:
                        print('This task has been starred!')
                    else:
                        task.starred = False
                        update_task(task)
                        save_data()
                        show_task_detail(task)
                else:
                    print('命令有误！')


        # 退出程序
        if not is_over:
            # 将内存中的数据写入data.json
            save_data()
            break


