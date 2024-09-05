from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime
from uuid import UUID, uuid4
#

from database import Base
from main import app, get_db

#   //  User Functions
#
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#   //  Drug Functions
#
def list_drugs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Drug).offset(skip).limit(limit).all()

#   //  History Functions
#

def get_user_history(db: Session, user_id: str):
    return db.query(models.History).filter(models.History.user_id == user_id).first
#

#// yeah not done yet ayeeeee
def use_drug(db: Session, usage: schemas.HistoryCreate, user: int, route: str, dosage: str):
    db_history = models.History(**usage.model_dump(), id = uuid4(), user_id=user)
    db.add(db_history)
    db.commit()
    db.refresh(db_history)
    return db_history