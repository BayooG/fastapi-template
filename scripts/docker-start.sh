#!/bin/sh

set -e

./scripts/wait-for-postgres.sh $POSTGRES_HOST
poetry run alembic upgrade head



poetry run uvicorn service.main:app --host 0.0.0.0 --port 8000 --reload