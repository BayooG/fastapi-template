from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

import os

#routes
from app.api.v1.endpoints.users import router as UserRouter

# we don't need those in docker mode
# from dotenv import load_dotenv
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# load_dotenv(os.path.join(BASE_DIR, ".env"))

def configure_app(app):
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_DATABASE = os.getenv("DB_DATABASE")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    
    DATABASE_URL= f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
    print('url', DATABASE_URL)
    app.add_middleware(DBSessionMiddleware, db_url=DATABASE_URL)

def initialize_app(app):
    configure_app(app)
    app.include_router(UserRouter)

app = FastAPI(title="Second Opinion API",
              debug=os.getenv("DEBUG"),
              description='get a second opinion: a dental consultation community',
              )
initialize_app(app)

if __name__ == "__main__":
     # Load cli commands
    from app.cli import app as cli

    cli()