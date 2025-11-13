from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserOut
from app.security import hash_password # <-- Importieren unserer Hashing-Funktion

# Wir erstellen einen neuen Router
router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    Erstellt einen neuen Benutzer in der Datenbank.
    """

    # 1. Prüfen, ob der User (Username oder E-Mail) schon existiert
    db_user_email = db.query(User).filter(User.email == user_data.email).first()
    if db_user_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    db_user_username = db.query(User).filter(User.username == user_data.username).first()
    if db_user_username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken"
        )

    # 2. Das Passwort hashen
    hashed_pw = hash_password(user_data.password)

    # 3. Den neuen User erstellen (mit dem gehashten Passwort)
    #    Wir müssen das 'password' aus dem user_data-Objekt entfernen

    # Sicherer Weg, das User-Objekt zu erstellen:
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user