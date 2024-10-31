from fastapi import Depends, HTTPException, status
from jose import jwt, JWSError
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from models import User
from database import sessionLocal


Secret_key = "sourceCode"
Algorithm = "HS256"
Access_Token_Expire_Min = 30

pwd_context=  CryptContext(schemes=["bcrypt"], deprecated = "auto" )

def verify_password(plain_password, hash_password):
    return pwd_context.verify(plain_password, hash_password)

def get_pass_hash(password):
    return pwd_context.hash(password)

def create_access_token( data: dict, expire_delta: timedelta = timedelta(minutes=15)):
    to_encode = data.copy()
    expire  = datetime.now(timezone.utc) + expire_delta
    to_encode.update({"exp" : expire})
    return jwt.encode(to_encode, Secret_key, algorithm=Algorithm)

def get_user_by_username(db:Session, username:str):
    return db.query(User).filter(User.username == username).first()