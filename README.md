## Описание
Проект предназначен для проверки доступности веб-сайтов по их url.
Список доменов загружается через excel-файл и сохраняется в БД.
Данные с информацией о доступности веб-сайта сохраняются в БД.
Также реализована возможность продолжить проверку с определенного сайта (начиная с определенного id).

## Как запустить этот проект
1. Создайте папку для этого проекта и перейдите в нее.
2. Склонируйте репозиторий командой `git clone https://github.com/PavelKimm/http_checker.git .
` (обратите внимание на точку в конце команды)
3. Если в системе не установлен [Pipenv](https://pipenv.pypa.io/en/latest/install/), но установлен pip, один из простых
спопобов установить его – выполнить команду
`pip install --user pipenv`
4. Для создания виртуального окружения с нужными пакетами выполните команду
`pipenv install`
5. Для активации виртуального окружения выполните команду
`pipenv shell`
6. После выполнения команды `python manage.py runserver` веб-приложение будет доступно по [данному адресу](http://localhost:8000/)

## API
Для загрузки сайтов в БД из файла используйте следующий запрос:
```text
(POST) http://localhost:8000/api/v1/analyzer/load-websites/
Request body:
{
    "files": [YOUR_FILE1.xlsx, YOUR_FILE2.xlsx]
}
```
Запуск проверки сайтов:
```text
(POST) http://localhost:8000/api/v1/analyzer/check-websites/
Request body:
{
    "start_from_id": WEBSITE_ID (OR null)
}
```
Для получения последней проверки по определенному сайту используйте следующий запрос:
```text
(GET) http://localhost:8000/api/v1/analyzer/websites/?url=WEBSITE_URL
Response example:
{
    "id": 2606,
    "website": {
        "id": 1732,
        "url": "almatyelectro.satu.kz"
    },
    "response_status_code": 200,
    "reason": "OK",
    "ip_address": "194.4.59.209",
    "server": "nginx",
    "checked_at": "2020-12-15T15:03:14.606176+06:00"
}
```

## Admin panel
Доступ к панели админа производится по следующей ссылке:<br>
http://127.0.0.1:8000/admin/

В БД из репозитория уже создан суперпользователь с логином **admin** и паролем **admin**
