from pydantic import BaseModel, Field, EmailStr
from enum import Enum


class EducationalLevel(str, Enum):
    MIDDLE_SCHOOL = "medie"
    HIGH_SCHOOL = "superiori"
    ITS = "its"
    BACHELOR_DEGREE = "triennale"
    MASTER_DEGREE = "magistrale"
    OTHER = "altro"


class HelperSignup(BaseModel):
    """
    Schema used to register new helper
    """

    name: str = Field(title="Helpers's name", max_length=20)
    surname: str = Field(title="Helpers's name", max_length=20)
    username: str = Field(title="Helpers's name", max_length=30)
    email: EmailStr = Field(title="Helpers's email", max_length=120)
    password: str = Field(title="Helpers's password", min_length=8)
    age: int = Field(title="Helpers's age", ge=14)
    school_address: str | None = Field(title="Helpers's school address")
    school_class: int | None = Field(title="Helpers's school class", ge=1, le=5)
    educational_level: EducationalLevel = Field(title="Educational level")


class HelperEmail(BaseModel):
    email: EmailStr = Field(title="Helpers's email", max_length=120)
