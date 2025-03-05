import csv
import json
import requests
from bs4 import BeautifulSoup

URL = "http://www.ufcstats.com/statistics/events/completed?page=all"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

events = []

for tr in soup.find_all('tr'):
    for desc in tr.descendants:
        if desc.name == 'a':
            text = desc.get_text(strip=True)
            href = desc.get('href')
            events.append({
                "event": text,
                "url": href,
                "fights": []
            })


def get_fight_links(url, fights):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    for tr in soup.find_all('tr'):
        fights.append(tr.get('data-link'))

for event in events:
    get_fight_links(event["url"], event["fights"])

json_file = 'events-test.json'
with open(json_file, 'w', encoding='utf-8') as file:
    json.dump(events, file, indent=4, ensure_ascii=False)  # Pretty-print with indent=4

print(f"JSON file '{json_file}' created successfully.")
