# import requests
# import json
# from bs4 import BeautifulSoup
# import csv
# import random
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from seleniumbase import Driver
# from selenium.webdriver.common.keys import Keys

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


#     chrome_options.add_argument(f"user-agent={random.choice(user_agents)}")

#     chrome_options = webdriver.ChromeOptions()
#     browser = webdriver.Chrome(options=chrome_options)
#     browser.maximize_window()

#     browser.get("https://www.invisalign.fr/find-a-doctor")
#     time.sleep(5)  # Tunggu halaman terbuka
#     browser.maximize_window()

#     time.sleep(5)  # Tunggu halaman terbuka

#     # 3️⃣ Klik tombol dengan class "Close pop up
#     try:
#         btn_trouver_un_praticien = WebDriverWait(browser, 10).until(
#             EC.element_to_be_clickable((By.CLASS_NAME, "btn-close"))
#         )
#         btn_trouver_un_praticien.click()
#         print("✅ Tombol 'Close pop up' diklik!")
#     except Exception as e:
#         print(f"⚠️ Tombol 'Close pop up' tidak ditemukan atau tidak bisa diklik: {e}")

#     time.sleep(5)  # Tunggu halaman terbuka

#     # 1️⃣ Klik tombol cookie persetujuan ("truste-consent-button")
#     try:
#         agree_button = WebDriverWait(browser, 10).until(
#             EC.element_to_be_clickable((By.ID, "truste-consent-button"))
#         )
#         agree_button.click()
#         print("✅ Tombol 'Tour accepter' diklik!")
#     except Exception as e:
#         print(f"⚠️ Tombol 'Tour accepter' tidak ditemukan atau tidak bisa diklik: {e}")


#     time.sleep(5)  # Tunggu halaman terbuka



#     # Tunggu hingga elemen utama dl-search-form-frame muncul
#     try:
#         search_form = WebDriverWait(browser, 10).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "dl-search-form-frame"))
#         )
#         print("✅ Elemen utama 'dl-search-form-frame' ditemukan!")
#     except Exception as e:
#         print(f"❌ Elemen 'dl-search-form-frame' tidak ditemukan: {e}")


#     time.sleep(5)  # Tunggu halaman terbuka

#     # 2️⃣ Isi input lokasi dengan "01"
#     try:
#         location_input = WebDriverWait(search_form, 10).until(
#             EC.presence_of_element_located((By.NAME, "location"))
#         )

#         location_input.click()
#         location_input.clear()
#         location_input.send_keys("01")
#         location_input.send_keys(Keys.RETURN)

#         print("✅ Input 'location' berhasil diisi dengan '01'!")
#     except Exception as e:
#         print(f"⚠️ Input 'location' tidak ditemukan atau tidak bisa diisi: {e}")
    
#     time.sleep(8)  # Tunggu halaman terbuka

#     # 3️⃣ Klik tombol dengan class "teenCheckbox"
#     try:
#         btn_teenCheckbox = WebDriverWait(browser, 10).until(
#             EC.element_to_be_clickable((By.NAME, "teen"))
#         )
#         btn_teenCheckbox.click()
#         print("✅ Tombol 'Adolescents (moins de 19 ans)' diklik!")
#     except Exception as e:
#         print(f"⚠️ Tombol 'Adolescents (moins de 19 ans)' tidak ditemukan atau tidak bisa diklik: {e}")
        
#     time.sleep(5)  # Tunggu halaman terbuka

#     # 3️⃣ Klik tombol dengan class "btn Trouver un praticien"
#     try:
#         rechercher_button = WebDriverWait(browser, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Rechercher')]"))
#         )
#         rechercher_button.click()
#         print("✅ Tombol 'Rechercher' berhasil diklik!")
#     except Exception as e:
#         print(f"⚠️ Tombol 'Rechercher' tidak ditemukan atau tidak bisa diklik: {e}")

#     # browser.refresh()
#     time.sleep(10)      

#     # return browser

# # def open_to_website(browser):
# #     browser.get("https://www.invisalign.fr/find-a-doctor#v=results&c=01&cy=fr&s=d")
# #     time.sleep(10)


# def main():
#     browser = setup_browser()
#     # open_to_website(browser)
#     time.sleep(50)
#     browser.quit()

# if __name__ == "__main__":
#     main()





