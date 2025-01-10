import sqlite3
from fastapi import APIRouter
from pydantic import BaseModel
from Users import check_user_permission
from Users import check_user_auth
from Users import get_user_from_token


tests = APIRouter(prefix="/tests", tags=["Tests"])


class CreateTest(BaseModel):
    name: str
    taskIdList: list
    token: str


class DeleteTest(BaseModel):
    id: int
    token: str


async def create_test_in_db(name: str, task_id_list: list):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Tests (Name, TaskIdList) VALUES (?, ?)", (name, "%%%".join(task_id_list)))
        conn.commit()
        conn.close()
        return "true"
    except Exception:
        return "error"


async def delete_test_in_db(id: int):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Tests WHERE id = ?", (id,))
        cursor.execute("DELETE FROM Results WHERE test_id = ?", (id,))
        conn.commit()
        conn.close()
        return "true"
    except Exception:
        return "error"


async def get_tests_for_user_from_db(user_id: int):
    try:
        tests_list = []
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Tests")
        for test in cursor.fetchall():
            if not len(cursor.execute("SELECT * FROM Results WHERE test_id = ? and user_id = ?", (test[0], user_id)).fetchall()):
                tests_list.append([test[0], test[1], test[2].split("%%%")])
        conn.close()
        return tests_list
    except Exception as e:
        return e


async def get_test_for_user_from_db(test_id: int, user_id: int):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        ans = cursor.execute("SELECT * FROM Results WHERE test_id = ? and user_id = ?", (test_id, user_id)).fetchall()
        if ans:
            return "Error: This test is not available to you"
        select_test_id, name, tasks = cursor.execute("SELECT * FROM Tests WHERE id = ?", (test_id,)).fetchall()[0]
        return [select_test_id, name, tasks.split("%%%")]
    except Exception:
        return "Error: Server error"


@tests.get("/tests/{token}")
async def get_all_tests(token: str):
    if await check_user_auth(token):
        try:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            ans = cursor.execute("SELECT * FROM Tests").fetchall()
            return ans
        except Exception:
            return "Error: Server error"
    return "Error: Invalid token"


@tests.post("/create")
async def create_test(inp: CreateTest):
    user = await check_user_permission(inp.token)
    if user == "True":
        ans = await create_test_in_db(inp.name, inp.taskIdList)
        if "error" in ans:
            return "Error: Server error"
        else:
            return "Success"
    return user


@tests.delete("/delete")
async def delete_test(inp: DeleteTest):
    user = await check_user_permission(inp.token)
    if user == "True":
        ans = await delete_test_in_db(inp.id)
        if "error" in ans:
            return "Error: Server error"
        else:
            return "Success"
    return user


@tests.get("/testsForUser/{token}")
async def get_tests_for_user(token: str):
    try:
        user_id = await get_user_from_token(token)
        if user_id != "error":
            ans = await get_tests_for_user_from_db(user_id)
            return ans
        else:
            return "Error: Invalid token"
    except Exception:
        return f"Error: Server error"


@tests.get("/testForUser/{token}/{test_id}")
async def get_test_for_user(token: str, test_id: int):
    try:
        user_id = await get_user_from_token(token)
        if user_id != "error":
            ans = await get_test_for_user_from_db(test_id, user_id)
            return ans
        else:
            return "Error: Invalid token"
    except Exception:
        return f"Error: Server error"