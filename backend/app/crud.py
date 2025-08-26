from sqlalchemy.orm import Session
from . import models, schemas
from .core import security

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed = security.get_password_hash(user.password) if user.password else None
    db_user = models.User(name=user.name, email=user.email, hashed_password=hashed, field=user.field)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not user.hashed_password:
        return None
    if not security.verify_password(password, user.hashed_password):
        return None
    return user
