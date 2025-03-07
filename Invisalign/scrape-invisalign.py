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

    browser.get("https://www.invisalign.fr/find-a-doctor")
    time.sleep(5)  # Tunggu halaman terbuka
    browser.maximize_window()

    # 3️⃣ Klik tombol dengan class "Close pop up
    try:
        btn_trouver_un_praticien = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-close"))
        )
        btn_trouver_un_praticien.click()
        print("✅ Tombol 'Close pop up' diklik!")
    except Exception as e:
        print(f"⚠️ Tombol 'Close pop up' tidak ditemukan atau tidak bisa diklik: {e}")

    try:
        agree_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, "truste-consent-button"))
        )
        agree_button.click()
        print("✅ Tombol 'Tour accepter' diklik!")
    except Exception as e:
        print(f"⚠️ Tombol 'Tour accepter' tidak ditemukan atau tidak bisa diklik: {e}")

    time.sleep(1)      

    return browser


def open_to_website(browser):
    browser.get("https://www.invisalign.fr/find-a-doctor#v=results&c=01&cy=fr&s=d")
    time.sleep(10)

    # Tunggu hingga elemen utama dl-search-form-frame muncul
    try:
        search_form = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "dl-results-pane"))
        )
        print("✅ Elemen utama 'dl-search-box' ditemukan!")
    except Exception as e:
        print(f"❌ Elemen 'dl-search-box' tidak ditemukan: {e}")
        return

    time.sleep(5)

    # Isi input lokasi dengan "02"
    try:
        location_input = WebDriverWait(search_form, 10).until(
            EC.presence_of_element_located((By.NAME, "location"))
        )

        location_input.click()
        location_input.clear()
        location_input.send_keys("02")
        location_input.send_keys(Keys.RETURN)

        print("✅ Input 'location' berhasil diisi dengan '02'!")
    except Exception as e:
        print(f"⚠️ Input 'location' tidak ditemukan atau tidak bisa diisi: {e}")

    time.sleep(5)

    # Klik tombol "Adolescents (moins de 19 ans)"
    try:
        btn_teenCheckbox = WebDriverWait(search_form, 10).until(
            EC.element_to_be_clickable((By.NAME, "teen"))
        )
        btn_teenCheckbox.click()
        print("✅ Tombol 'Adolescents (moins de 19 ans)' diklik!")
    except Exception as e:
        print(f"⚠️ Tombol 'Adolescents (moins de 19 ans)' tidak ditemukan atau tidak bisa diklik: {e}")

    time.sleep(5)

    # Klik tombol "Rechercher"
    try:
        rechercher_button = WebDriverWait(search_form, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Rechercher')]"))
        )
        rechercher_button.click()
        print("✅ Tombol 'Rechercher' berhasil diklik!")
    except Exception as e:
        print(f"⚠️ Tombol 'Rechercher' tidak ditemukan atau tidak bisa diklik: {e}")

    time.sleep(5)

    # Tunggu hingga elemen utama dl-search-form-frame muncul
    try:
        search_map = WebDriverWait(search_form, 10).until(
            EC.presence_of_element_located((By.ID, "dl-map-container"))
        )
        print("✅ Elemen utama 'Maps' ditemukan!")
    except Exception as e:
        print(f"❌ Elemen 'Maps' tidak ditemukan: {e}")
        return

    time.sleep(5)

    try:
        # Tunggu hingga semua ikon peta muncul
        map_buttons = WebDriverWait(search_map, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@role="button"]//img'))
        )

        print(f"🔍 Ditemukan {len(map_buttons)} ikon peta untuk diklik.")

        # Klik setiap ikon peta satu per satu
        for idx, button in enumerate(map_buttons, start=1):
            try:
                WebDriverWait(browser, 5).until(EC.element_to_be_clickable(button))
                button.click()
                print(f"✅ Ikon peta ke-{idx} diklik!")

                time.sleep(3)  # Tunggu agar dialog muncul

                try:
                    dialog = WebDriverWait(browser, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "gm-style-iw"))
                    )
                    print("✅ Dialog muncul!")

                    # Cari semua elemen "Plus de détails" dalam dialog
                    time.sleep(2)  # Beri waktu agar elemen termuat
                    links = dialog.find_elements(By.XPATH, "//a[contains(text(), 'Plus de détails')]")

                    if not links:
                        print("⚠️ Tidak ada link 'Plus de détails' yang ditemukan.")
                        continue  # Skip ke ikon peta berikutnya

                    print(f"🔍 Ditemukan {len(links)} link 'Plus de détails' dalam dialog.")

                    for link_idx, link in enumerate(links, start=1):
                        try:
                            # Scroll ke elemen agar terlihat
                            ActionChains(browser).move_to_element(link).perform()
                            time.sleep(1)

                            # Klik link "Plus de détails"
                            link.click()
                            print(f"🖱️ Mengklik link ke-{link_idx}...")

                            # Tunggu hingga tab baru terbuka
                            WebDriverWait(browser, 10).until(lambda d: len(d.window_handles) > 1)
                            
                            # Pindah ke tab baru
                            new_window = browser.window_handles[-1]
                            browser.switch_to.window(new_window)  

                            # Tunggu hingga halaman termuat dan cetak title
                            WebDriverWait(browser, 10).until(EC.title_contains(""))
                            print(f"📝 [{link_idx}] Title Halaman: {browser.title}")

                            # Tutup tab baru
                            browser.close()

                            # Kembali ke tab utama sebelum lanjut ke link berikutnya
                            browser.switch_to.window(browser.window_handles[0])
                            print(f"↩️ Kembali ke halaman utama setelah membuka link ke-{link_idx}.")

                            time.sleep(2)  # Jeda sebelum klik link berikutnya

                        except Exception as e:
                            print(f"⚠️ Gagal membuka link ke-{link_idx}: {e}")

                except Exception as e:
                    print("⚠️ Dialog tidak muncul setelah klik ikon peta.")

            except Exception as e:
                print(f"⚠️ Gagal mengklik ikon peta ke-{idx}: {e}")

    except Exception as e:
        print(f"⚠️ Tidak ditemukan ikon peta yang bisa diklik: {e}")


def main():
    browser = setup_browser()
    open_to_website(browser)
    time.sleep(10)
    browser.quit()


if __name__ == "__main__":
    main()
