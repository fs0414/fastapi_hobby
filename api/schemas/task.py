from typing import Optional

from pydantic import BaseModel, Field

class Task(BaseModel):
    id: int
    title: Optional[str] = Field(None, example='task01')
    done: bool = Field(Field, description='完了フラグ')