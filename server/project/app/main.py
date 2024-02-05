from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.endpoints import router as apirouter
from .authentication.auth import router as authrouter
from .database import engine, Base


app = FastAPI()
app.include_router(apirouter)
app.include_router(authrouter, prefix="/auth", tags=["auth"])

# CORS settings
origins = [
    "http://localhost:5500",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Initialize the database tables
Base.metadata.create_all(bind=engine)
