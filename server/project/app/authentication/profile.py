from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .schemas import ProfileCreate, ProfileResponse  # Adjust based on your actual schemas
from .models import Profile, User  # Adjust based on your actual models
from .database import get_db
from .oauth2 import get_current_user  # Ensure this dependency correctly identifies the current user

router = APIRouter()

@router.post("/profile/", response_model=ProfileResponse)
def create_profile(
    profile_data: ProfileCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    # Check if the current user already has a profile
    existing_profile = db.query(Profile).filter(Profile.user_id == current_user.id).first()
    if existing_profile:
        raise HTTPException(status_code=400, detail="Profile already exists")
    
    # Create a new profile
    new_profile = Profile(**profile_data.dict(), user_id=current_user.id)
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile


