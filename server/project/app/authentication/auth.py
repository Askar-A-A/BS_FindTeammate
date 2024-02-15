from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlalchemy.orm import Session
from ..models.models import User  
from ..database import get_db  
from .hashing import get_hashed_password 
from ..models.schemas import UserOut  
from .hashing import verify_password
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/signup", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def register_user(
    username: str = Form(...), 
    email: str = Form(...), 
    password: str = Form(...), 
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email is already in use")
               
    hashed_password = get_hashed_password(password)
    new_user = User(username=username, email=email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    # Redirect to the main page (or any other page) after successful registration
    response = JSONResponse(content={"message": "Registration successful"},
                            headers={"HX-Redirect": "http://127.0.0.1:5500/client/index.html"})
    return response


@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    response = JSONResponse(content={"message": "Login successful", "username": user.username}, headers={"HX-Redirect": "http://127.0.0.1:5500/client/index.html"})
    return response

