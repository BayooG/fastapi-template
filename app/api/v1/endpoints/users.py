from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi_sqlalchemy import db

from app.schema import UserIn, UserOut
from app.models import User as ModelUser
from app.api.v1.business import cerate_user, get_user_by_id, update_user, delete_user

router = APIRouter(
    prefix="/users",
)


@router.get("/", tags=["users"],)
def get_all_users():
    users = db.session.query(ModelUser).all()
    return users

@router.get("/{user_id}", tags=["users"],
            status_code=status.HTTP_200_OK,
            response_model=UserOut)
def get_user(user_id):
    return get_user_by_id(user_id)

@router.post("/", tags=["users"],
            response_model=UserOut,
            status_code=status.HTTP_201_CREATED,)
def post_user(user: UserIn):
    return cerate_user(user)

@router.put("/{user_id}",tags=["users"],
            response_model=UserOut,)
def update(user_id, user :UserIn):
    user = update_user(user_id, user)
    if user:
        return user
    else: 
        return JSONResponse(status_code = status.HTTP_404_NOT_FOUND,
                            content={"message": "User not found"})

@router.delete("/{user_id}", tags=["users"],
            status_code=status.HTTP_204_NO_CONTENT,)
def delete(user_id):
    state =  delete_user(user_id)
    if not state:
        return JSONResponse(status_code = status.HTTP_404_NOT_FOUND,
                            content={"message": "User not found"})

    
