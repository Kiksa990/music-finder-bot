import requests
from config import SHAZAM_TOKEN

def recognize_music(audio_url: str) -> str:
    """
    Отправляет аудио в Shazam API и возвращает название трека.
    audio_url — ссылка на аудиофайл из Telegram.
    """
    endpoint = "https://shazam.p.rapidapi.com/songs/v2/detect"
    headers = {
        "X-RapidAPI-Key": SHAZAM_TOKEN,
        "X-RapidAPI-Host": "shazam.p.rapidapi.com",
        "Content-Type": "application/json"
    }
    payload = {
        "url": audio_url
    }

    try:
        response = requests.post(endpoint, json=payload, headers=headers)
        result = response.json()

        # Попытка извлечь название трека
        track = result.get("track", {})
        title = track.get("title", "Неизвестный трек")
        artist = track.get("subtitle", "Неизвестный артист")

        return f"🎶 {artist} — {title}"
    except Exception as e:
        return f"Ошибка при распознавании: {e}"