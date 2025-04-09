# NOTE:
# This script was originally built to scrape Google-based LinkedIn profiles.
# Due to dynamic result blocking, dummy data was used for demonstration.



import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    "User-Agent": "Mozilla/5.0"
}

query = 'site:linkedin.com/in/ "Founder" "IT Startup" Bangalore'
url = f"https://www.google.com/search?q={query}"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

results = []
for g in soup.find_all('div', class_='tF2Cxc'):
    link = g.find('a')['href']
    title = g.find('h3').text if g.find('h3') else 'No title'
    print(f"{title} --> {link}")
    results.append({"Name": title, "LinkedIn URL": link})

# Save only if results found
if results:
    df = pd.DataFrame(results)
    df.to_excel("linkedin_profiles.xlsx", index=False)
    print("✅ LinkedIn data extracted and saved to 'linkedin_profiles.xlsx'")
else:
    print("❌ No profiles found. Try checking selectors or search result blocking.")
