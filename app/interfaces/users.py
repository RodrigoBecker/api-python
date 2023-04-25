from typing import List

from pydantic import BaseModel, Field


class UsersOutput(BaseModel):
    name: str
    last_name: str
    cpf: str
    identity_register: str
    age: int
    birthdate: str
    mother_name: str
    email: str


class UsersListOutPut(BaseModel):
    users: List[UsersOutput] = Field(default_factory=list)


class UserCreateInput(BaseModel):
    name: str
    last_name: str
    cpf: str
    identity_register: str
    age: int
    birthdate: str
    mother_name: str
    email: str


class UserCreateOutput(BaseModel):
    message: str


class UserDeletedOutput(BaseModel):
    message: str
