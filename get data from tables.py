import requests
import json
from pyquery import PyQuery as pq

def extract_table_data(table):
    # Extract the amount of table rows
    rows = table('tbody tr')
    amount_of_items = len(rows) - 1
    items = []

    # Loop through each row of the table
    for i in range(1, amount_of_items+1):
        # Extract the name of the item from the first column
        name_of_item = rows.eq(i).find('td span span a').attr("title")
        
        # Extract the required level from the second column
        req_level = rows.eq(i).find('td:nth-child(2)').text()

        # Extract the required attributes from the third column
        third_column = rows.eq(i).find('td:nth-child(3)').text()

        # Extract the values from the fourth column
        fourth_column = rows.eq(i).find('td:nth-child(4)').text()

        # Extract the values from the fifth column
        fifth_column = rows.eq(i).find('td:nth-child(5)').text()

        # Extract the values from the sixth column
        sixth_column = rows.eq(i).find('td:nth-child(6)').text()

        # Append the item data to the list of items
        items.append({'name': name_of_item, 'req_level': req_level, '3': third_column, '4': fourth_column, '5': fifth_column, '6': sixth_column})

    return items

def extract_all_tables():
    # Make a GET request to the URL and parse the HTML response using PyQuery
    url = "https://www.poewiki.net/wiki/Body_armour"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    doc = pq(response.content)

    # Find all of the tables on the page with the .wikitable class
    tables = doc('.wikitable')

    # Loop through each table and extract the data
    for i, table in enumerate(tables):
        table_data = extract_table_data(pq(table))

        # Save the data to a JSON file
        filename = f'output{i+1}.json'
        with open(filename, 'w') as f:
            json.dump(table_data, f, indent=2)

extract_all_tables()
