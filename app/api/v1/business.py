from app.schema import UserIn
from app.models import User as ModelUser 

from fastapi_sqlalchemy import db


def cerate_user(user: UserIn):
    db_user = ModelUser(
        first_name=user.first_name, last_name=user.last_name, age=user.age
    )
    db.session.add(db_user)
    db.session.commit()
    return db_user

def get_user_by_id(user_id: int): #should change to uuid
    return db.session.query(ModelUser).filter_by(id=user_id).first()

def update_user(user_id, UserIn):
    user = get_user_by_id(user_id)
    if user:
        user.first_name = UserIn.first_name if UserIn.first_name else user.first_name
        user.last_name = UserIn.last_name if UserIn.last_name else user.last_name
        user.age = UserIn.age if UserIn.age else user.age
        
        db.session.add(user)
        db.session.commit()
        return user
        
def delete_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True

