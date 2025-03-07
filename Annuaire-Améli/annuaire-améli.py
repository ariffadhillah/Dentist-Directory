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
from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

def setup_browser():
    # Konfigurasi Chrome Options
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

    chrome_options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()

# Chirurgien-dentiste spécialiste en orthopédie dento-faciale

    browser.get("https://annuairesante.ameli.fr/nouvelle-recherche/professionnels-de-sante.html")
    time.sleep(5)  # Tunggu halaman terbuka
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



    # Isi input lokasi dengan "01"
    time.sleep(5)  
    send_keys = "01"
    try:
        location_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "ps_localisation"))
        )

        # Pastikan input dalam keadaan fokus
        location_input.click()
        time.sleep(1)  # Beri waktu sebelum membersihkan input

        # Bersihkan input dengan kombinasi yang lebih aman
        try:
            location_input.clear()  # Metode pertama
            location_input.send_keys(Keys.CONTROL + "a")  # Pilih semua teks
            location_input.send_keys(Keys.BACKSPACE)  # Hapus teks yang dipilih
        except Exception:
            print("⚠️ Gagal membersihkan input, melanjutkan pengisian...")

        time.sleep(1)  # Jeda sebelum memasukkan teks baru

        # Masukkan lokasi baru
        location_input.send_keys(send_keys)
        location_input.send_keys(Keys.RETURN)

        print(f"✅ Input lokasi berhasil diisi dengan '{send_keys}'!")

        # Tunggu perubahan setelah input dikirim
        time.sleep(5)  

    except Exception as e:
        print(f"⚠️ Input lokasi tidak ditemukan atau tidak bisa diisi: {e}")

    return browser


def proses_search(browser):
    try:
        time.sleep(3)
        search_result = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "centrecadre"))
        )
        print("✅ Elemen utama 'centrecadre' ditemukan!")
    except Exception:
        print("❌ Elemen 'centrecadre' tidak ditemukan!")
        return

    while True:
        try:
            time.sleep(3)

            # Cari semua elemen "item-professionnel"
            search_items = WebDriverWait(browser, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "item-professionnel"))
            )
            print(f"✅ Ditemukan {len(search_items)} elemen 'item-professionnel'!")

            for idx, item in enumerate(search_items, start=1):
                try:
                    nom_pictos_element = item.find_element(By.CLASS_NAME, "nom_pictos")
                    nom_pictos_text = nom_pictos_element.text.strip()
                    print(f"🔢 [{idx}] Nama ditemukan: {nom_pictos_text}")
                except Exception:
                    print(f"⚠️ [{idx}] Elemen 'nom_pictos' tidak ditemukan dalam item ini.")

            try:
                # Cek pagination untuk halaman berikutnya
                pagination = search_result.find_element(By.CLASS_NAME, "pagination")
                print("📌 Elemen pagination ditemukan!")

                try:
                    next_page_link = pagination.find_element(By.XPATH, './/a[img[contains(@alt, "Page suivante")]]')
                    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_page_link)
                    time.sleep(2)
                    next_page_link.click()
                    print("➡️ Beralih ke halaman berikutnya!")
                    WebDriverWait(browser, 10).until(
                        EC.presence_of_element_located((By.ID, "centrecadre"))
                    )
                    print("✅ Halaman baru berhasil dimuat!")
                except Exception:
                    print("🚫 Tidak ada halaman berikutnya! Selesai.")
                    break

            except Exception as e:
                print(f"❌ Kesalahan dalam pencarian data: {e}")
                break
        except:
            print("🚫 Tidak ada elemen 'item-professionnel' yang ditemukan! Selesai.")
            break


def main():
    browser = setup_browser()
    proses_search(browser)
    time.sleep(10)
    browser.quit()


if __name__ == "__main__":
    main()
