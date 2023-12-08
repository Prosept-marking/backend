# Проект Просепт:
[![MSPP CI/CD](https://github.com/Prosept-marking/backend/actions/workflows/main.yml/badge.svg)](https://github.com/Prosept-marking/backend/actions/workflows/main.yml/badge.svg)

Цель проекта - разработка решения, которое отчасти автоматизирует процесс сопоставления товаров оператором. Основная идея - предлагать несколько товаров заказчика, которые с наибольшей вероятностью соответствуют размечаемому товару дилера. Выбор наиболее вероятных подсказок делается методами машинного обучения.

Полезные ссылки:
- Swagger: http://prosept.hopto.org/swagger/
- Archive project: https://disk.yandex.com.am/d/-Ih7A6b707sy8A



## Оглавление:
- [Технологии](#технологии)
- [Описание работы](#описание-работы)
- [Установка и запуск](#установка-и-запуск)
- [Удаление](#удаление)
- [Авторы](#авторы)



## Технологии:
<details><summary>Развернуть</summary>

**Языки программирования, библиотеки и модули:**

[![Python](https://img.shields.io/badge/Python-v3.11-blue?logo=python)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/-pandas-464646?logo=)](https://docs.python.org/3/library/pandas.html#the-interpreter-stack)
[![logging](https://img.shields.io/badge/-logging-464646?logo=)](https://docs.python.org/3/library/logging.html)
[![Pytest](https://img.shields.io/badge/-Pytest-464646?logo=Pytest)](https://docs.pytest.org/en/latest/)
[![uvicorn](https://img.shields.io/badge/-uvicorn-464646?logo=Uvicorn)](https://www.uvicorn.org/)


**Фреймворк, расширения и библиотеки:**

[![Django](https://img.shields.io/badge/Django-v4.1-blue?logo=Django)](https://www.djangoproject.com/)


**База данных:**

[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?logo=PostgreSQL)](https://www.postgresql.org/)


**CI/CD:**

[![GitHub_Actions](https://img.shields.io/badge/-GitHub_Actions-464646?logo=GitHub)](https://docs.github.com/en/actions)
[![docker_hub](https://img.shields.io/badge/-Docker_Hub-464646?logo=docker)](https://hub.docker.com/)
[![docker_compose](https://img.shields.io/badge/-Docker%20Compose-464646?logo=docker)](https://docs.docker.com/compose/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?logo=NGINX)](https://nginx.org/ru/)

[⬆️Оглавление](#оглавление)
</details>



## Описание работы:
При запуске приложения БД инициализируется следующими таблицами:
1. Товары производителя
2. Товары дилеров
3. Перечень дилеров
4. Таблица сопоставления товаров производителя и дилеров

Сервис поддерживает следующие базовые функции:

**Главное меню:**

- Выводится товар из таблицы производителя с пагинацией
- Возможность фильтра данных по дилеру, статусу обработки и даты получения записи

**Поиск совпадений:**

- Автоматическое сопоставление товара производителя с товаром дилера на основе ML
- Возможность выбора совпадения для подтверждения сопоставления
- Возможность отклонения совпадения для дальнейшего сопоставления в "ручную"
- Возможность перехода к следуйющей модели

**Статистика:**

- Подсчет ежедневной статистики работы с товаром
- Статистики сопоставлений по конкретному дилеру

[⬆️Оглавление](#оглавление)



## Установка и запуск:
Удобно использовать принцип copy-paste - копировать команды из GitHub Readme и вставлять в командную строку Git Bash или IDE (например VSCode).
#### Предварительные условия:
<details><summary>Развернуть</summary>

Предполагается, что пользователь:
 - создал аккаунт [DockerHub](https://hub.docker.com/), если запуск будет производиться на удаленном сервере.
 - установил [Docker](https://docs.docker.com/engine/install/) и [Docker Compose](https://docs.docker.com/compose/install/) на локальной машине или на удаленном сервере, где проект будет запускаться в контейнерах. Проверить наличие можно выполнив команды:
    ```bash
    docker --version && docker-compose --version
    ```
</details>
<hr>
<details><summary>Локальный запуск</summary>

1. Клонируйте репозиторий с GitHub и в **.env**-файле введите данные для переменных окружения (значения даны для примера, но их можно оставить; подсказки даны в комментариях):
```bash
git clone https://github.com/Prosept-marking/backend.git && \
cd backend && \
cp .env_example .env && \
nano .env
```
Для работы сервиса необходимо задать значения минимум пяти переменным окружения: `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`, , `DB_HOST`, `DB_PORT`.


2. Запуск - из корневой директории проекта выполните команду:
```bash
docker compose up -d --build
```
Проект будет развернут в четырех docker-контейнерах (db, backend, frontend, nginx) по адресу `http://localhost:80`.

3. Остановить docker и удалить контейнеры можно командой из корневой директории проекта:
```bash
docker compose down
```
Если также необходимо удалить тома базы данных и статики:
```bash
docker compose down -v
```
<hr></details>
<details><summary>Запуск на удаленном сервере</summary>

1. Создайте `Actions.Secrets` согласно списку ниже (значения указаны для примера) + переменные окружения из `env_example` файла:
```py

# Данные удаленного сервера и ssh-подключения:
HOST  # публичный IP-адрес вашего удаленного сервера
USER
SSH_KEY
SSH_PASSPHRASE

#  Переменные для работы с PostgreSQL.
POSTGRES_HOST=db
POSTGRES_DB=postgres
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=12345

# Переменные для создания суперюзера.
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@admin.com
DJANGO_SUPERUSER_PASSWORD=admpass

# Переменные для работы с docker.
DOCKERHUB_USERNAME=username
DOCKERHUB_USERNAME_FRONT=username_front
PROJECT_NAME=project_name
```

4. Запустите вручную `workflow`, чтобы автоматически развернуть проект в четырех docker-контейнерах (db, backend, frontend, nginx) на удаленном сервере.
</details>
<hr>

При первом запуске будут автоматически произведены следующие действия:
  * выполнятся миграции БД
  * создастся суперюзер (пользователь с правами админа) с учетными данными из переменных окружения `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL`, `DJANGO_SUPERUSER_PASSWORD`.
  * соберется статика

Вход в админ-зону осуществляется по адресу: http://`hostname`/admin/ , где `hostname`:
  * `localhost`
  * Доменное имя удаленного сервера, например `prosept.hopto.org`

[⬆️Оглавление](#оглавление)



## Удаление:
Для удаления проекта выполните команду:
```bash
cd .. && rm -fr backend
```

[⬆️Оглавление](#оглавление)



## Авторы:

[Vladislav Kuznetsov](https://github.com/VladislavCR)

[Ilya Gorbunov](https://github.com/gorbunov-ilya)

[⬆️В начало](#Проект-MSPP)