import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()

    browser.get("https://www.invisalign.fr/find-a-doctor")
    time.sleep(5)  # Tunggu halaman terbuka

    # Klik tombol "Close pop up"
    try:
        btn_close_popup = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-close"))
        )
        btn_close_popup.click()
        print("✅ Tombol 'Close pop up' diklik!")
    except Exception:
        print("⚠️ Tombol 'Close pop up' tidak ditemukan atau tidak bisa diklik.")

    # Klik tombol "Tour accepter"
    try:
        agree_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "truste-consent-button"))
        )
        agree_button.click()
        print("✅ Tombol 'Tour accepter' diklik!")
    except Exception:
        print("⚠️ Tombol 'Tour accepter' tidak ditemukan atau tidak bisa diklik.")

    return browser


# Fungsi untuk mengklik tombol zoom in atau zoom out
def click_zoom_button(browser, label, times):
    try:
        zoom_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//button[@aria-label='{label}' or @title='{label}']"))
        )

        for i in range(times):
            zoom_button.click()
            print(f"✅ {label} klik ke-{i+1} berhasil!")
            time.sleep(1)  # Beri jeda agar efek zoom selesai

        print(f"✅ {label} berhasil diklik {times} kali!")

    except Exception as e:
        print(f"⚠️ Gagal mengklik tombol {label}: {e}")




