## Запуск скрипта

Для запуска нужно установить необходимые пакеты, для этого создадим виртуальное окружение и активируем его с помощью команд:
```shell
$ python -m venv myenv
$ .\myenv\Scripts\activate
```
Так же установить пакеты:
```shell
$ pip install fastapi uvicorn sqlalchemy asyncpg psycopg2 pydantic python-dotenv
```
Что бы собрать контейнер и запустить его воспользоваться командами:
```shell
$ docker-compose up --build
$ docker-compose up -d
```

P.s. Для запуска необходим установленный на пк Docker.