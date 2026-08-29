from fastapi import FastAPI, HTTPException
from models import UserCreate, UserPublic
from security import hash_password
from database import db
from datetime import datetime
app = FastAPI()

users_collection = db["users"]

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/auth/register", response_model=UserPublic)
def register(user: UserCreate):
    # 1. Check if a user with this email already exists
    existing_user = users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # 2. Hash the password — never store it plain
    hashed = hash_password(user.password)

    # 3. Build the document to store
    user_doc = {
        "name": user.name,
        "email": user.email,
        "hashed_password": hashed,
        "auth_provider": "local",
        "created_at": datetime.utcnow(),
    }

    # 4. Insert into MongoDB
    result = users_collection.insert_one(user_doc)

    # 5. Return the public-safe version (no password field at all)
    created_user = users_collection.find_one({"_id": result.inserted_id})
    return UserPublic(
        name=created_user["name"],
        email=created_user["email"],
        created_at=created_user.get("created_at"),
    )