from pydantic import BaseModel, Field


class FreeHelp(BaseModel):
    title: str
    description: str
    tags: list[str] | None
    id_student: str | None
