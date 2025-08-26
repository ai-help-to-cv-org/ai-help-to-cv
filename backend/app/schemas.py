from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: Optional[str]
    email: EmailStr
    password: str
    field: Optional[str]

class UserOut(BaseModel):
    id: int
    name: Optional[str]
    email: EmailStr
    field: Optional[str]

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class GoogleLoginRequest(BaseModel):
    # dummy: gerçek uygulamada google token doğrulama yapılır
    email: EmailStr
