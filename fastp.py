from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

# Маршрут с валидацией user_id
@app.get("/user/{user_id}")
def get_user_by_id(
    user_id: Annotated[
        int, Path(gt=0, le=100, description="Enter User ID", example=1)
    ]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Маршрут с валидацией username и age
@app.get("/user/{username}/{age}")
def get_user_info(
    username: Annotated[
        str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")
    ],
    age: Annotated[
        int, Path(ge=18, le=120, description="Enter age", example=24)
    ]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

# Главная страница
@app.get("/")
def main_page():
    return {"message": "Главная страница"}

# Маршрут администратора
@app.get("/user/admin")
def admin_page():
    return {"message": "Вы вошли как администратор"}