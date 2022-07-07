# Currency Converter API Coding Task

### A simple currency converter API implemented using FastAPI with the following main endpoints:

1.) /list_currencies = API endpoint for fetching the list all supported currencies.

2.) /convert/ = currency convert API endpoint

### And sub API endpoints

1.) /login = API endpoint for user login

2.) /token = API endpoint for a user to retrieve available tokens.

### First steps, run the following commands in order:

```
python -m venv env
pip install -r requirements.txt
```

### To start the app:

`uvicorn main:app --reload`

### Before using the currency converter API's, access /login endpoint and use these credentials:

```
username: admin
password: root
```

#### Upon accessing the currency converter API's, do not forgot to set the Auth bearer token (which is provided after login)

#### API documentation: http://localhost:8000/docs
