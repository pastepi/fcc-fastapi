from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, EmailStr


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserBase(BaseModel):
    id: int
    email: EmailStr


class UserResponse(UserBase):
    created_at: datetime
    posts: list[PostBase] = []

    class Config:
        from_attributes = True


class PostResponse(PostBase):
    id: int
    created_at: datetime
    user_id: int
    user: UserBase

    class Config:
        from_attributes = True


class PostVotesResponse(PostResponse):
    votes: int


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


class Vote(BaseModel):
    post_id: int
    dir: Literal[0, 1]
