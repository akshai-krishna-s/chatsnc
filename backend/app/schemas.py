from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from llama_index.llms import MessageRole
from typing import List


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserOut


class TokenData(BaseModel):
    id: Optional[int] = None


class ChatCreateOut(BaseModel):
    id: int

    class Config:
        from_attributes = True


class ChatOut(BaseModel):
    id: int
    history: Optional[List]
    created_at: datetime

    class Config:
        from_attributes = True


class History(BaseModel):
    role: MessageRole
    content: str


class HistoryOut(BaseModel):
    role: str
    content: str
