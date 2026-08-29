from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Literal

class UserCreate(BaseModel):
    """What the client sends us when registering."""
    name: str
    email: EmailStr
    password: str  # plain text, ONLY at this input stage — we hash it immediately in Step 8

class UserInDB(BaseModel):
    """What we actually store in MongoDB."""
    name: str
    email: EmailStr
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    auth_provider: Literal["local", "google"] = "local"

class UserPublic(BaseModel):
    """What we send BACK to the client — notice: no password field at all."""
    name: str
    email: EmailStr
    created_at: datetime