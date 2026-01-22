import yt_dlp

def download_video(url: str) -> str:
    """
    Скачивает видео с YouTube по ссылке.
    Возвращает строку с информацией о видео.
    """
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',  # имя файла = название видео
            'noplaylist': True,
            'quiet': True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

            # Формируем красивый ответ
            title = info.get("title", "Без названия")
            uploader = info.get("uploader", "Неизвестный автор")
            duration = info.get("duration", 0)  # в секундах
            minutes = duration // 60
            seconds = duration % 60
            quality = info.get("format", "Неизвестное качество")

            return (
                f"🎬 Видео: {title}\n"
                f"👤 Автор: {uploader}\n"
                f"⏱️ Длительность: {minutes}:{seconds:02d}\n"
                f"📹 Качество: {quality}\n"
                f"💾 Файл сохранён: {filename}"
            )
    except Exception as e:
        return f"❌ Ошибка при скачивании: {e}"