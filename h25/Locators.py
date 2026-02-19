from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


# Слова, які будемо вводити
words = ["Selenium", "Python", "Automation", "Testing", "Google Search"]

# Сюди будемо складати результати парсингу
all_results = []

# Запуск Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.google.com/")

# Приймаємо cookies якщо є
try:
    time.sleep(2)
    agree_btn = driver.find_element(By.XPATH, "//button//div[text()='Прийняти все' or text()='Accept all']")
    agree_btn.click()
except:
    pass


# Знаходимо поле пошуку (можна будь-який варіант, але залишимо найкращий)
search_box = driver.find_element(By.NAME, "q")


# Для кожного слова: вводимо, шукаємо, парсимо
for word in words:
    search_box.send_keys(word)
    search_box.send_keys(Keys.ENTER)
    time.sleep(3)

    # Парсимо всі блоки результатів
    results = driver.find_elements(By.CSS_SELECTOR, "div.tF2Cxc")

    print(f"\n========== Results for: {word} ==========")

    for r in results:
        try:
            title = r.find_element(By.TAG_NAME, "h3").text
        except:
            title = "No title"

        try:
            link = r.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        except:
            link = "No link"

        try:
            desc = r.find_element(By.CSS_SELECTOR, "div.VwiC3b").text
        except:
            desc = "No description"

        print("Title:", title)
        print("Link:", link)
        print("Description:", desc)
        print("-" * 60)

        all_results.append({
            "search_word": word,
            "title": title,
            "link": link,
            "description": desc
        })

    # Повертаємось назад на Google головну
    driver.get("https://www.google.com/")
    time.sleep(2)

    # знову шукаємо поле пошуку (бо сторінка перезавантажилась)
    search_box = driver.find_element(By.NAME, "q")
    # search_box = driver.find_element(By.ID, "APjFqb")
    # search_box = driver.find_element(By.CLASS_NAME, "gLFyf")
    # search_box = driver.find_element(By.CSS_SELECTOR, "#APjFqb")
    # search_box = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')

    # очищення (на всякий випадок)
    search_box.clear()


# Зберігаємо у файл
with open("google_results.txt", "w", encoding="utf-8") as f:
    for item in all_results:
        f.write(f"SEARCH WORD: {item['search_word']}\n")
        f.write(f"TITLE: {item['title']}\n")
        f.write(f"LINK: {item['link']}\n")
        f.write(f"DESCRIPTION: {item['description']}\n")
        f.write("=" * 70 + "\n")

print("\nSaved results to google_results.txt")

# Закриваємо браузер
driver.quit()
