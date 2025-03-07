import requests
import pandas as pd
import time
from bs4 import BeautifulSoup
from random import uniform

# Simpan semua data di list
all_data = []

# Headers dan cookies 
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}
cookies = {
    'cookie': '_gid=GA1.2.81135835.1740936846; _hjSessionUser_2353692=eyJpZCI6IjkyMmMzYWQ0LTUzYzUtNWUyMi05NmNmLTMwZjIwZWRjMjcxOSIsImNyZWF0ZWQiOjE3NDA5MzY4NDQzMzksImV4aXN0aW5nIjp0cnVlfQ==; PHPSESSID=7mvvlt35lfnsip9rsphe1kf1dn; _hjSession_2353692=eyJpZCI6IjJjZjc3NWQ5LTU5ZDItNDRlZC04YzUzLTYxZGYzOGYxYmE3YSIsImMiOjE3NDEwMTY0MjcyODIsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowfQ==; _ga_3L4PHV1SWR=GS1.1.1741016421.5.1.1741016467.14.0.0; _ga=GA1.2.1986518598.1740936844'
}


# Nama file CSV
csv_filename = "Annuaire Dentaire--1.csv"

# Inisialisasi file CSV dengan header jika belum ada
pd.DataFrame(columns=["Name", "Praticiens", "Address", "Telephone", "URL/Web"]).to_csv(csv_filename, index=False, encoding='utf-8-sig', mode="w")

# Base URL
base_url = 'https://annuairedentaire.com/annuaire/chirurgiens-dentistes/odf?page='

# Mulai dari halaman 1
page = 89

while True:
    url = base_url + str(page)
    print(f"🔄 Scraping halaman {page}: {url}")

    # Request ke halaman
    response = requests.get(url, headers=headers, cookies=cookies)
    if response.status_code != 200:
        print(f"❌ Gagal mengakses {url}")
        break  # Hentikan jika error

    soup = BeautifulSoup(response.content, 'html.parser')

    # Cek apakah ada daftar dokter di halaman ini
    links = [
        'https://annuairedentaire.com' + item.find('a')['href']
        for item in soup.find_all('div', class_='card-list card-anden')
    ]

    if not links:
        print("✅ Semua halaman telah diproses.")
        break  # Hentikan jika tidak ada lagi dokter (pagination habis)

    page_data = []  # Simpan data per halaman

    # Proses setiap link detail dokter
    for link in links:
        response = requests.get(link, headers=headers, cookies=cookies)
        soup = BeautifulSoup(response.content, 'html.parser')

        page_link = soup.find('div', class_='main-content fiche-cd')
        if not page_link:
            print(f"⚠️ 'main-content fiche-cd' div not found on {link}")
            continue

        col_div = page_link.find('div', class_='col-lg-16 col-24')
        if not col_div:
            print(f"⚠️ 'col-lg-16 col-24' div not found on {link}")
            continue

        # Nama dan Praticiens
        name = col_div.find('h1')
        praticiens = col_div.find('h2')

        name_text = name.text.strip() if name else "⚠️ Name not found"
        praticiens_text = praticiens.text.strip().replace('\n', ' ') if praticiens else "⚠️ Praticiens not found"

        # Address (Menggabungkan semua text dalam <p>)
        address_tag = col_div.find('i', class_='icon-fiche-adresse')
        address = "⚠️ Address not found"
        if address_tag:
            address_p = address_tag.find_parent('p')
            if address_p:
                address = " ".join(address_p.stripped_strings)

        # Telephone
        telephone_tag = col_div.find('i', class_='icon-fiche-telephone')
        telephone = telephone_tag.find_next_sibling(string=True).strip() if telephone_tag else "⚠️ Telephone not found"

        # URL Web
        web_url_tag = col_div.find('i', class_='icon-fiche-web')
        web_url = web_url_tag.find_next_sibling(string=True).strip() if web_url_tag else "⚠️ URL Web not found"

        # Simpan data dalam format dictionary
        data = {
            "Name": name_text,
            "Praticiens": praticiens_text,
            "Address":"'"+ address.strip(),
            "Telephone":"'"+ telephone,
            "URL/Web": web_url
        }
        page_data.append(data)

        print(f"📌 Name: {name_text}, Address: {address}")

    # Simpan data ke CSV hanya sekali per halaman
    if page_data:
        df = pd.DataFrame(page_data)
        df.to_csv(csv_filename, index=False, encoding='utf-8-sig', mode="a", header=False)

    print(f"📄 Halaman {page} selesai...")

    time.sleep(uniform(1, 2))  # Jeda antar request untuk menghindari pemblokiran
    page += 1  # Pindah ke halaman berikutnya

