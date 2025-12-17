from fastapi import FastAPI
from app.database import engine
import app.models as models
from .routers import register


app = FastAPI()
# models.Base.metadata.drop_all(bind=engine)
# models.Base.metadata.create_all(bind=engine)

# Resgister User

app.include_router(register.router)