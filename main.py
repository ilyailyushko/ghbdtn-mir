"""
Минимальное FastAPI-приложение с одним эндпоинтом приветствия.
"""

from curses import echo
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
    return "Привет мир, как дела, хорошо?"


@app.get(f"{echo}/<name>")
async def hello_name(name: str) -> str:
    """
    Эндпоинт: возвращает приветствие на русском с именем.

    Args:
        name: Имя для приветствия.

    Returns:
        Строка ``Привет, {name}`` в теле ответа (text/plain).
    """
    return f"Привет, {name}"