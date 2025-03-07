import requests
import json
from bs4 import BeautifulSoup
import re
import random  
import time




cookies = {
    'cookie': '_ga=GA1.1.1742961980.1740936294; _pk_id.6.96a2=943e3ed8d094fda0.1740936296.; PHPSESSID=j30pjih5q357tpaqmmab260bgf; _pk_ref.6.96a2=%5B%22%22%2C%22%22%2C1740992063%2C%22https%3A%2F%2Fwww.upwork.com%2F%22%5D; _pk_ses.6.96a2=1; _ga_91T9T33B2V=GS1.1.1740992064.3.0.1740992064.0.0.0'
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
}

# response = requests.get('https://www.ordre-chirurgiens-dentistes.fr/annuaire/php/actions/get-praticiens.php?name=&firstName=&zip=01&city=&spe=ODF&page=0',  cookies=cookies, headers=headers)

# soup = BeautifulSoup(response.content, 'html.parser')

# services_items = soup.find_all('div', {'class': 'service-item'})

# for item in services_items:
#     items_service_item_container = item.find('div', {'class': 'service-item-container'})
    
#     service_item_data = items_service_item_container.find('div', {'class': 'service-item-data'})

#     if service_item_data:
    
#         text_content = service_item_data.get_text(separator="\n", strip=True)
    
#         rpps_match = re.search(r"N° RPPS\s*:\s*(\d+)", text_content)
#         specialite_match = re.search(r"Spécialité\s*:\s*(.+)", text_content)
#         mode_exercice_match = re.search(r"Mode d'exercice\s*:\s*(.+)", text_content)
#         adresse_match = re.search(r"Adresse d'exercice\s*:\s*(.+)", text_content)

#         name = items_service_item_container.find('h4').text.strip() if items_service_item_container.find('h4') else None

#         data = {
#             "Name": name,
#             "RPPS": rpps_match.group(1) if rpps_match else None,
#             "Spécialité": specialite_match.group(1).strip() if specialite_match else None,
#             "Mode d'exercice": mode_exercice_match.group(1).strip() if mode_exercice_match else None,
#             "Adresse d'exercice": adresse_match.group(1).strip() if adresse_match else None
#         }

#         results.append(data)
# print(results)

cookies = {}  # Sesuaikan jika diperlukan
headers = {}  # Sesuaikan jika diperlukan

all_data = []

# Loop untuk zip dari 01 hingga 95
for zip_code in range(1, 96):
    zip_str = f"{zip_code:02d}"  # Format dua digit (01, 02, ..., 95)
    page = 0

    while True:
        url = f'https://www.ordre-chirurgiens-dentistes.fr/annuaire/php/actions/get-praticiens.php?name=&firstName=&zip={zip_str}&city=&spe=ODF&page={page}'
        
        response = requests.get(url, cookies=cookies, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        services_items = soup.find_all('div', {'class': 'service-item'})

        if not services_items:
            print(f"Tidak ada data di ZIP {zip_str} halaman {page}, lanjut ZIP berikutnya.")
            break  # Hentikan loop jika tidak ada data

        for item in services_items:
            items_service_item_container = item.find('div', {'class': 'service-item-container'})
            
            service_item_data = items_service_item_container.find('div', {'class': 'service-item-data'}) if items_service_item_container else None

            if service_item_data:
                text_content = service_item_data.get_text(separator="\n", strip=True)

                rpps_match = re.search(r"N° RPPS\s*:\s*(\d+)", text_content)
                specialite_match = re.search(r"Spécialité\s*:\s*(.+)", text_content)
                mode_exercice_match = re.search(r"Mode d'exercice\s*:\s*(.+)", text_content)
                adresse_match = re.search(r"Adresse d'exercice\s*:\s*(.+)", text_content)

                name = items_service_item_container.find('h4').text.strip() if items_service_item_container.find('h4') else None

                data = {
                    "ZIP": zip_str,
                    "Name": name,
                    "RPPS": rpps_match.group(1) if rpps_match else None,
                    "Spécialité": specialite_match.group(1).strip() if specialite_match else None,
                    "Mode d'exercice": mode_exercice_match.group(1).strip() if mode_exercice_match else None,
                    "Adresse d'exercice": adresse_match.group(1).strip() if adresse_match else None
                }
                
                print(data)

                all_data.append(data)

        print(f"ZIP {zip_str}, Halaman {page} selesai. Menunggu sebelum lanjut...")

        # Tunggu sebelum ke halaman berikutnya (random antara 2 - 5 detik)
        time.sleep(random.uniform(2, 5))  

        page += 1  # Lanjut ke halaman berikutnya

print(f"Total data yang dikumpulkan: {len(all_data)}")

