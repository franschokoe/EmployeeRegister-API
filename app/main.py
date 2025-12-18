from fastapi import FastAPI , status
from app.database import engine
import app.models as models
from .routers import register , role


app = FastAPI()
# models.Base.metadata.drop_all(bind=engine)
# models.Base.metadata.create_all(bind=engine)
@app.get("/" , status_code= status.HTTP_202_ACCEPTED)
async def root():
    return {"msg" : "success"}

# Resgister User
app.include_router(register.router)

# Role router
app.include_router(role.router)