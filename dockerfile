"""Вариант того как это можно было бы запустить в dockerfile, но такой
потребности нет, поскольку я обошёлся sqlite для такого маленького приложения.
В принципе можно было бы поменять базу на postgres и запускать всё это дело
через docker-compose.yml
"""
FROM python:3.12.4

WORKDIR /app/

RUN pip install 'poetry==1.6.1'
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false &&  \
    poetry install --no-interaction --no-ansi --no-dev

COPY . .

CMD chmod a+x scripts/*sh &&  \
    /app/scripts/run_migration.sh &&  \
    /app/scripts/run_gunicorn.sh
