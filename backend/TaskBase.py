import requests
from bs4 import BeautifulSoup
from fastapi import APIRouter


task_base = APIRouter(tags=['TaskBase'], prefix="/taskbase")


@task_base.get('/tasks/{number}')
async def get_tasks(number: int):
    if number <= 27:
        try:
            ans = await get_tasks_by_number(number)
            return ans
        except Exception:
            return "Error: Server error"
    else:
        return "Error: Invalid number task"


@task_base.get('/task/{number}')
async def get_task(number: int):
    try:
        ans = await get_task_by_id(number)
        return ans
    except Exception:
        return "Error: Server error"



async def get_tasks_by_number(number: int):
    tasks = []
    url = f"https://kompege.ru/api/v1/task/number/{number}"
    response = requests.get(url)
    response.encoding = "utf-8"
    response = response.json()
    for item in response:
        ans = item["text"]
        if "base64" in ans:
            continue
        table = []
        img = []
        soup = BeautifulSoup(ans, "lxml")
        if "td" in ans:
            for i in soup.find_all("tr"):
                lst = []
                for j in i.find_all("td"):
                    if j.text == " ":
                        lst.append("")
                    else:
                        lst.append(j.text.replace(" ", ""))
                table.append(lst)
        writer_link = "".join([i.get("href") for i in soup.find_all("a")])
        writer_name = ("".join([i.text for i in soup.find_all("a")]).replace("(", "").replace(")", ""))
        text = "".join([i.text for i in soup.find_all("p")])
        if "img" in ans:
            img = [i.get("src") for i in soup.find_all("img")]
        if not text:
            continue
        else:
            if writer_link:
                if text[0] == "(":
                    text = text.replace("(", "", 1).replace(")", "", 1)
                text = text.replace(writer_name, "").strip()
        otv = item["key"]
        number_task = item["number"]
        task_id = item["taskId"]
        files = item["files"]
        difficulty = ""
        match item["difficulty"]:
            case 0:
                difficulty = "Базовый"
            case 1:
                difficulty = "Средний"
            case 2:
                difficulty = "Сложный"
            case 3:
                difficulty = "Гроб"
        elem = {
            "text": text.replace(" ", ""),
            "writer_name": writer_name,
            "writer_link": writer_link,
            "table": table,
            "img": img,
            "otv": otv,
            "number_task": number_task,
            "task_id": task_id,
            "files": files,
            "difficulty": difficulty
        }
        tasks.append(elem)
    return tasks


async def get_task_by_id(id: int):
    url = f"https://kompege.ru/api/v1/task/{id}"
    response = requests.get(url)
    response.encoding = "utf-8"
    response = response.json()
    ans = response["text"]
    table = []
    img = []
    soup = BeautifulSoup(ans, "lxml")
    if "td" in ans:
        for i in soup.find_all("tr"):
            lst = []
            for j in i.find_all("td"):
                if j.text == " ":
                    lst.append("")
                else:
                    lst.append(j.text.replace(" ", ""))
            table.append(lst)
    writer_link = "".join([i.get("href") for i in soup.find_all("a")])
    writer_name = ("".join([i.text for i in soup.find_all("a")]).replace("(", "").replace(")", ""))
    text = "".join([i.text for i in soup.find_all("p")])
    if "img" in ans:
        img = [i.get("src") for i in soup.find_all("img")]
    if not text:
        return "Error: Task incorrect"
    else:
        if writer_link:
            if text[0] == "(":
                text = text.replace("(", "", 1).replace(")", "", 1)
            text = text.replace(writer_name, "").strip()
    otv = response["key"]
    number_task = response["number"]
    task_id = response["taskId"]
    files = response["files"]
    difficulty = ""
    match response["difficulty"]:
        case 0:
            difficulty = "Базовый"
        case 1:
            difficulty = "Средний"
        case 2:
            difficulty = "Сложный"
        case 3:
            difficulty = "Гроб"
    elem = {
        "text": text.replace(" ", ""),
        "writer_name": writer_name,
        "writer_link": writer_link,
        "table": table,
        "img": img,
        "otv": otv,
        "number_task": number_task,
        "task_id": task_id,
        "files": files,
        "difficulty": difficulty
    }
    return [elem]


def check_otv_for_task_id(task_id: str, user_otv: str):
    url = f"https://kompege.ru/api/v1/task/{task_id}"
    response = requests.get(url)
    response.encoding = "utf-8"
    response = response.json()
    otv = response["key"]
    if user_otv == otv:
        return True
    return False