from bs4 import BeautifulSoup, Tag, NavigableString
import json
import requests

def parse_fighter_details(html_content):
    """Extracts fighter details from HTML."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract basic details
    name = soup.find('span', class_='b-content__title-highlight').text.strip()
    record = soup.find('span', class_='b-content__title-record').text.strip()
    nickname_elem = soup.find('p', class_='b-content__Nickname')
    nickname = nickname_elem.text.strip() if nickname_elem else ""

    # Find the information boxes
    boxes = soup.find_all('div', class_='js-guide')

    fighter_data = {
        "name": name,
        "record": record,
        "nickname": nickname,
        "physical_attributes": {},
        "career_statistics": {}
    }

    # Extract physical attributes from the first box
    if len(boxes) > 0:
        physical_attrs = boxes[0].find_all('li')
        for attr in physical_attrs:
            key_element = attr.find('i')
            key = key_element.text.strip().replace(":", "")
            value = key_element.next_sibling.strip() if key_element.next_sibling else ""
            fighter_data["physical_attributes"][key] = value

    # Extract career statistics from the second box
    if len(boxes) > 1:
        career_stats = boxes[1].find_all('li')
        for stat in career_stats:
            key_element = stat.find('i')
            key = key_element.text.strip().replace(":", "")
            if not key:
                continue
            value = key_element.next_sibling.strip() if key_element.next_sibling else ""
            fighter_data["career_statistics"][key] = value

    return fighter_data

# # Example usage:
# URL = "http://www.ufcstats.com/fighter-details/2844b047183a1adb"
# page = requests.get(URL)

# fighter_data = parse_fighter_details(page.content)

# json_file = 'test_fighter.json'
# with open(json_file, 'w', encoding='utf-8') as file:
#     json.dump(fighter_data, file, indent=4, ensure_ascii=False)  # Pretty-print with indent=4

# print(f"JSON file '{json_file}' created successfully.")
