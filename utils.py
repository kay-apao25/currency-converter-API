from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# Default user
users_db = {
    "admin": {
        "username": "admin",
        "hashed_password": "secretroot",
    },
}

def hash_password(password: str):
    ''' Used to check user password '''
    return "secret" + password


class User(BaseModel):
    username: str


class UserInDB(User):
    hashed_password: str
