from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os

app = FastAPI()

# Модель для входных данных
class URLRequest(BaseModel):
    url: str

@app.post("/fetch-html/")
async def fetch_html(data: URLRequest):
    try:
        # Загружаем HTML-код
        response = requests.get(data.url)
        response.raise_for_status()

        # Путь для сохранения файла
        save_path = os.getenv("SAVE_PATH", "./data")
        os.makedirs(save_path, exist_ok=True)

        file_path = os.path.join(save_path, "output.html")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(response.text)

        return {"message": "HTML успешно сохранен", "file_path": file_path}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Ошибка при загрузке URL: {e}")
