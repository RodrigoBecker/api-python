from pydantic import BaseModel


class UsersOutput(BaseModel):
    name: str
    last_name: str
    cpf: str
    identity_register: str
    age: int
    birthdate: str
    mother_name: str
    email: str


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
