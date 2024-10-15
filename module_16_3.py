from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_users():
    return users


@app.post('/user/{username}/{age}')
async def post_user(username: str = Path(min_length=1, max_length=50, description='Enter your name', example='1'),
                    age: int = Path(ge=18, le=80, description='Enter age', example='24')):
    current = str(int(max(users, key=int)) + 1)
    users[current] = f'Имя: {username}, возраст: {age}'
    return f'User {current} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int = Path(ge=0, le=100),
                      username: str = Path(min_length=1, max_length=50, description='Enter '
                                                                                    'name '
                                                                                    'for update'),
                      age: int = Path(ge=18, le=80)):
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is registered'


@app.delete('/user/{user_id}')
async def delete_user(user_id: str = Path(min_length=1, max_length=3)):
    users.pop(user_id)
    return f'User {user_id} has been deleted'
