FROM python:3.11

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY pyproject.toml poetry.lock  /app/

RUN pip install poetry && poetry install --no-root

RUN apt-get update && apt-get install -y postgresql-client

COPY ./ /app

# COPY scripts/ /app/scripts/

# COPY alembic.ini poetry.lock  /app/

# COPY tests/  /app/tests/

# COPY seed/  /app/scripts/seed/

# RUN chmod -R +x /app/scripts/

# ENTRYPOINT ["/app/scripts/docker-start.sh"]

ENTRYPOINT ["python","/app/main.py"]
