import requests
import json
from bs4 import BeautifulSoup
import csv
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
from random import uniform

def setup_browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-extensions")

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
    ]

    chrome_options.add_argument(f"user-agent={random.choice(user_agents)}")
    browser = webdriver.Chrome(options=chrome_options)
    browser.get("https://annuairesante.ameli.fr/nouvelle-recherche/professionnels-de-sante.html")
    time.sleep(5)
    browser.maximize_window()

    try:
        btn_trouver_un_praticien = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Liste des professions')]"))
        )
        btn_trouver_un_praticien.click()
        print("✅ Tombol 'Liste des professions' diklik!")
    except Exception as e:
        print(f"⚠️ Tombol 'Liste des professions' tidak ditemukan atau tidak bisa diklik: {e}")

    # Tunggu hingga elemen Maps muncul
    try:
        pop_ups = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "popin"))
        )
        print("✅ Elemen utama 'open Pop up propesiaonal' ditemukan!")
    except Exception:
        print("❌ Elemen 'no open pop pus' tidak ditemukan!")
        return
    
    time.sleep(5) 
    
    # 3️⃣ Klik tombol dengan class "Close pop up
    try:
        select_items = WebDriverWait(pop_ups, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Chirurgien-dentiste spécialiste en orthopédie dento-faciale')]"))
        )
        select_items.click()
        print("✅ Tombol 'Chirurgien-dentiste spécialiste en orthopédie dento-faciale' diklik!")
    except Exception as e:
        print(f"⚠️ Tombol 'Chirurgien-dentiste spécialiste en orthopédie dento-faciale' tidak ditemukan atau tidak bisa diklik: {e}")

    time.sleep(5) 

    try:
        radio_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, "formCarteVitaleOui"))
        )
        radio_button.click()
        print("✅ Radio button 'Carte Vitale' berhasil diklik!")
    except Exception as e:
        print(f"⚠️ Radio button 'Carte Vitale' tidak ditemukan atau tidak bisa diklik: {e}")

    return browser

def input_location(browser, location):
    try:
        location_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "ps_localisation"))
        )
        location_input.click()
        time.sleep(1)
        location_input.clear()
        location_input.send_keys(Keys.CONTROL + "a")
        location_input.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        location_input.send_keys(location)
        location_input.send_keys(Keys.RETURN)
        print(f"✅ Input lokasi berhasil diisi dengan '{location}'!")
        time.sleep(5)

    except Exception as e:
        print(f"⚠️ Input lokasi tidak ditemukan atau tidak bisa diisi: {e}")

def klik_modifier_recherche(browser):
    try:
        btn_modifier = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/modifier_votre_recherche.html')]"))
        )
        btn_modifier.click()
        print("🔄 Kembali ke halaman pencarian!")
        time.sleep(5)
    except Exception as e:
        print(f"⚠️ Tombol 'Modifier votre recherche' tidak ditemukan atau tidak bisa diklik: {e}")

def proses_search(browser, location):
    csv_filename = "Annuaire Améli.csv"

    if location == "01":
        pd.DataFrame(columns=["ZIP", "Name", "Professions", "Telephone", "Address"]).to_csv(
            csv_filename, index=False, encoding='utf-8-sig', mode="w"
        )

    page_data = []
    while True:
        try:
            time.sleep(3)
            html = browser.page_source
            soup = BeautifulSoup(html, "html.parser")

            # Temukan semua item hasil pencarian
            search_items = soup.find_all("div", class_="item-professionnel")

            for idx, item in enumerate(search_items, start=1):
                try:
                    # Mengambil Nama
                    nama_element = item.select_one(".nom_pictos h2 a")
                    nama_text = nama_element.get_text(strip=True) if nama_element else "Tidak ditemukan"

                    # Mengambil Spesialisasi
                    specialite_element = item.select_one(".item.left.specialite")
                    specialite_text = specialite_element.get_text(strip=True) if specialite_element else "Tidak ditemukan"

                    # Mengambil Nomor Telepon
                    telp_element = item.select_one(".item.left.tel")
                    telp_text = telp_element.get_text(strip=True).replace("\xa0", " ") if telp_element else "Tidak ditemukan"

                    # Mengambil Alamat
                    alamat_element = item.select_one(".item.left.adresse")
                    alamat_text = alamat_element.get_text(separator=", ", strip=True) if alamat_element else "Tidak ditemukan"

                    print(f"🔢 [{idx}] Nama: {nama_text}")
                    print(f"📌 [{idx}] Spesialisasi: {specialite_text}")
                    print(f"📞 [{idx}] Telephone: {telp_text}")
                    print(f"📍 [{idx}] Alamat: {alamat_text}\n")

                    data = {
                        'ZIP': "'" + location,
                        'Name': nama_text,
                        'Professions': specialite_text,
                        'Telephone': "'"+telp_text,
                        "Address": alamat_text
                    }           

                    page_data.append(data)

                except Exception as e:
                    print(f"⚠️ [{idx}] Error dalam memproses item: {e}")

            df = pd.DataFrame(page_data)
            df.to_csv(csv_filename, index=False, encoding='utf-8-sig', mode="a", header=False)

            time.sleep(uniform(2, 5))

            # Mencari pagination menggunakan BeautifulSoup
            pagination = soup.find("div", class_="pagination")
            if pagination:
                next_page_link = pagination.find("a", alt="Page suivante")
                if next_page_link:
                    next_url = next_page_link["href"]
                    browser.get(next_url)
                    print("➡️ Beralih ke halaman berikutnya!")
                    time.sleep(5)
                    continue

            print("🚫 Tidak ada halaman berikutnya! Selesai.")
            break

        except Exception as e:
            print(f"🚫 Kesalahan saat mencari elemen: {e}")
            break

def main():
    browser = setup_browser()
    for location in range(1, 96):
        location_code = str(location).zfill(2)
        input_location(browser, location_code)
        proses_search(browser, location_code)
        klik_modifier_recherche(browser)
    browser.quit()

if __name__ == "__main__":
    main()
