import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# create a model
class User(BaseModel):
    id: str
    user_name: str
    password: str
    active: bool

users = []

@app.get('/Users')
def get_user():
    return users

@app.post('/user')
def creat_user(user: User):
    users.append(user)
    return users

@app.put('/user/{id}')
def update_user(id: str, update_user: User):
    for idx, user in enumerate(users):
        if user.id == id:
            users[idx] = update_user
            return users
    return f'user id ${id} not found..!!'

@app.delete('/users/{id}')
def delete_user(id: str):
    global users
    users = [user for user in users if user.id != id]
    return users

if __name__ == '__main__':
    uvicorn.run(app, debug = True)