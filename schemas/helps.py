from pydantic import BaseModel, Field

class FreeHelp(BaseModel):
    title: str
    description: str
    images: list[bytes] | None
    tags: list[str] | None
    duration: int = Field(ge=0, le=5)
