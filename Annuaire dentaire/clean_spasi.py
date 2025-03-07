import pandas as pd

# Baca file CSV
df = pd.read_csv("Annuaire Dentaire.csv")

# Bersihkan spasi berlebih dalam kolom 'Address'
df["Address"] = df["Address"].str.replace(r'\s+', ' ', regex=True).str.strip()

# Simpan kembali ke file CSV
df.to_csv("cleaned_Annuaire Dentaire.csv", index=False)

print("Spasi berlebih sudah dibersihkan dan disimpan di cleaned_Annuaire Dentaire.csv")
