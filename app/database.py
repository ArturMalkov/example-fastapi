from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}" \
                          f"@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(database="blogposts", user="postgres", password="Kleopatra2003!", host="localhost",
#                                 port="5433", cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection established")
#         break
#     except Exception as err:
#         print("Connecting to database failed")
#         print(f"Error: {err}")
#         time.sleep(2)
