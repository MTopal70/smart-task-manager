from passlib.context import CryptContext

# Wir definieren den Hashing-Algorithmus (bcrypt)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Nimmt ein Klartext-Passwort und gibt den Hash zurück."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Vergleicht ein Klartext-Passwort mit einem Hash."""
    return pwd_context.verify(plain_password, hashed_password)