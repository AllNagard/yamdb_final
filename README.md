![Build Status](https://github.com/AllNagard/yamdb_final/workflows/yamdb_workflow/badge.svg)

ip адрес приложения 130.193.56.96

# yamdb_final
yamdb_final
# Project Title

Проект представляет собой REST API для сервиса YaMDb — базы отзывов о фильмах, книгах и музыке. 
Документация с шаблонами запросов к API и структуре ответов находится по адресу /redoc

### Prerequisites

Развертывание на сервере происходит автоматически при выполнении push в ветку main

### Installing

Скачайте каталог yamdb_final


Для остановки приложения выполните команду docker-compose down

Переименуйте файл .env.example в .env и внесите в него индивидуальные настройки

Для перехода в контейнер выполните команду docker-compose exec <имя_контейнера> bash

для подключения статики выполните python3 manage.py collectstatic

для создания суперпользователя выполните команду python3 manage.py createsuperuser 

для заполнения базы данных начальными данными выполните команду python3 manage.py loaddata fixtures.json

запуск миграций в контейнере производится командой fab runmigrations --hosts="130.193.56.96"



## Tests

для запуска автоматических тестов в корневой директории выполните команду pytest

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [PostgreSQL](https://www.postgresql.org/) - Relational Database
* [Docker](https://www.docker.com/) - Used for containerized application
* [Fabric] (http://www.fabfile.org/) - Used for migration process automation 

## Contributing
pass



## Versioning

pass

## Authors
Алла Драган - Alla Dragan (Alla - it's my name, it's not a combination of a preposition with an article )))

## License
Этот проект лицензируется в соответствии с лицензией MIT License

Copyright (c) 2021 yamdb_final

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Acknowledgments

Спасибо моему мужу и дочке! Вы всегда вдохновляете меня идти вперед!
