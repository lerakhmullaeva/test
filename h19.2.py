# У venv Python встановіть Flask за допомогою команди pip install flask
# Створіть у окремій директорії файл арр.ру та скопіюйте у нього код файлу арр.ру який приведено нижче в початкових даних.
# Запустіть http сервер за допомогою команди python app.py
# Сервер стартує за базовою адресою http://127.0.0.1:8080
# Враховуючи документацію яку наведено нижче вам потрібно написати код, який використовуючи модуль request зробить через POST upload якогось зображення на сервер, 
# за допомогою GET отримає посилання на цей файл и потім за допомогою DELETE зробить видалення файлу з сервера.
# Документація для арр.pу
# Серверна частина надає можливість завантажувати, отримувати та видаляти зображення.
# - ЗАВАНТАЖЕННЯ зображення
# Метод: POST
# Шлях: /upload
# Опис: Завантажує зображення на сервер.
# Параметри запиту:
# - image: файл зображення (тип MIME: image/*)
# Відповідь:
# - Код стану 201 (Created) у разі успішного завантаження.
# - Повертає URL завантаженого зображення у форматі JSON:
# {
# "image_url": "<http://127.0.0.1:8080/uploads/exampLe.jpg>"
# }
# - ОТРИМАННЯ URL завантаженого зображення
# Метод: GET|
# Шлях: /Image/<filename>
# Опис: Повертає URL або саме зображення в залежності від заголовка Content-Type. ‹filenane› повинен бути вказаним враховуючи правила кодування ULR
# Відповідь:
# - Код стану 200 (OK)
# - Повертає URL завантаженого зображення у форматі JSON, якщо Content-Type рівний text:
# { 
# "image_url": "<http://127.0.0.1:8080/uploads/example.jpg>"
# }
# - Повертає саме зображення, якщо Content-Type рівний Image.
# - ВИДАЛЕННЯ зображення
# jsonCopy code
# {
# "message": "Image example.jpg перейменовано на new_example.jpg"
# }
# Метод: DELETE
# Шлях: /delete/‹filename>
# Опис: Видаляє завантажене зображення з серверу. <fiLename› повинен бути вказаним враховуючи правилакодування ULR
# Відповідь:
# - Код стану 200 (ОК) у разі успішного видалення.
# - Повертає повідомлення про успішне видалення у форматі JSON:
# {
# "image_url": "http://127.0.0.1:8080/uploads/example.jpg"
# }


import requests

BASE_URL = "http://127.0.0.1:8080"

# 1) POST /upload — завантажуємо зображення
with open("sample.jpg", "rb") as img:
    response = requests.post(
        f"{BASE_URL}/upload",
        files={"image": img}
    )

print("UPLOAD status:", response.status_code)
upload_data = response.json()
print("UPLOAD response:", upload_data)

# беремо filename з URL
image_url = upload_data["image_url"]
filename = image_url.split("/")[-1]

# 2) GET /image/<filename> — отримуємо URL (Content-Type = text)
response = requests.get(
    f"{BASE_URL}/image/{filename}",
    headers={"Content-Type": "text"}
)

print("GET status:", response.status_code)
print("GET response:", response.json())

# 3) DELETE /delete/<filename> — видаляємо файл
response = requests.delete(f"{BASE_URL}/delete/{filename}")

print("DELETE status:", response.status_code)
print("DELETE response:", response.json())


