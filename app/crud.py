# 数据库的四大基本操作为: 增(Create), 删(Delete), 改(Write), 查(Read). 取首字母缩写为 CRUD.
# 本项目虽不使用数据库, 但仍然涉及对文件的增删改查操作, 因此延续此命名.
# 本项目要引用 model 模块, 使用 os 等读写项目根目录下 data 目录的文件.
# 简单起见, 这里不需要实时读取, 而是定义一个 init 函数, 在应用启动时读取所有数据到内存中.
# 之后在对数据进行增删改查时, 直接操作内存中的数据, 并在每次修改后将数据写回文件.

# 这里你需要定义如下函数:
# init() -> None: 初始化函数, 读取 data 目录下的所有数据文件到内存中.
# create_task(task: Task) -> None: 创建任务, 注意 id 的分配.
# get_task(task_id: int) -> Task | None: 获取任务, 根据任务 id 从内存中获取任务, 找不到则返回 None.
# delete_task(task_id: int) -> None: 删除任务, 注意 id 不需要回收.
# update_task(task: Task) -> None: 更新任务, 根据任务 id 索引任务, 并更新其内容.
# 此外还有一个全局变量 data: List[Task], 用于存储所有任务数据.


from typing import List
from app.model import Task, TaskStatus
import json
from datetime import datetime
import os


data: List[Task] = []

def init():
    # 获取当前文件的绝对路径
    current_file = __file__
    # 获取当前文件所在目录（app包目录）
    current_dir = os.path.dirname(os.path.abspath(current_file))
    # 获取项目根目录（app的父目录）
    project_root = os.path.dirname(current_dir)
    # 构建data.json的完整路径
    data_path = os.path.join(project_root, 'data', 'data.json')
    try:
        with open(data_path, 'r', encoding='utf-8') as file:
            read_data = json.load(file)
            for read_task in read_data:
                data.append(Task(**read_task))
            for task in data:
                task.deadline = datetime.strptime(task.deadline, '%Y-%m-%d %H:%M')
                task.created_at = datetime.strptime(task.created_at, '%Y-%m-%d %H:%M')
                task.closed_at = datetime.strptime(task.closed_at, '%Y-%m-%d %H:%M')
                if task.status == "PENDING":
                    task.status = TaskStatus.PENDING
                elif task.status == "COMPLETED":
                    task.status = TaskStatus.COMPLETED
                elif task.status == "CANCELED":
                    task.status = TaskStatus.CANCELED
                elif task.status == "OVERDUE":
                    task.status = TaskStatus.OVERDUE
    except BaseException:
        return None

def create_task(task: Task):
    # 注意 id 的分配, 最简单的方法就是让 id = 1, 2, 3, ...
    # 但 data 任务数组是从文件读取的, 不能相信它的顺序, 因此需要遍历 data 找到最大的 id, 然后加 1 作为新任务的 id.
    """分配id"""
    if data :
        new_id = max(task.id for task in data) + 1
    else:
        new_id = 1
    try:
        task.id = new_id
        data.append(task)
    except BaseException:
        return None

def get_task(task_id: int) -> Task | None:
    for read_task in data:
        if read_task.id == task_id:
            return read_task
    return None


def delete_task(task_id: int):
    # 注意 id 的管理, 删除任务删除即可, 不需要更新其他任务的 id 来补充删除空缺.
    for read_task in data:
        if read_task.id == task_id:
            data.remove(read_task)

def update_task(task: Task):
    if task.status == TaskStatus.PENDING and task.deadline < datetime.now():
        task.status = TaskStatus.OVERDUE
    return None

def save_data():
    tasks = []
    for task in data:
        tasks.append({'id':task.id,
                      'title':task.title,
                      'description':task.description,
                      'deadline':task.deadline.strftime('%Y-%m-%d %H:%M'),
                      'status': task.status.name,
                      'created_at': task.created_at.strftime('%Y-%m-%d %H:%M'),
                      'closed_at': task.created_at.strftime('%Y-%m-%d %H:%M'),
                      'starred': task.starred})
        # 获取当前文件的绝对路径
        current_file = __file__
        # 获取当前文件所在目录（app包目录）
        current_dir = os.path.dirname(os.path.abspath(current_file))
        # 获取项目根目录（app的父目录）
        project_root = os.path.dirname(current_dir)
        # 构建data.json的完整路径
        data_path = os.path.join(project_root, 'data', 'data.json')
        with open(data_path, 'w+', encoding='utf-8') as file:
            json.dump(tasks, file, ensure_ascii=False, indent=4)