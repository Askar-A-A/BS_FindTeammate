from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.endpoints import router 
from .database import engine, Base


app = FastAPI()
app.include_router(router)

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
