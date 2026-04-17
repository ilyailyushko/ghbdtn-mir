"""
Минимальное FastAPI-приложение с одним эндпоинтом приветствия.
"""

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI(
    title="Приветствие",
    description='Возвращает текст "Привет мир".',
    version="0.1.0",
)


@app.get("/", response_class=PlainTextResponse)
async def hello() -> str:
    """
    Корневой эндпоинт: возвращает приветствие на русском.

    Returns:
        Строка ``Привет мир`` в теле ответа (text/plain).
    """
    return "Привет мир"
