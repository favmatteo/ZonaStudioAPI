from pydantic import BaseModel, Field


class Student(BaseModel):
    """
    Schema used to register new student
    """

    name: str = Field(title="Student's name", max_length=20)
    surname: str = Field(title="Student's name", max_length=20)
    username: str = Field(title="Student's name", max_length=30)
    email: str = Field(title="Student's email", max_length=120)
    password: str = Field(title="Student's password", min_length=8)
    age: int = Field(title="Student's age", ge=14)
    school_address: str = Field(title="Student's school address")
    school_class: int = Field(title="Student's school class", ge=1, le=5)
