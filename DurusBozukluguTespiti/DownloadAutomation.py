from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
import time

# Start ChromeDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Search at Google Images
query = "pectus carinatum"
search_url = f"https://www.google.com/search?q={query}&tbm=isch"
driver.get(search_url)
time.sleep(5)        # Wait the page to load

# Sayfayı aşağı kaydırarak daha fazla görsel yüklenmesini sağlama
for _ in range(20):  # İstenilen sayıda kaydır
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(2)

# Görsellerin URL'lerini bulma (CSS seçici kullanarak)
image_elements = driver.find_elements(By.CSS_SELECTOR, 'img[src], img[data-src]')
image_urls = []

for img in image_elements:
    try:
        # Sadece HTTP ile başlayan 'src' veya 'data-src' URL'lerini ekleyin
        src = img.get_attribute("src") or img.get_attribute("data-src")
        if src and src.startswith("http"):
            image_urls.append(src)
    except Exception as e:
        print(f"Görsel URL'si alınamadı: {e}")

print(f"{len(image_urls)} adet görsel bulundu.")

# İndirilecek klasörü belirleme
os.makedirs(f'{query}_images', exist_ok=True)

# Görselleri indirme
for i, url in enumerate(image_urls):
    try:
        # HTTP üzerinden gelen görselleri indirme
        response = requests.get(url, timeout=10)  # 10 saniye içinde yanıt bekleyin
        if response.status_code == 200:
            with open(f"{query}_images/{query}_{i}.jpg", 'wb') as f:
                f.write(response.content)
            print(f"{query}_{i}.jpg indirildi.")
        else:
            print(f"Görsel indirilemedi, durum kodu: {response.status_code}")
    except Exception as e:
        print(f"Görsel indirilemedi: {e}")

# Tarayıcıyı kapatma
driver.quit()
