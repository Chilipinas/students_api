## Запуск скрипта

Для запуска нужно установить необходимые пакеты, для этого создадим виртуальное окружение и активируем его с помощью команд:
```shell
$ python -m venv myenv
$ .\myenv\Scripts\activate
```
Так же установить пакеты:
```shell
$ pip install fastapi uvicorn sqlalchemy databases[sqlite] python-dotenv
```