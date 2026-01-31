from fastapi import FastAPI
from core.config import Settings
from db.session import engine
from db.base_class import Base

def create_tables():
    Base.metadata.create_all(bind=engine)
#everytime any module that will inherit the base class they will be auto created on out app is starting up

def start_application():
    app = FastAPI(title=Settings.PROJECT_TITLE,version=Settings.PROJECT_VERSION)
    create_tables()
    return app

app = start_application()

@app.get("/")
def hello():
    return {"msg" : "Hello FastAPI"} 