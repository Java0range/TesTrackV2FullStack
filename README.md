# TesTrackV2
TesTrackV2 Beta - это OpenSource Web приложение для проведения пробников ЕГЭ по информатике, нацеленое в первую очередь на повышение новыков для сдачи экзамена


**Автор Проекта** - Кудаев Никита


**Цели**: Написать OpenSource Web приложение для проведения пробников ЕГЭ по информатике, нацеленое в первую очередь на повышение новыков для сдачи экзамена.


В проекте должны быть реализованы такие функции, как:
+ Разработка интуитивно понятного интерфейса c адаптивной вёрсткой.
+ Большая база тренировочных заданий.
+ Удобная админ панель для учителя.
+ Удобная аналитика по тестам и ученикам для учителя.


**Возможные улучшения:**
+ Переход на базу данных PostgreSQL для повышения производительности и масштабируемости.
+ Добавить более глубокую аналитику результатов тестирования.


# Локальный запуск
+ Для локального запуска потребуется скачать [Docker Desktop](https://www.docker.com/get-started/)
+ После необходимо скачать проект или воспользоваться `git clone`
+ Заменить строку `axios.defaults.baseURL = "http://82.148.19.224/api"` на `axios.defaults.baseURL = "http://localhost/api"` по пути `frontend/src/App.vue`
+ Запуск проекта осуществляется через командную строку. В директории `/TesTrackV2FullStack` проекта выполнить команду `docker compose up --build`
+ После запуска Docker сайт будет доступен по адресу `http://localhost`
+ Для остановки проекта можно воспользоваться сочетанием клавиш `Ctrl + C` или командой `docker compose stop`


# Запуск проекта на сервере
**Важно:** для запуска проекта на сервере IP сервера нужно прописать в 2 файлах:
1. По пути `/backend/main.py` на 18 строке изменить: `origins = ["http://localhost:5173", "http://Ip адрес вашего сервера:5173"]`
2. По пути `/frontend/src/App.vue` на 14 строке изменить: `axios.defaults.baseURL = "http://Ip адрес вашего сервера/api"`


Пример запуска проекта на пустом только что созданном ubuntu сервере:
```
sudo apt-update
sudo apt-get install git
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
git clone https://github.com/Java0range/TesTrackV2FullStack.git
# На данном этапе обычно производится замена Ip описанная выше
cd TasTrackV2FullStack
docker compose up --build
```
Для остановки существуют 2 способа:
+ `Ctrl + C`
+ `docker compose stop`