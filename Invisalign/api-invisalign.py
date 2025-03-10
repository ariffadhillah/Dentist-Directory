import requests
import json
import re
import pandas as pd

# URL API
url = "https://eudoclocsvc-production-eu.herokuapp.com/rd?uct=47&cl=fr%2Cmc&f=F1&s=S0&rd=40&rdi=2.5&it=eu&lng=0.4502368&lat=44.2470173&cid=359ed12e8c4e&sid=016c8d727d3c&vid=606580a360fa&_=1741530164165&method=axiosJsonpCallback51"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.invisalign.fr/",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "cross-site"
}

number_of_zip = "47"

csv_filename = f'Invisalign-{number_of_zip}.csv'

# Inisialisasi file CSV dengan header (ditulis hanya sekali)
pd.DataFrame(columns=["ZIP", "Name", "Business Name", "Address", "Email", "Telephone", "Fax" ]).to_csv(
    csv_filename, index=False, encoding='utf-8-sig', mode="w"
)

page_data = []

# Mengambil data dari API
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.text  # Mendapatkan teks respons

    # Menghapus pembungkus JSONP: axiosJsonpCallback1(...)
    clean_data = re.sub(r'^axiosJsonpCallback\d*\(|\);$', '', data)

    # Konversi string ke JSON
    try:
        json_data = json.loads(clean_data)

        # Mengambil daftar hasil dari JSON
        response_data = json_data.get("responseData", {}).get("results", [])
        print(json.dumps(response_data, indent=4))
        print()

        # Menampilkan semua BusinessName dan City
        for item in response_data:
            fullname = item.get("FullName", "N/A")
            businessName = item.get("BusinessName", "N/A")
            line_ = item.get("Line1", "N/A")
            postalCode_ = item.get("PostalCode", "N/A")
            city = item.get("City", "N/A")
            country = item.get("Country", "N/A")
            email_ = item.get("Email", "N/A")
            fax_ = item.get("Fax", "N/A")
            officePhone = item.get("OfficePhone", "N/A")

            address = f"{line_}, {postalCode_}, {city}, {country}"

            print(f"Name: {fullname}")
            print(f"Business Name: {businessName}")
            print(f"Address: {address}")
            print(f"Email: {email_}")
            print(f"Fax: {fax_}")
            print(f"Office Phone: {officePhone}")
            print()  

            # Menambahkan data ke list
            page_data.append({
                'ZIP': "'"+number_of_zip,
                'Name': fullname,
                'Business Name': businessName,
                'Address': address,
                'Email': email_,
                'Telephone':"'"+officePhone,
                'Fax': "'"+fax_,
            })

        # Membuat DataFrame dan menulis ke CSV SEKALI SAJA setelah loop selesai
        df = pd.DataFrame(page_data)
        df.to_csv(csv_filename, index=False, encoding='utf-8-sig', mode="a", header=False)

    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")

else:
    print(f"Error {response.status_code}: {response.text}")
