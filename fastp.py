from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import List, Annotated

app = FastAPI()

# Список пользователей
users: List[BaseModel] = []

# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int

# GET запрос: получение всех пользователей
@app.get("/users")
def get_users():
    return users

# POST запрос: добавление нового пользователя
@app.post("/user/{username}/{age}")
def add_user(
    username: Annotated[
        str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")
    ],
    age: Annotated[
        int, Path(ge=18, le=120, description="Enter age", example=24)
    ]
):
    user_id = users[-1].id + 1 if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user

# PUT запрос: обновление пользователя
@app.put("/user/{user_id}/{username}/{age}")
def update_user(
    user_id: Annotated[
        int, Path(gt=0, description="Enter User ID", example=1)
    ],
    username: Annotated[
        str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanProfi")
    ],
    age: Annotated[
        int, Path(ge=18, le=120, description="Enter age", example=28)
    ]
):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

# DELETE запрос: удаление пользователя
@app.delete("/user/{user_id}")
def delete_user(
    user_id: Annotated[
        int, Path(gt=0, description="Enter User ID", example=1)
    ]
):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")

# Пример начальных маршрутов (без изменений)
@app.get("/")
def main_page():
    return {"message": "Главная страница"}

@app.get("/user/admin")
def admin_page():
    return {"message": "Вы вошли как администратор"}
