from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from app.database import Base

# Модель студента
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Group', back_populates='students')

# Модель группы
class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    students = relationship('Student', back_populates='group')

# Модель для создания студента
class StudentCreate(BaseModel):
    name: str
    group_id: int

# Модель для создания группы
class GroupCreate(BaseModel):
    name: str

# Модель для ответа с информацией о студенте
class StudentResponse(BaseModel):
    id: int
    name: str
    group_id: int

# Модель для ответа с информацией о группе
class GroupResponse(BaseModel):
    id: int
    name: str
    students: List[StudentResponse]

