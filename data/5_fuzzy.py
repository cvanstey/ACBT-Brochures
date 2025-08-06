import pandas as pd
from geopy.geocoders import Nominatim
from time import sleep
import re

import pandas as pd

# === File Paths ===
input_path = r"C:\Users\Public\Documents\archive\parsed_brochure_geocoded72925.csv"
output_path = r"C:\Users\Public\Documents\archive\parsed_brochure_geocoded72925new fuzzy.csv"

# === Load CSV Data ===
df = pd.read_csv(input_path)

# === Geolocator Setup ===
geolocator = Nominatim(user_agent="acbt-mapping-script")
df['latitude'] = None
df['longitude'] = None

# === Helper: Clean and simplify address ===
def simplify_address(address):
    if pd.isna(address):
        return ""
    address = str(address)
    address = re.sub(r"\d{1,5}", "", address)  # Remove numbers
    address = re.sub(r"[^\w\s&]", "", address)  # Remove punctuation
    address = re.sub(r"\s{2,}", " ", address).strip()
    return address

# === Geocoding Function ===
def try_geocode(row):
    components = [str(row.get(col, '')).strip() for col in ['Address', 'City', 'State'] if pd.notna(row.get(col, ''))]
    components = [str(row.get(col) or '').strip() for col in ['Address', 'City', 'State']]
    original = ', '.join(components)
    city = str(row.get('City') or '').strip()
    state = str(row.get('State') or '').strip()
    address = simplify_address(str(row.get('Address') or ''))
    simplified = f"{address}, {city}, {state}"

    queries = [original, simplified]
    for query in queries:
        try:
            location = geolocator.geocode(query)
            if location:
                return location.latitude, location.longitude
        except Exception as e:
            print(f"⚠️ Error geocoding '{query}': {e}")
        sleep(1)
    return None, None

# === Main Loop ===
for idx, row in df.iterrows():
    lat, lon = try_geocode(row)
    df.at[idx, 'latitude'] = lat
    df.at[idx, 'longitude'] = lon
    address_str = row.get('Address', '')
    if lat and lon:
        print(f"✅ {address_str} => ({lat}, {lon})")
    else:
        print(f"❌ {address_str} => Not Found")

# === Save to Excel ===
df.to_excel(output_path, index=False)
print(f"📄 Geocoded file saved to:\n{output_path}")
