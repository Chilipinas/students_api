from fastapi import APIRouter, HTTPException
from app.database import SessionLocal, engine
from app.models import Student, Group, StudentCreate, GroupCreate, StudentResponse, GroupResponse

router = APIRouter()

# API эндпоинт для создания студента
@router.post("/students/")
def create_student(student: StudentCreate):
    db = SessionLocal()
    db_student = Student(name=student.name, group_id=student.group_id)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"id": db_student.id, "name": db_student.name, "group_id": db_student.group_id}

# API эндпоинт для создания группы
@router.post("/groups/")
def create_group(group: GroupCreate):
    db = SessionLocal()
    db_group = Group(name=group.name)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return {"id": db_group.id, "name": db_group.name}

# API эндпоинт для получения информации о студенте по его id
@router.get("/students/{student_id}")
def get_student(student_id: int):
    db = SessionLocal()
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"id": student.id, "name": student.name, "group_id": student.group_id}

# API эндпоинт для получения информации о группе по ее id
@router.get("/groups/{group_id}")
def get_group(group_id: int):
    db = SessionLocal()
    group = db.query(Group).filter(Group.id == group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return {"id": group.id, "name": group.name}

# API эндпоинт для удаления студента
@router.delete("/students/{student_id}")
def delete_student(student_id: int):
    db = SessionLocal()
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message": "Student deleted"}

# API эндпоинт для удаления группы
@router.delete("/groups/{group_id}")
def delete_group(group_id: int):
    db = SessionLocal()
    group = db.query(Group).filter(Group.id == group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    db.delete(group)
    db.commit()
    return {"message": "Group deleted"}

# API эндпоинт для получения списка студентов
@router.get("/students/")
def get_students():
    db = SessionLocal()
    students = db.query(Student).all()
    return students

# API эндпоинт для получения списка групп
@router.get("/groups/")
def get_groups():
    db = SessionLocal()
    groups = db.query(Group).all()
    return groups

# API эндпоинт для добавления студента в группу
@router.post("/groups/{group_id}/students/{student_id}")
def add_student_to_group(group_id: int, student_id: int):
    db = SessionLocal()
    group = db.query(Group).filter(Group.id == group_id).first()
    student = db.query(Student).filter(Student.id == student_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student.group_id = group_id
    db.commit()
    return {"message": "Student added to group"}

# API эндпоинт для удаления студента из группы
@router.delete("/groups/{group_id}/students/{student_id}")
def remove_student_from_group(group_id: int, student_id: int):
    db = SessionLocal()
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student.group_id = None
    db.commit()
    return {"message": "Student removed from group"}

# API эндпоинт для получения всех студентов в группе
@router.get("/groups/{group_id}/students/")
def get_students_in_group(group_id: int):
    db = SessionLocal()
    group = db.query(Group).filter(Group.id == group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    students = group.students
    return students

# API эндпоинт для перевода студента из группы A в группу B
@router.put("/students/{student_id}/move/{group_id}")
def move_student(student_id: int, group_id: int):
    db = SessionLocal()
    student = db.query(Student).filter(Student.id == student_id).first()
    group = db.query(Group).filter(Group.id == group_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    student.group_id = group_id
    db.commit()
    return {"message": "Student moved to another group"}