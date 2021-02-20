# yamdb_final
yamdb_final
# Project Title

Проект представляет собой REST API для сервиса YaMDb — базы отзывов о фильмах, книгах и музыке. 
Документация с шаблонами запросов к API и структуре ответов находится по адресу /redoc

### Prerequisites

Для развертывания приложения необходимо установить Docker

### Installing

Скачайте каталог INFRA_SP2
В корневой директории запустите команду docker-compose up
После запуска контейнера приложение будет доступно по адресу http://0.0.0.0:8000
Для остановки приложения выполните команду docker-compose down

для создания суперпользователя выполните команду python3 manage.py createsuperuser 

для заполнения базы данных начальными данными выполните команду python3 manage.py loaddata fixtures.json

запуск миграций в контейнере производится командой fab runmigrations --hosts="127.0.0.1"

## Tests

для запуска автоматических тестов в корневой директории выполните команду pytest

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [PostgreSQL](https://www.postgresql.org/) - Relational Database
* [Docker](https://www.docker.com/) - Used for containerized application

## Contributing
pass

[![yambd](https://github.com/AllNagard/yamdb_final/actions/workflows/yambd_workflow.yml/badge.svg)](https://github.com/AllNagard/yamdb_final/actions/workflows/yambd_workflow.yml)


## Versioning

pass

## Authors
Алла Драган - Alla Dragan (Alla - it's my name, it's not a combination of a preposition with an article )))

## License
Этот проект лицензируется в соответствии с лицензией MIT License

Copyright (c) 2021 infra_sp2

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
