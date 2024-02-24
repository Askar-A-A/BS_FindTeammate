from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status, Form, Response
from sqlalchemy.orm import Session
from ..database import get_db  
from .utils import *
from fastapi.responses import JSONResponse
from ..models.models import User
from ..models.schemas import *



router = APIRouter()

@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password):
       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    
   
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(subject=user.id, expires_delta=access_token_expires)
    
   
    response_content = {"access_token": access_token, "token_type": "bearer"}
    return JSONResponse(content=response_content)


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


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        user = get_user_by_username(db, username)
        if user is None:
            raise credentials_exception
        return user
    except jwt.JWTError:
        raise credentials_exception


@router.get("/auth/check")
async def check_auth_status(current_user: User = Depends(get_current_user)):
    return {"authenticated": True} 

