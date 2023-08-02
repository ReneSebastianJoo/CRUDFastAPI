from fastapi import APIRouter, HTTPException, Depends, status, Request
from fastapi.responses import HTMLResponse, FileResponse  
from typing import Annotated
from sqlalchemy.orm import Session
from database import sessionLocal
from models.user import User
from schemas.Usuario import Usuario
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


user = APIRouter(prefix="/users",
                   tags=["users"],
                   responses={404:{"description":"Not found"}})

# Archivos estaticos y plantillas
user.mount("/static", StaticFiles(directory="static"), name="static")
template = Jinja2Templates(directory="./templates")

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@user.get("/all", status_code=status.HTTP_200_OK)
async def get_users(db: db_dependency):
    data = db.query(User).all()
    return data

@user.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: int, db: db_dependency):
    user =db.query(User).filter(User.id ==user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user.get("/usersmail/{emailUsuario}", status_code=status.HTTP_200_OK)
async def get_user_by_email(emailUsuario: str, db: db_dependency):
    user =db.query(User).filter(User.email == emailUsuario).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user.post("/",status_code=status.HTTP_201_CREATED)
async def create_user (user: Usuario, db: db_dependency):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()

@user.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, db: db_dependency):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    print ("El usuario con el id{user_id} ha sido eliminado")
    return {"status": "success", "note": "{user_id}"}
    
# Arreglar esto ya que no es util
@user.put("/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_id: int, user: Usuario, db: db_dependency):
    user_update = db.query(User).filter(User.id == user_id)
    updt = user_update.first()
    if updt is None:
        raise HTTPException(status_code=404, detail="User not found")
    update_data = user
    user_update.filter(User.id == user_id).update(update_data)
    db.commit()
    return {"status": "success", "note": updt}


@user.get("/", response_class=HTMLResponse)
def raiz(request: Request):
    return template.TemplateResponse("usuarios.html",{'request': request}, status_code=200)


