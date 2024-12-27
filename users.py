from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

#entidad user
class User(BaseModel):
    id:int
    name:str
    surname:str
    url:str
    age:int

users_list = [
    User(id = 1,name = "Celeste",surname="Cobix",url="Te amo",age=20),
    User(id = 2,name = "Carlo",surname="Cabrera",url="Amo a mi novia",age=20),
    User(id = 3,name = "Sparky",surname="Cobix",url="Amo a mi dueño",age=20)
]
@app.get("/usersjson")
async def usersjson():
    return [{"name":"Celeste","surname":"Cobix","url":"Te amo","age":20},
            {"name":"Carlo","surname":"Cabrera","url":"Amo a mi novia","age":20},
            {"name":"Sparky","surname":"Cabrera","url":"Amo a mi dueño","age":10}]

@app.get("/users")
async def users():
    return users_list

#PATH(Parametros)
@app.get("/users/{id}")
async def user(id:int):
    return search_user(id)


#QUERY(Parametros)
@app.get("/userquery/")
async def user(id: int):
    return search_user(id)


def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "user not found"}