print("🎉 Semua data berhasil disimpan ke Annuaire Dentaire.csv!")



# csv_filename = "Annuaire Dentaire.csv"
# pd.DataFrame(columns=["Name", "Address", "Telephone", "URL/Web"]).to_csv(csv_filename, index=False, encoding='utf-8-sig', mode="w")


# # Base URL
# base_url = 'https://annuairedentaire.com/annuaire/chirurgiens-dentistes/odf?page='

# # Mulai dari halaman 1
# page = 1

# while True:
#     url = base_url + str(page)
#     print(f"🔄 Scraping halaman {page}: {url}")

#     # Request ke halaman
#     response = requests.get(url, headers=headers, cookies=cookies)
#     if response.status_code != 200:
#         print(f"❌ Gagal mengakses {url}")
#         break  # Hentikan jika error

#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Cek apakah ada daftar dokter di halaman ini
#     links = [
#         'https://annuairedentaire.com' + item.find('a')['href']
#         for item in soup.find_all('div', class_='card-list card-anden')
#     ]

#     if not links:
#         print("✅ Semua halaman telah diproses.")
#         break  # Hentikan jika tidak ada lagi dokter (berarti pagination habis)

#     page_data = []

#     # Proses setiap link detail dokter
#     for link in links:
#         response = requests.get(link, headers=headers, cookies=cookies)
#         soup = BeautifulSoup(response.content, 'html.parser')

#         page_link = soup.find('div', class_='main-content fiche-cd')
#         if not page_link:
#             print(f"⚠️ 'main-content fiche-cd' div not found on {link}")
#             continue

#         col_div = page_link.find('div', class_='col-lg-16 col-24')
#         if not col_div:
#             print(f"⚠️ 'col-lg-16 col-24' div not found on {link}")
#             continue

#         # Nama dan Praticiens
#         name = col_div.find('h1')
#         praticiens = col_div.find('h2')

#         name_text = name.text.strip() if name else "⚠️ Name not found"
#         praticiens_text = praticiens.text.strip().replace('\n', ' ') if praticiens else "⚠️ Praticiens not found"

#         # Address (Menggabungkan semua text dalam <p>)
#         address_tag = col_div.find('i', class_='icon-fiche-adresse')
#         address = "⚠️ Address not found"
#         if address_tag:
#             address_p = address_tag.find_parent('p')
#             if address_p:
#                 address = " ".join(address_p.stripped_strings)

#         # Telephone
#         telephone_tag = col_div.find('i', class_='icon-fiche-telephone')
#         telephone = telephone_tag.find_next_sibling(string=True).strip() if telephone_tag else "⚠️ Telephone not found"

#         # URL Web
#         web_url_tag = col_div.find('i', class_='icon-fiche-web')
#         web_url = web_url_tag.find_next_sibling(string=True).strip() if web_url_tag else "⚠️ URL Web not found"

#         data = {
#             "Name": "'" + name,
#             "Address": "'" + address,
#             "Telephone": "'" + telephone,
#             "URL/Web": "'" + web_url
#         }
#         page_data.append(data)

#         print(f"📌 Name: {name}, Address: {address}")

#         df = pd.DataFrame(page_data)
#         df.to_csv(csv_filename, index=False, encoding='utf-8-sig', mode="a", header=False)

#         print(f"📄 halaman {page} selesai...")

#     time.sleep(uniform(1, 2))  # Jeda antar request
#     # Pindah ke halaman berikutnya
#     page += 1
# print("🎉 Semua data berhasil disimpan ke Annuaire Dentaire.csv!")