# 19.1
# Є відкритий офіційний API NASA Images and Video Library ( https://images-api.nasa.gov ), який дозволяє виконувати пошук медіа 
# та отримувати список файлів (assets) для кожного знайденого медіа-елемента.
# Ваше завдання - за допомогою модуля requests:
# - Виконати пошук зображень, повʼязаних з ровером Curiosity на Марсі.
# - 3 JSON відповіді витягнути nasa_id для знайдених елементів.
# - Для кожного nasa_id зробити додатковий запит до endpoint-a /asset/[nasa_id], щоб отримати список URL-ів
# файлів.
# - Обрати з цього списку посилання на JPG-зображення (наприклад, перший jpg або "найкращий" варіант, якщо їх кілька).
# - Скачати 2 зображення і зберегти локально як:
#   - mars_photot.jpg
#   - mars_photo2.jpg
# Важливо: потрібно виконати мінімум 3 НТТР-запити:
# 1 запит /search + 2 запити /asset/(nasa_id) (і ще 2 запити на скачування jpg-файлів).
# Доступні endpoint-и (Images API)
#   GET /search?q=(q) - пошук медіа
#   GET /asset/(nasa_id) - список файлів (URL) для вибраного медіа

# початковий шаблон
# import requests
# BASE_URL = "https://images-api.nasa.gov"
# # Пошук зображень
# search_url = f" {BASE_URL}/search"
# search_params = f
# "q": "Curiosity rover Mars"
# , # пошуковий запит
# "media_type": "image"
# ', # тільки зображення
# "page_size": 20 # щоб було з чого вибрати
# # Отримання файлів по nasa_id
# asset_url_template = f" {BASE_URL}/asset/{{nasa_id}}"

import os
import requests
from typing import List, Optional

BASE_URL = "https://images-api.nasa.gov"
TIMEOUT = 30

def assert_status_ok(resp: requests.Response, context: str = "") -> None:
    """одразу “фейлимо” сценарій, якщо бекенд повернув не 200 """
    if resp.status_code != 200:
        raise RuntimeError(
            f"HTTP {resp.status_code} error {context}. Response text: {resp.text[:300]}"
        )

def search_curiosity_images(page_size: int = 20) -> dict:
    search_url = f"{BASE_URL}/search"
    params = {
        "q": "Curiosity rover Mars",
        "media_type": "image",
        "page_size": page_size,
    }

    resp = requests.get(search_url, params=params, timeout=TIMEOUT)
    assert_status_ok(resp, context="during /search")
    return resp.json()

def extract_nasa_ids(search_json: dict, limit: int = 3) -> List[str]:
    """З /search JSON витягуємо nasa_id з items."""
    items = (search_json.get("collection") or {}).get("items") or []
    nasa_ids: List[str] = []

    for item in items:
        data_list = item.get("data") or []
        if not data_list:
            continue

        nasa_id = data_list[0].get("nasa_id")
        if nasa_id:
            nasa_ids.append(nasa_id)

        if len(nasa_ids) >= limit:
            break

    if len(nasa_ids) < limit:
        raise RuntimeError(f"Found only {len(nasa_ids)} nasa_id(s), expected at least {limit}.")

    return nasa_ids

def get_asset_urls(nasa_id: str) -> List[str]:
    """Для конкретного nasa_id бачимо список файлів через /asset/{nasa_id}."""
    asset_url = f"{BASE_URL}/asset/{nasa_id}"
    resp = requests.get(asset_url, timeout=TIMEOUT)
    assert_status_ok(resp, context=f"during /asset/{nasa_id}")

    asset_json = resp.json()
    items = (asset_json.get("collection") or {}).get("items") or []

    urls = []
    for it in items:
        href = it.get("href")
        if href:
            urls.append(href)

    if not urls:
        raise RuntimeError(f"No asset URLs found for nasa_id={nasa_id}")

    return urls


def pick_best_jpg(urls: List[str]) -> Optional[str]:
    jpgs = [u for u in urls if u.lower().endswith((".jpg", ".jpeg"))]
    if not jpgs:
        return None

    priority_keywords = ["orig", "original", "large", "~orig", "~large"]
    for kw in priority_keywords:
        for u in jpgs:
            if kw in u.lower():
                return u

    return jpgs[0]


def download_file(url: str, out_path: str) -> None:
    """Скачування файлу.Використовуємо stream=True, щоб не тримати весь файл в пам'яті."""
    resp = requests.get(url, stream=True, timeout=TIMEOUT)
    assert_status_ok(resp, context=f"downloading {url}")

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)

    with open(out_path, "wb") as f:
        for chunk in resp.iter_content(chunk_size=1024 * 64):
            if chunk:
                f.write(chunk)


def main() -> None:
    search_json = search_curiosity_images(page_size=20)

    # витягуємо 3 nasa_id 
    nasa_ids = extract_nasa_ids(search_json, limit=3)
    print("Found nasa_id:", nasa_ids)

    # беремо 2 перших nasa_id, робимо /asset і вибираємо jpg
    selected_jpg_urls = []
    selected_ids_for_download = nasa_ids[:2]  # рівно 2 для скачування

    for nasa_id in selected_ids_for_download:
        urls = get_asset_urls(nasa_id)
        jpg_url = pick_best_jpg(urls)
        if not jpg_url:
            raise RuntimeError(f"No JPG found among assets for nasa_id={nasa_id}")
        selected_jpg_urls.append(jpg_url)

    print("Selected JPG URLs:")
    for u in selected_jpg_urls:
        print(" -", u)

    # скачування 2 jpg
    download_file(selected_jpg_urls[0], "mars_photo1.jpg")
    download_file(selected_jpg_urls[1], "mars_photo2.jpg")

    print("Done! Saved as mars_photo1.jpg and mars_photo2.jpg")


if __name__ == "__main__":
    main()
