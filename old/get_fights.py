import json

# Open and read the JSON file
json_file = './events-test.json'
with open(json_file, 'r', encoding='utf-8') as file:
    events = json.load(file)

# Extract all fights
all_fights = []
for event in events:
    all_fights.extend(fight for fight in event['fights'] if fight is not None)  # Filter out null fights

# Save the fights list to a new JSON file
fights_file = 'all_fights-test.json'
with open(fights_file, 'w', encoding='utf-8') as file:
    json.dump(all_fights, file, indent=4, ensure_ascii=False)

print(f"All fights have been saved to '{fights_file}'.")
