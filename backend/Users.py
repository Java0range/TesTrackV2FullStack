import sqlite3
from fastapi import APIRouter
from pydantic import BaseModel
from Auth import Auth


users = APIRouter(tags=["Users"], prefix="/users")

security = Auth(
    open("./keys/signature_key.txt", "r", encoding="utf-8").read().strip(),
    str.encode(open("./keys/crypto_key.txt", "r", encoding="utf-8").read().strip())
)


class User(BaseModel):
    username: str
    password: str


class UserCreate(BaseModel):
    username: str
    password: str
    is_admin: bool
    token: str


class Token(BaseModel):
    token: str


class CheckIsTeacher(BaseModel):
    token: str


class DeleteUser(BaseModel):
    id: int
    token: str


async def get_user_by_db(username: str, password: str):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    ans = cursor.execute(f"SELECT id, password FROM Users WHERE username = '{username}'").fetchone()
    conn.close()
    if ans:
        if ans[1] == password:
            return ans[0]
        return False
    return False


async def check_username(username: str):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    ans = cursor.execute(f"SELECT id FROM Users WHERE username = '{username}'").fetchone()
    conn.close()
    if ans:
        return True
    return False


async def create_user_for_db(username, password, is_admin=False):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (username, password, isAdmin) VALUES (?, ?, ?)", (username, password, is_admin))
    conn.commit()
    conn.close()


async def check_user_permission(token: str):
    user_id = security.get_user_for_token(token)
    if "Error" not in token:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        ans = cursor.execute(f"SELECT isAdmin FROM Users WHERE id = {user_id}").fetchone()
        if ans[0]:
            return "True"
        return "Error: Not enough rights"
    return f"{user_id}"


async def check_user_auth(token: str):
    user_id = security.get_user_for_token(token)
    if user_id:
        return True
    else:
        return False


async def get_user_from_token(token: str):
    user_id = security.get_user_for_token(token)
    if user_id:
        return user_id
    else:
        return "error"


@users.post("/auth")
async def auth(inp: User):
    try:
        ans = await get_user_by_db(inp.username, inp.password)
        if ans:
            return {"token": security.generate_token_for_user(ans)}
        return "Error: Invalid username or password"
    except Exception as e:
        return "Error: Server error: " + str(e)


@users.post("/create")
async def create_user(inp: UserCreate):
    if await check_user_auth(inp.token):
        try:
            if await check_username(inp.username):
                return "Error: Username already exists"
            else:
                await create_user_for_db(inp.username, inp.password, is_admin=inp.is_admin)
                return "Success"
        except Exception as e:
            return f"Error: Server error: {e}"
    return "Error: Invalid token"


@users.get("/users/{token}")
async def get_all_users(token: str):
    try:
        if await check_user_auth(token):
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            ans = cursor.execute(f"SELECT id, username, isAdmin FROM Users").fetchall()
            conn.close()
            return ans
        else:
            return "Error: Invalid token"
    except Exception:
        return "Error: Server error"


@users.post("/isTeacher")
async def is_teacher(inp: CheckIsTeacher):
    user = await check_user_permission(inp.token)
    if user == "True":
        return "True"
    return user


@users.delete("/delete")
async def delete_user(inp: DeleteUser):
    try:
        user = await check_user_permission(inp.token)
        if user == "True":
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM Users WHERE id = {inp.id}")
            cursor.execute(f"DELETE FROM Results WHERE user_id = {inp.id}")
            conn.commit()
            conn.close()
        return user
    except Exception:
        return "Error: Server error"