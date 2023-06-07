from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Подключение к базе данных
SQLALCHEMY_DATABASE_URL = "postgresql://<db_user>:<db_password>@<db_host>:5432/<db_name>"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


