from task_manager.models import Task
from task_manager.storage import load, save
from typing import Optional
class TaskManager:
    tasks:list[Task]

    def __init__(self):
        try:
            self.tasks=load()
        except:
            self.tasks=[]
            print("no tasks")

    def add(self,title: str,priority:str):
        task=Task(
            title=title,
            id=max((task.id for task in self.tasks), default=0) + 1,
            priority=priority
        )
        self.tasks.append(task)
        save(self.tasks)

    def delete(self,id: int):
        self.tasks = [task for task in self.tasks if task.id != id]
        save(self.tasks)

    def complete(self, id:int):
        for task in self.tasks:
            if task.id == id:
                task.status = "done"
        save(self.tasks)

    def list_task(self,filter:Optional[str]) -> list[Task]:
        if filter:
            for task in self.tasks:
                if task.status == filter:
                  print(f"#{task.id} [{task.priority}] {task.title} - {task.status}     ({task.created_at})")
        else:
          for task in self.tasks:
            print(f"#{task.id} [{task.priority}] {task.title} - {task.status}     ({task.created_at})")
