from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(plain_password: str) -> str:
    """Turns a plain password into a one-way bcrypt hash."""
    return pwd_context.hash(plain_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Checks if a plain password matches a stored hash, without ever reversing the hash."""
    return pwd_context.verify(plain_password, hashed_password)