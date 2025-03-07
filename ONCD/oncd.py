import requests
import re
import time
import pandas as pd
from bs4 import BeautifulSoup
from random import uniform

# Simpan semua data di list
all_data = []

# Headers dan cookies 
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
cookies = {
    'cookie': '_ga=GA1.1.1742961980.1740936294; _pk_id.6.96a2=943e3ed8d094fda0.1740936296.; PHPSESSID=j30pjih5q357tpaqmmab260bgf'
}

# Buat file CSV dan tulis header hanya sekali
csv_filename = "ONCD.csv"
pd.DataFrame(columns=["ZIP", "Name", "N° RPPS", "Spécialité", "Mode d'exercice", "Adresse d'exercice"]).to_csv(csv_filename, index=False, encoding='utf-8-sig', mode="w")

# Loop ZIP 01 hingga 95
for zip_code in range(1, 96):
    zip_str = f"{zip_code:02d}"  # Format '01', '02', ..., '95'
    page = 0

    while True:
        url = f"https://www.ordre-chirurgiens-dentistes.fr/annuaire/php/actions/get-praticiens.php?name=&firstName=&zip={zip_str}&city=&spe=ODF&page={page}"
        response = requests.get(url, headers=headers, cookies=cookies)

        # Jika error, hentikan loop
        if response.status_code != 200:
            print(f"⛔ Error fetching {url}")
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        services_items = soup.find_all('div', {'class': 'service-item'})

        # Jika tidak ada data di halaman ini, lanjut ke ZIP berikutnya
        if not services_items:
            print(f"✅ Selesai membaca ZIP {zip_str}")
            break

        # List untuk menyimpan data halaman ini
        page_data = []

        for item in services_items:
            items_service_item_container = item.find('div', {'class': 'service-item-container'})
            service_item_data = items_service_item_container.find('div', {'class': 'service-item-data'}) if items_service_item_container else None

            if service_item_data:
                text_content = service_item_data.get_text(separator="\n", strip=True)

                # Ambil data dengan regex
                rpps_match = re.search(r"N° RPPS\s*:\s*(\d+)", text_content)
                specialite_match = re.search(r"Spécialité\s*:\s*(.+)", text_content)
                mode_exercice_match = re.search(r"Mode d'exercice\s*:\s*(.+)", text_content)
                adresse_match = re.search(r"Adresse d'exercice\s*:\s*(.+)", text_content)

                name = items_service_item_container.find('h4').text.strip() if items_service_item_container.find('h4') else None

                data = {
                    "ZIP": "'" + zip_str,
                    "Name": "'" + name,
                    "N° RPPS": "'" + (rpps_match.group(1) if rpps_match else ""),
                    "Spécialité": "'" + (specialite_match.group(1).strip() if specialite_match else ""),
                    "Mode d'exercice": "'" + (mode_exercice_match.group(1).strip() if mode_exercice_match else ""),
                    "Adresse d'exercice": "'" + (adresse_match.group(1).strip() if adresse_match else "")
                }

                # Simpan data per halaman
                page_data.append(data)

                # Cetak Name dan N° RPPS saat ini
                print(f"📌 Name: {name}, N° RPPS: {rpps_match.group(1) if rpps_match else 'N/A'}")

        # Tambahkan data halaman ini ke CSV (tanpa menimpa data sebelumnya)
        df = pd.DataFrame(page_data)
        df.to_csv(csv_filename, index=False, encoding='utf-8-sig', mode="a", header=False)

        print(f"📄 ZIP {zip_str}, halaman {page} selesai...")

        # Jeda untuk menghindari deteksi bot (2-5 detik)
        time.sleep(uniform(2, 5))

        # Lanjut ke halaman berikutnya
        page += 1
        

print("🎉 Semua data berhasil disimpan ke ONCD.csv!")
