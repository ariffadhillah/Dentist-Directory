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
from selenium.common.exceptions import TimeoutException
from seleniumbase import Driver
from selenium_stealth import stealth

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
    """Mengatur browser dengan proxy, User-Agent, dan stealth mode"""
    chrome_options = Options()

    # Menambahkan proxy acak
    proxy = get_random_proxy()
    chrome_options.add_argument(f"--proxy-server={proxy}")

    # Menambahkan User-Agent acak
    user_agent = random.choice(user_agents)
    chrome_options.add_argument(f"user-agent={user_agent}")

    # Mengaktifkan mode stealth
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-extensions")

    # Inisialisasi browser dengan stealth
    browser = webdriver.Chrome(options=chrome_options)
    stealth(
        browser,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    # # Buka halaman awal
    # browser.get("https://www.doctolib.fr")

    browser = Driver(uc=True)
    url = "https://www.doctolib.fr"
    browser.uc_open_with_reconnect(url, 4)
    browser.uc_gui_click_captcha()
    browser.maximize_window()


    time.sleep(random.uniform(4, 10))

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
    time.sleep(random.uniform(4, 10))

    return browser

def open_to_website(browser, profile_slug):
    csv_filename = 'Doctolib.csv'

    # Jika file tidak ada, buat dengan header
    try:
        pd.read_csv(csv_filename)
    except FileNotFoundError:
        pd.DataFrame(columns=["Name", "Spécialité", "Address", "Telephone"]).to_csv(
            csv_filename, index=False, encoding='utf-8-sig', mode="w"
        )

    """Membuka URL berdasarkan profile_slug dan mengambil JSON"""
    url = f"https://www.doctolib.fr/online_booking/api/slot_selection_funnel/v1/info.json?profile_slug={profile_slug}"
    
    # Percobaan ulang jika terdeteksi sebagai bot
    retries = 3
    while retries > 0:
        browser.get(url)
        time.sleep(random.uniform(4, 10))  # Randomized delay

        try:
            # Ambil teks JSON dari halaman
            json_text = browser.find_element(By.TAG_NAME, "pre").text
            json_data = json.loads(json_text)

            # Ambil data yang diminta
            profile = json_data.get("data", {}).get("profile", {})
            places = json_data.get("data", {}).get("places", [{}])[0]

            # Ambil informasi yang dibutuhkan
            name = profile.get("name_with_title", "N/A")
            title = profile.get("subtitle", "N/A")
            place_name = places.get("address", "N/A")
            city = places.get("city", "N/A")
            zipcode = places.get("zipcode", "N/A")
            officePhone = places.get("landline_number", "N/A")

            # Tampilkan hasil
            print(f"Nama        : {name}")
            print(f"Title       : {title}")
            print(f"Tempat      : {place_name}")
            print(f"Kota        : {city}")
            print(f"Kode Pos    : {zipcode}")
            print(f"Telepon     : {officePhone}")
            print("=" * 80)

            # Simpan hasil ke CSV langsung setelah diproses
            df = pd.DataFrame([{
                'Name': name,
                'Spécialité': title,
                'Address': f"{place_name}, {zipcode}, {city}",
                'Telephone': f"'{officePhone}"
            }])

            df.to_csv(csv_filename, index=False, encoding='utf-8-sig', mode="a", header=False)
            print(f"Data {profile_slug} berhasil disimpan ke CSV.")
            break  # Keluar dari loop jika berhasil

        except Exception as e:
            retries -= 1
            print(f"Percobaan gagal ({3 - retries}/3). Error: {e}")
            if retries > 0:
                print("Menunggu sebelum mencoba lagi...")
                time.sleep(random.uniform(10, 20))  # Delay sebelum mencoba kembali
            else:
                print(f"Gagal mengambil data untuk {profile_slug} setelah 3 kali percobaan.")

def main():
    # Load CSV yang berisi daftar profile_slug
    df = pd.read_csv("hasil-scraping-name-doctor.csv")

    if "profile_slug" not in df.columns:
        print("Kolom 'profile_slug' tidak ditemukan di CSV!")
        return

    profile_slugs = df["profile_slug"].dropna().tolist()

    # Inisialisasi browser
    browser = setup_browser()

    for slug in profile_slugs:
        print(f"Membuka data untuk: {slug}")
        open_to_website(browser, slug)

    print("Scraping selesai.")
    browser.quit()

if __name__ == "__main__":
    main()