def open_to_website(browser):
    browser.get("https://www.invisalign.fr/find-a-doctor#v=results&c=01&cy=fr&s=d")
    time.sleep(5)

    # Tunggu hingga elemen hasil pencarian muncul
    try:
        search_form = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "dl-results-pane"))
        )
        print("✅ Elemen utama 'dl-results-pane' ditemukan!")
    except Exception:
        print("❌ Elemen 'dl-results-pane' tidak ditemukan!")
        return


    time.sleep(2)

    # Isi input lokasi dengan "02"
    send_keys = "02"
    try:
        location_input = WebDriverWait(search_form, 10).until(
            EC.presence_of_element_located((By.NAME, "location"))
        )

        # Pastikan input dalam keadaan fokus
        location_input.click()
        time.sleep(1)  # Beri waktu sebelum membersihkan input

        # Bersihkan input menggunakan metode tambahan
        location_input.clear()  # Metode pertama
        location_input.send_keys(Keys.CONTROL + "a")  # Pilih semua teks
        location_input.send_keys(Keys.BACKSPACE)  # Hapus teks yang dipilih
        time.sleep(1)  # Jeda sebelum memasukkan teks baru

        # Masukkan lokasi baru
        location_input.send_keys(send_keys)
        location_input.send_keys(Keys.RETURN)

        print("✅ Input lokasi berhasil diisi dengan '02'!")
    except Exception as e:
        print(f"⚠️ Input lokasi tidak ditemukan atau tidak bisa diisi: {e}")


    time.sleep(5)

    # Klik checkbox "Adolescents (moins de 19 ans)"
    try:
        btn_teen_checkbox = search_form.find_element(By.NAME, "teen")
        btn_teen_checkbox.click()
        print("✅ Tombol 'Adolescents (moins de 19 ans)' diklik!")
    except Exception:
        print("⚠️ Tombol 'Adolescents (moins de 19 ans)' tidak ditemukan!")

    time.sleep(5)

    # Klik tombol "Rechercher"
    try:
        rechercher_button = search_form.find_element(By.XPATH, "//a[contains(text(), 'Rechercher')]")
        rechercher_button.click()
        print("✅ Tombol 'Rechercher' berhasil diklik!")
    except Exception:
        print("⚠️ Tombol 'Rechercher' tidak ditemukan!")

    time.sleep(5)

    # Tunggu hingga elemen Maps muncul
    try:
        search_map = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "dl-map-container"))
        )
        print("✅ Elemen utama 'Maps' ditemukan!")
    except Exception:
        print("❌ Elemen 'Maps' tidak ditemukan!")
        return

    time.sleep(5)


                # width: 100vw !important;
                # height: 100vh !important;
                # position: fixed !important;
                # top: 0 !important;
                # left: 0 !important;
                # z-index: 9999 !important;
                # max-width: 1916px;
                # max-height: 2000px;
                # # width: 100% !important;
                # # max-width: 1880px !important;
    css_script = """
    var style = document.createElement('style');
    style.innerHTML = `
        @media (min-width: 1200px) {
            .dl-root .dl-map-container {
                height: 100vh !important;
                # height: 638px;
            }
            .dl-results-pane {
                width: 100%;
                max-width: 1916px;
                max-height: 2000px;
                height: 100%;
                position: fixed !important;
                top: 0 !important;
                left: 0 !important;
                z-index: 9999 !important;
            }
            .Footer_cookieManager__JriPH,
            .Footer_copyright__gTNqp,
            .dl-root.eu .dl-results-top-tile,
            .Footer_secondRow__n0mgo,
            .Footer_floatRow___Vs1v,
            .Default_root__yo2mK,
            .Default_root__yo2mK,
            .dl-root.eu .dl-filter-header-row,
            .Header_sticky-visible__wwz7A {
                display: none !important;
            }
        }
    `;
    document.head.appendChild(style);
    """
    browser.execute_script(css_script)
    print("✅ CSS berhasil ditambahkan untuk '.dl-results-pane'!")


    # Sembunyikan semua '.container-fluid' kecuali yang pertama
    hide_script = """
    var containers = document.querySelectorAll('.container-fluid');
    containers.forEach((container, index) => {
        if (index > 0) {
            container.style.display = 'none';
        }
    });
    """
    browser.execute_script(hide_script)
    print("✅ Semua '.container-fluid' kecuali yang pertama telah disembunyikan!")


    click_zoom_button(browser, "Zoom avant", 2)

    # Klik ikon peta
    try:
        map_buttons = WebDriverWait(search_map, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@role="button"]//img'))
        )

        print(f"🔍 Ditemukan {len(map_buttons)} ikon peta.")
        

        for idx, button in enumerate(map_buttons, start=1):
            try:

                WebDriverWait(browser, 5).until(EC.element_to_be_clickable(button))                
                
                browser.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", button)
                time.sleep(2)  # Jeda agar peta bergeser


                button.click()
                print(f"✅ Ikon peta ke-{idx} diklik!")
                time.sleep(3)

                try:
                    dialog = WebDriverWait(browser, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "gm-style-iw"))
                    )

                    print("✅ Dialog muncul!")

                    links = dialog.find_elements(By.XPATH, "//a[contains(text(), 'Plus de détails')]")

                    if not links:
                        print("⚠️ Tidak ada link 'Plus de détails' yang ditemukan.")
                        continue

                    print(f"🔍 Ditemukan {len(links)} link 'Plus de détails'.")

                    for link_idx, link in enumerate(links, start=1):
                        try:
                            ActionChains(browser).move_to_element(link).perform()
                            time.sleep(5)
                            link.click()
                            print(f"🖱️ Klik link ke-{link_idx}...")

                            time.sleep(5)
                            WebDriverWait(browser, 10).until(lambda d: len(d.window_handles) > 1)

                            new_window = browser.window_handles[-1]
                            browser.switch_to.window(new_window)

                            time.sleep(5)
                            WebDriverWait(browser, 10).until(EC.title_contains(""))
                            print(f"📝 [{link_idx}] Title: {browser.title}")

                            browser.close()
                            browser.switch_to.window(browser.window_handles[0])
                            print(f"↩️ Kembali ke halaman utama.")

                            time.sleep(2)

                        except Exception:
                            print(f"⚠️ Gagal membuka link ke-{link_idx}.")                    
                    

                    try:
                        btn_close_popup_dialog = WebDriverWait(browser, 5).until(
                            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Fermer' or @title='Fermer']"))
                        )
                        btn_close_popup_dialog.click()
                        print("✅ Tombol 'Close dialog Fermer' diklik!")
                    except Exception:
                        print("⚠️ Tombol 'Close dialog Fermer' tidak ditemukan atau tidak bisa diklik.")
                    
                    # click_zoom_button(browser, "Zoom arrière", 3)


                except Exception:
                    print("⚠️ Dialog tidak muncul!")

            except Exception:
                print(f"⚠️ Gagal mengklik ikon peta ke-{idx}!")

    except Exception:
        print("⚠️ Tidak ada ikon peta yang bisa diklik!")


def main():
    browser = setup_browser()
    open_to_website(browser)
    time.sleep(5)
    browser.quit()


if __name__ == "__main__":
    main()
