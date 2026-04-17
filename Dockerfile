# Образ для FastAPI-приложения (uvicorn).
FROM python:3.12-slim-bookworm

# Не буферизовать stdout/stderr — логи сразу видны в `docker logs`.
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Зависимости отдельным слоем — кэш при неизменном requirements.txt.
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY main.py .

EXPOSE 8000

# Слушаем все интерфейсы — нужно для контейнера.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
