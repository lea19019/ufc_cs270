import json
import random

# Open and read the JSON file
json_file = './all_fights_test.json'
with open(json_file, 'r', encoding='utf-8') as file:
    all_fights = json.load(file)

simplified_figths = random.choices(all_fights, k=100)

fights_file = f'{len(simplified_figths)}_fights.json'
with open(fights_file, 'w', encoding='utf-8') as file:
    json.dump(simplified_figths, file, indent=4, ensure_ascii=False)

print(f"All fights have been saved to '{fights_file}'.")
