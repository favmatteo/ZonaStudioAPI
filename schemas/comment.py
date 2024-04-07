from pydantic import BaseModel, Field


class Comment(BaseModel):
    text: str
    id_free_post: int | None = None
    id_payment_post: int | None = None
