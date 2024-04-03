from pydantic import BaseModel, Field, EmailStr

class TokenData(BaseModel):
    token: str