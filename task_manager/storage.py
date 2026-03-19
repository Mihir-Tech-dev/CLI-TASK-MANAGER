import json
from task_manager.models import Task
from datetime import datetime

def task_to_dict(task: Task) -> dict:
    return{
        "id": task.id,
        "title": task.title,
        "status":task.status,
        "priority":task.priority,
        "created_at":task.created_at.isoformat()
    }

def dict_to_task(data: dict) -> Task:
    return Task(
        id = data["id"],
        title=data["title"],
        status=data["status"],
        priority=data["priority"],
        created_at=datetime.fromisoformat(data["created_at"])
    )

def save(tasks:list[Task]) -> None:
    data = [task_to_dict(task) for task in tasks]
    with open("store.json", "w") as f:
        json.dump(data, f, indent=2)

def load() -> list[Task]:
    try:
        with open("store.json", "r") as f:
            data = json.load(f)
            return [dict_to_task(d) for d in data]
    except FileNotFoundError:
        return []