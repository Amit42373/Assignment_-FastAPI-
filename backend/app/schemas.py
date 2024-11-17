from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class PasswordRecovery(BaseModel):
    username_or_email: str
    old_password: str
    new_password: str