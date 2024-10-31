from sqlalchemy.orm import Session  
from models import User, Project, Task
from schemas import UserCreate, ProjectCreate, TaskCreate
from auth import get_pass_hash


def create_user(db:Session, user: UserCreate):
    hashed_password = get_pass_hash(user.password)
    db_user = User(user = user.username, hashed_password = hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_project(db:Session, project: ProjectCreate):
    db_project = Project(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def create_task( db: Session, task : TaskCreate, owner_id : int, project_id : int):
    db_task = Task(**task.model_dump(), owner_id = owner_id, project_id = project_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task