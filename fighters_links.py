import json

# Open and read the JSON file safely
json_file = './8012_fights_data.json'
try:
    with open(json_file, 'r', encoding='utf-8') as file:
        fights_data = json.load(file)
except (json.JSONDecodeError, FileNotFoundError) as e:
    print(f"Error loading JSON: {e}")
    fights_data = []

# Extract unique fighter links
fighters_set = set()

for fight in fights_data:
    for key in ["fighter1", "fighter2"]:
        fighter = fight.get("fighters", {}).get(key, {}).get("link")
        if fighter:
            fighters_set.add(fighter)

# Convert set to list and save to JSON
fighters_links = list(fighters_set)

fights_file = 'fighters.json'
with open(fights_file, 'w', encoding='utf-8') as file:
    json.dump(fighters_links, file, indent=4, ensure_ascii=False)

print(f"Saved {len(fighters_links)} unique fighter links to {fights_file}.")