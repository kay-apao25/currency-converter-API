import requests

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from format import PrettyJSONResponse
from utils import users_db, UserInDB, hash_password, oauth2_scheme


app = FastAPI()
BASE_URL = "https://api.apilayer.com/fixer/"
headers = {
    "apikey": "xggalLmg5MtbIjyKsb5IePqLcC41SNny"
}


''' Authentication endpoints '''

@app.get("/token")
async def fetch_bearer_token(token: str = Depends(oauth2_scheme)):
    ''' Returns available authorized token '''
    return {"token": token}

@app.post("/login")
async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    ''' Facilitates user login '''
    users = users_db.get(form_data.username)
    if not users:
        raise HTTPException(status_code=400, detail="User does not exist")
    user = UserInDB(**users)
    hashed_password = hash_password(form_data.password)
    if hashed_password != user.hashed_password:
        raise HTTPException(status_code=400, detail="Username or password does not match")

    return {"access_token": user.username, "token_type": "bearer"}


''' Currency Converter API endpoints '''

@app.get("/list_currencies", response_class=PrettyJSONResponse)
async def get_supported_currencies(_: str = Depends(oauth2_scheme)):
    ''' Returns list of supported currencies '''
    url = f"{BASE_URL}symbols"
    return requests.get(url, headers=headers).json()["symbols"]


@app.get("/convert", response_class=PrettyJSONResponse)
async def convert_currencies(from_currency: str, to_currency: str, amount: float, date: str = None, _: str = Depends(oauth2_scheme)):
    ''' Facilitates converting of a certain amount from specified from and to currencies '''
    url = f"{BASE_URL}convert?to={to_currency.upper()}&from={from_currency.upper()}&amount={amount}"
    if date:
        url = f"{url}&date={date}"
    return requests.get(url, headers=headers).json()
