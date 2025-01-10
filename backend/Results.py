from fastapi import APIRouter
from pydantic import BaseModel
from TaskBase import check_otv_for_task_id
from Users import get_user_from_token
from Users import check_user_permission
import sqlite3

results = APIRouter(prefix="/results", tags=["results"])


class SaveResult(BaseModel):
    test_id: int
    result: list
    token: str


async def save_result_in_db(test_id: int, user_id: int, result: list):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT TaskIdList FROM Tests WHERE id = ?", (test_id,))
    tasks_id = cursor.fetchall()[0][0].split("%%%")
    answers = []
    for i in range(len(tasks_id)):
        if result[i]:
            if check_otv_for_task_id(tasks_id[i], result[i]):
                answers.append("1")
            else:
                answers.append("0")
        else:
            answers.append("0")
    cursor.execute("INSERT INTO Results(user_id, test_id, otv) VALUES (?, ?, ?)", (user_id, test_id, "%%%".join(answers)))
    conn.commit()
    conn.close()
    return answers


async def get_result_for_test_from_db(test_id: str):
    results = []
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT TaskIdList FROM Tests WHERE id = ?", (test_id,))
    results.append(cursor.fetchone()[0].split("%%%"))
    cursor.execute("SELECT Users.username, Results.otv FROM Results INNER JOIN Users ON Users.id = Results.user_id WHERE Results.test_id = ?", (test_id,))
    for item in cursor.fetchall():
        results.append({
            "user": item[0],
            "result": item[1].split("%%%")
        })
    return results


async def get_result_for_user_from_db(user_id: str):
    results = []
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Users.username, Tests.Name, Results.otv FROM Results INNER JOIN Users ON Users.id = Results.user_id INNER JOIN Tests ON Tests.id = Results.test_id WHERE Results.user_id = ?", (user_id,))
    for item in cursor.fetchall():
        results.append({
            "user": item[0],
            "test": item[1],
            "result": item[2].split("%%%")
        })
    return results

@results.post("/save")
async def save_result(inp: SaveResult):
    try:
        user_id = await get_user_from_token(inp.token)
        if user_id != "error":
            ans = await save_result_in_db(inp.test_id, user_id, inp.result)
            return ans
        else:
            return "Error: Invalid token"
    except Exception:
        return "Error: Server error"


@results.get("/test/{token}/{test_id}")
async def get_results_for_test(token: str, test_id: str):
    try:
        user = await check_user_permission(token)
        if user == "True":
            ans = await get_result_for_test_from_db(test_id)
            return ans
        return user
    except Exception:
        return "Error: Server error"


@results.get("/user/{token}/{user_id}")
async def get_results_for_test(token: str, user_id: str):
    try:
        user = await check_user_permission(token)
        if user == "True":
            ans = await get_result_for_user_from_db(user_id)
            return ans
        return user
    except Exception:
        return "Error: Server error"