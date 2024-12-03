from bs4 import BeautifulSoup
import json
import requests

def extract_fighter_info(person_div):
    """Extract basic fighter information from their div"""
    status = person_div.find('i', class_='b-fight-details__person-status').text.strip()
    name = person_div.find('a', class_='b-link').text.strip()
    nickname_elem = person_div.find('p', class_='b-fight-details__person-title')
    nickname = nickname_elem.text.strip() if nickname_elem else ""
    
    return {
        'status': status,
        'name': name,
        'nickname': nickname
    }

def extract_fight_stats(table_body):
    """Extract fight statistics from a table body"""
    stats = {}
    rows = table_body.find_all('tr', class_='b-fight-details__table-row')
    
    for row in rows:
        cols = row.find_all('td', class_='b-fight-details__table-col')
        if not cols:
            continue
            
        # Skip if this is just a header row
        if not cols[0].find_all('p', class_='b-fight-details__table-text'):
            continue
            
        fighter1_stats = {}
        fighter2_stats = {}
        
        for i, col in enumerate(cols[1:], 1):  # Skip the fighter names column
            values = col.find_all('p', class_='b-fight-details__table-text')
            if len(values) >= 2:
                fighter1_stats[f'col_{i}'] = values[0].text.strip()
                fighter2_stats[f'col_{i}'] = values[1].text.strip()
        
        stats['fighter1'] = fighter1_stats
        stats['fighter2'] = fighter2_stats
        break  # We only need the first row with actual stats
        
    return stats

def extract_tables_data(table):
    """Extract significant strike statistics"""
    headers = [th.text.strip() for th in table.find('thead').find_all('th')]
    body = table.find('tbody')
    
    strikes_data = {}  # Skip the "Fighter" header
    stats = extract_fight_stats(body)
    
    # Map the generic column numbers to actual headers
    fighter1_strikes = {}
    fighter2_strikes = {}
    
    for i, header in enumerate(headers[1:], 1):
        fighter1_strikes[header] = stats['fighter1'][f'col_{i}']
        fighter2_strikes[header] = stats['fighter2'][f'col_{i}']
    
    strikes_data['fighter1'] = fighter1_strikes
    strikes_data['fighter2'] = fighter2_strikes
    
    return strikes_data

def parse_fight_details(html_content):
    """Main function to parse fight details from HTML content"""
    soup = BeautifulSoup(html_content, 'html.parser')
    fight_details = soup.find('div', class_='b-fight-details')
    
    # Extract basic fight information
    fight_data = {
        'fighters': {},
        'fight_details': {},
        'totals': {},
        'significant_strikes': {}
    }
    
    # Extract fighter information
    fighters_div = fight_details.find('div', class_='b-fight-details__persons')
    fighter_divs = fighters_div.find_all('div', class_='b-fight-details__person')
    
    for i, fighter_div in enumerate(fighter_divs, 1):
        fight_data['fighters'][f'fighter{i}'] = extract_fighter_info(fighter_div)
    
    # Extract fight details
    fight_info = fight_details.find('div', class_='b-fight-details__fight')
    fight_data['fight_details']['title'] = fight_info.find('i', class_='b-fight-details__fight-title').text.strip()
    
    # Inside the method extraction part:
    method_item = fight_info.find('i', class_='b-fight-details__text-item_first')
    if method_item:
        method_value = method_item.find('i', attrs={'style': 'font-style: normal'})
        if method_value:
            fight_data['fight_details']['method'] = method_value.text.strip()

    # Extract method, round, time, etc.
    details = fight_info.find_all('p', class_='b-fight-details__text')
    for detail in details:
        items = detail.find_all('i', class_='b-fight-details__text-item')
        for item in items:
            label = item.find('i', class_='b-fight-details__label')
            if label:
                key = label.text.strip().replace(':', '').lower()
                value = item.text.replace(label.text, '').strip()
                fight_data['fight_details'][key] = value

    # Extract strike details
        if 'Details:' in detail.text:
            strike_details = detail.text.replace('Details:', '').strip()
            if strike_details:
                fight_data['fight_details']['details'] = strike_details

    # Extract total stats
    totals_table = fight_details.find('table', style='width: 745px')
    if totals_table:
        fight_data['totals'] = extract_tables_data(totals_table)
    
    # Extract significant strikes
    sig_strikes_table = fight_details.find_all('table', style='width: 745px')[1]
    if sig_strikes_table:
        fight_data['significant_strikes'] = extract_tables_data(sig_strikes_table)
    
    return fight_data


# Example usage:
# URL = "http://www.ufcstats.com/fight-details/425e856cac6f521b"
# page = requests.get(URL)

# fight_data = parse_fight_details(page.content)
# json_file = 'test.json'
# with open(json_file, 'w', encoding='utf-8') as file:
#     json.dump(fight_data, file, indent=4, ensure_ascii=False)  # Pretty-print with indent=4

# print(f"JSON file '{json_file}' created successfully.")
