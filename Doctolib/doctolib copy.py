# import requests
# import json
# from bs4 import BeautifulSoup
# import csv
# import random
# import time
# import pandas as pd
# from random import uniform
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
# from seleniumbase import Driver

# from selenium.webdriver.common.action_chains import ActionChains

# def setup_browser():
#     # Konfigurasi Chrome Options
#     chrome_options = Options()
#     chrome_options.add_argument("--disable-infobars")
#     chrome_options.add_argument("start-maximized")
#     chrome_options.add_argument("--disable-extensions")

#     user_agents = [
#         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
#         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
#         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
#         "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
#     ]
#     proxy = get_random_proxy()
#     chrome_options = Options()
#     chrome_options.add_argument(f"--proxy-server={proxy}")
#     chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
#     chrome_options.add_argument("--disable-blink-features=AutomationControlled")

#     chrome_options.add_argument(f"user-agent={random.choice(user_agents)}")


#     # chrome_options.add_argument(
#     #     "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
#     # )
    

#     proxy_list = [
#         "85.215.64.49:80",
#         "219.65.73.81:80",
#         "50.223.246.237:80",
#         "50.207.199.87:80",
#         "41.207.187.178:80",
#         "44.218.183.55:80",
#         "44.195.247.145:80",
#         "50.207.199.83:80",
#         "50.174.7.153:80",
#         "50.202.75.26:80",
#         "50.169.37.50:80",
#         "50.232.104.86:80",
#         "50.239.72.16:80",
#         "50.221.74.130:80",
#         "203.115.101.51:80"
#     ]

#     random_proxy = random.choice(proxy_list)

#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument(f"--proxy-server={random_proxy}")
#         # Inisialisasi browser
#     browser = webdriver.Chrome(options=chrome_options)
#     browser.maximize_window()



#     # Buka halaman awal
#     browser = Driver(uc=True)
#     url = "https://www.doctolib.fr"
#     # browser.get("https://www.doctolib.fr/")
#     time.sleep(5)  # Tunggu halaman terbuka
#     browser.uc_open_with_reconnect(url, 4)
#     browser.uc_gui_click_captcha()
#     browser.maximize_window()
    


#     # Tambahkan cookies
#     # cookies = [
#     #     {"name":"_doctolib_session","value":"4bbsrOB3sB9wZTfk7imlfBJCVfzq6GWhUJrpfl%2F%2BI4MB3yCIzKYDF59sNmnIK%2BBQIN7z5WSZgYAPPq4to3ykg1qIrkQnNfK4g0BVRyP6ridjjvtSrmCcdqxu5tWKKrRhlC4hUegWGGjcK3KTB1RQJLGiPhGQCbX6KSgFV8guXe9dzgCIfY6KpwfuICqWTgGl3DBVFFJX6iT4GZx6HTB3cJA94pV6c0%2FVJdQ82xgTw4zVIURsbg8YR9qS1DxtAYj3XgkV8KsK9Po2DbDvqXXE%2Fvw9GM1z2TphxbzjPFMhWawAcEjoPNfbQj%2F6qgsT4Lk1vsvWxp5azj0jdEDaNtCE4%2BV6tLrZF2E0ng%3D%3D--PxUD4wW0nSpaRxsh--tUkgw4dMFd384dYwMhpubQ%3D%3D"}

#     # ]

#     # Coba klik tombol dengan ID "didomi-notice-agree-button"
#     try:
#         agree_button = WebDriverWait(browser, 10).until(
#             EC.element_to_be_clickable((By.ID, "didomi-notice-agree-button"))
#         )
#         agree_button.click()
#         print("Tombol cookie 'didomi-notice-agree-button' diklik!")
#     except Exception as e:
#         print(f"Tombol cookie tidak ditemukan atau tidak bisa diklik: {e}")




#     # for cookie in cookies:
#     #     browser.add_cookie(cookie)

#     browser.refresh()
#     time.sleep(10)      

#     return browser

import requests
import json
from bs4 import BeautifulSoup
import csv
import random
import time
import pandas as pd
from random import uniform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from seleniumbase import Driver
from selenium.webdriver.common.action_chains import ActionChains


# Daftar proxy gratis yang akan dipilih secara acak
proxy_list = [
"173.212.216.227:8118",
"207.180.254.198:80",
"51.158.125.47:16379",
"80.15.216.57:80"
]

# Daftar User-Agent untuk menghindari deteksi bot
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
]

def get_random_proxy():
    """Pilih proxy secara acak dari daftar proxy."""
    return random.choice(proxy_list)

def setup_browser():
    """Mengatur browser dengan proxy dan User-Agent secara acak"""
    chrome_options = Options()

    # Menambahkan proxy acak
    proxy = get_random_proxy()
    chrome_options.add_argument(f"--proxy-server={proxy}")

    # Menambahkan User-Agent acak
    user_agent = random.choice(user_agents)
    chrome_options.add_argument(f"user-agent={user_agent}")

    # Menyembunyikan deteksi bot Selenium
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-extensions")

    # Inisialisasi browser
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()

    # Buka halaman awal dengan Seleniumbase (Undetected Chrome)
    browser = Driver(uc=True)
    url = "https://www.doctolib.fr"
    browser.uc_open_with_reconnect(url, 4)
    browser.uc_gui_click_captcha()
    browser.maximize_window()

    # Coba klik tombol cookie jika ada
    try:
        agree_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, "didomi-notice-agree-button"))
        )
        agree_button.click()
        print("Tombol cookie 'didomi-notice-agree-button' diklik!")
    except Exception as e:
        print(f"Tombol cookie tidak ditemukan atau tidak bisa diklik: {e}")

    # Refresh browser setelah menambahkan cookies
    browser.refresh()
    time.sleep(10)

    return browser

