import json
import requests
from tqdm import tqdm
from fight_data import parse_fight_details

# Replace 'file_path.json' with your JSON file path
file_path = './all_fights.json'

# Open and read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)


# Initialize variables
total_fights_json = []
consecutive_failures = 0
MAX_CONSECUTIVE_FAILURES = 10  # Stop if there are more than 10 consecutive failures
failures = []  # List to store failed fights (index and URL)

# Progress bar setup
print("Processing fights...")
with tqdm(total=len(data)) as progress_bar:
    for index, fight in enumerate(data, start=1):
        try:
            # Fetch and parse fight details
            page = requests.get(fight)
            fight_data = parse_fight_details(page.content)

            # Check if parsing returned an empty value
            if not fight_data:
                failures.append({"index": index, "fight": fight})
                consecutive_failures += 1
            else:
                # Add parsed fight data to the result list
                total_fights_json.append(fight_data)
                consecutive_failures = 0  # Reset failure counter on success

            # Stop execution if consecutive failures exceed the limit
            if consecutive_failures >= MAX_CONSECUTIVE_FAILURES:
                print(f"Error: More than {MAX_CONSECUTIVE_FAILURES} consecutive failures. Stopping execution.")
                break

        except Exception as e:
            # Handle any other exceptions during parsing
            print(f"Error: Failed to process fight #{index} due to exception: {e}")
            failures.append({"index": index, "fight": fight})
            consecutive_failures += 1

            # Stop execution if consecutive failures exceed the limit
            if consecutive_failures >= MAX_CONSECUTIVE_FAILURES:
                print(f"Error: More than {MAX_CONSECUTIVE_FAILURES} consecutive failures. Stopping execution.")
                break

        # Update the progress bar
        progress_bar.update(1)


# Save successful fights to a JSON file
json_file = f'{len(data)}_fights_data.json'
with open(json_file, 'w', encoding='utf-8') as file:
    json.dump(total_fights_json, file, indent=4, ensure_ascii=False)

# Save successful fights to a JSON file
results_file = f'{len(data)}_fights_data_results.json'
with open(results_file, 'w', encoding='utf-8') as file:
    json.dump(failures, file, indent=4, ensure_ascii=False)

# Final report
start_index = 1
end_index = index
total_processed = end_index - start_index + 1

print("\nFinal Report:")
print(f"Total fights processed: {total_processed}")
print(f"Processing started at index: {start_index}")
print(f"Processing ended at index: {end_index}")
print(f"Successful fights: {len(total_fights_json)}")
print(f"Failed fights: {len(failures)}")

