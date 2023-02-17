import json
import requests
from pyquery import PyQuery as pq
from typing import List, Dict

def extract_table_data(table: pq) -> List[Dict[str, str]]:
    """
    Extract data from a table and return a list of dictionaries.

    Each dictionary represents a row in the table, with keys representing
    column headers and values representing the data in the corresponding cells.
    """
    # Extract the table rows
    rows = table('tbody tr')
    items = []

    # Loop through the rows and extract data from each cell
    for row in rows[1:]:  # Skip the first row (header row)
        cells = pq(row)('td')
        item = {
            'name': cells.eq(0).find('a').attr("title"),
            'req_level': cells.eq(1).text(),
            '3': cells.eq(2).text(),
            '4': cells.eq(3).text(),
            '5': cells.eq(4).text(),
            '6': cells.eq(5).text()
        }
        items.append(item)

    return items

def extract_all_tables() -> None:
    """Extracts data from all the HTML tables in the target URL and saves it to separate JSON files."""
    # Use a session object to reuse the underlying TCP connection across requests
    with requests.Session() as session:
        url = "https://www.poewiki.net/wiki/Body_armour"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        # Make a single request to get the HTML for all the pages
        response = session.get(url, headers=headers)

        # Parse the HTML and extract the data from each table
        doc = pq(response.content)
        tables = doc('.wikitable')
        for i, table in enumerate(tables):
            table_data = extract_table_data(pq(table))

            # Save the data to a JSON file
            filename = f'output{i+1}.json'
            with open(filename, 'w') as f:
                json.dump(table_data, f, indent=2)

# Call the extract_all_tables function to start the data extraction process
extract_all_tables()