# Contoh penggunaan:


def open_to_website(browser):
    browser.get("https://www.doctolib.fr/orthodontiste/directory")
    time.sleep(5)

    # Klik tombol cookie jika ada
    try:
        agree_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, "didomi-notice-agree-button"))
        )
        agree_button.click()
        print("✅ Tombol cookie diklik!")
    except Exception as e:
        print(f"⚠️ Tombol cookie tidak ditemukan atau tidak bisa diklik: {e}")

    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "seo-directory-location-main-block"))
        )

        urls = []
        blocks = browser.find_elements(By.CLASS_NAME, "seo-directory-location-main-block")

        # Loop untuk mendapatkan teks dan URL dari setiap link di dalam block
        for block in blocks:
            links = block.find_elements(By.TAG_NAME, "a")
            for link in links:
                href = link.get_attribute("href")
                text_name = link.text.strip()  # Mengambil teks dari elemen <a>

                if href and (text_name, href) not in urls:
                    urls.append((text_name, href))  # Simpan sebagai tuple (text_name, href)

        # Menampilkan hasil dengan teks dan URL
        print(f"🔍 Ditemukan {len(urls)} URL, membuka halaman satu per satu...\n")
# sekarang 90
        start_index = 104
        csv_filename = f"Name_Doctor-{start_index}.csv"
        pd.DataFrame(columns=["City", "URL"]).to_csv(csv_filename, index=False, encoding='utf-8-sig', mode="w")

        for idx, (text_name, url) in enumerate(urls, start=1):
            if idx < start_index:
                continue  # Lewati URL sebelum indeks ke-5

        # for idx, (text_name, url) in enumerate(urls, start=1):
            # time.sleep(uniform(2, 5))
            time.sleep(5)
            browser.get(url)
            # time.sleep(uniform(2, 5))
            time.sleep(5)
            print(f"=== 🔎 Page {idx} - {text_name} ===")
            print(f"URL: {url}\n")

            page_data = []
            while True:  # Loop untuk pagination
                time.sleep(5)
                try:
                    search_result = WebDriverWait(browser, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, ".dl-layout-body.dl-layout-body-bottom.dl-layout-body-size-normal"))
                    )
                    time.sleep(uniform(5, 7))

                    try:
                        doctor_info = search_result.find_elements(By.CLASS_NAME, "responsive-doctor-border")

                        for i, doctor in enumerate(doctor_info, start=1):
                            try:
                                link_element = doctor.find_element(By.TAG_NAME, "a")
                                href = link_element.get_attribute("href")
                                # title_name = link_element.text.strip()  # Mengambil teks di dalam elemen <a>

                                if href:  # Pastikan URL tidak kosong
                                    print(f"🔗 Link {i}: {href}")  # Menampilkan URL
                                    # print(f"📝 Teks: {title_name}\n")  # Menampilkan teks dari link

                                    data = {'City': text_name, 'URL': href}  
                                    if data not in page_data:  # Hindari duplikasi
                                        page_data.append(data)

                            except Exception as e:
                                print(f"⚠️ Doctor {i} - Tidak ada link ditemukan: {e}")

                        if page_data:
                            df = pd.DataFrame(page_data)
                            df.to_csv(csv_filename, index=False, encoding='utf-8-sig', mode="a", header=False)

                        # time.sleep(uniform(2, 5))
                        time.sleep(5)


                        try:
                            next_button = WebDriverWait(browser, 10).until(
                                EC.presence_of_element_located((By.CLASS_NAME, "next-link"))
                            )

                            if next_button.get_attribute("disabled") is not None:
                                print("🚫 Tombol 'Next' tidak aktif! Selesai.")
                                break

                            browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_button)
                            time.sleep(5)
                            next_button.click()
                            print("➡️ Beralih ke halaman berikutnya!")

                            WebDriverWait(browser, 10).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, ".dl-layout-body.dl-layout-body-bottom.dl-layout-body-size-normal"))
                            )

                        except TimeoutException:
                            print("🚫 Tidak ada halaman berikutnya! Selesai.")
                            break
                        except StaleElementReferenceException:
                            print("⚠️ Elemen tidak lagi tersedia, mungkin halaman telah berubah.")

                    except Exception as e:
                        print(f"❌ Doctor Info tidak ditemukan di halaman {idx}: {url} - {e}")

                except Exception as e:
                    print(f"🚫 Tidak ada elemen 'search_result' yang ditemukan: {e}")
                    break

            print("=" * 50)

    except Exception as e:
        print(f"❌ Elemen tidak ditemukan: {e}")



def main():
    browser = setup_browser()
    open_to_website(browser)
    time.sleep(50)
    browser.quit()

if __name__ == "__main__":
    main()


# https://www.doctolib.fr/online_booking/api/slot_selection_funnel/v1/info.json?profile_slug=emmanuel-bocquet