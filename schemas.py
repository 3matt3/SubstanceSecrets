from pydantic import BaseModel
from typing import Optional
from typing import List

# // History

class HistoryBase(BaseModel):
    drug: str

class HistoryCreate(HistoryBase):
    dose: str
    roa: str

class History(HistoryBase):
    id: int
    user_id: int
    user: str
    datetime: str

    class Config:
        orm_mode=True

# // Drugs

class DrugBase(BaseModel):
    name: str

class DrugCreate(DrugBase):
    pass

class Drug(DrugBase):
    id: int
    description: str
    duration: str
    dosages: str

    class Config:
        orm_mode=True

# // Users

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id = int
    usage: list[History] = []
    is_active = bool

    class Config:
        orm_mode=True