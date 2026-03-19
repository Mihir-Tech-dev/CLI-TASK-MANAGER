from dataclasses import dataclass, field
from datetime import datetime
@dataclass
class Task:
    title:str
    id:int = field(default=0)
    status:str = field(default="todo")
    priority:str = field(default="medium")
    created_at:datetime =field(default_factory= datetime.now)