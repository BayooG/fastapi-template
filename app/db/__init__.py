import os
from sqlmodel import create_engine, Session


class DB:
    def __init__(
        self,
        db_name: str,
        db_port: int,
        db_host: str,
        db_username: str,
        db_password: str,
        db_type: str = "postgres",
    ):
        self.db_url = (
            f"{db_type}://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
        )
        self.engine = create_engine(self.db_url)

    def __enter__(self):
        self.session = Session(self.engine)
        return self.session

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()


connection = DB(
    os.environ["DB_NAME"],
    int(os.environ["DB_PORT"]),
    os.environ["DB_HOST"],
    os.environ["DB_USERNAME"],
    os.environ["DB_PASSWORD"],
)
