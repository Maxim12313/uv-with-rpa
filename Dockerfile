FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

COPY ./robot /app

RUN uv sync --locked

ENV PATH="/app/.venv/bin/:$PATH"

CMD ["uv", "run", "-m", "robocorp.tasks", "run", "task.py"]
