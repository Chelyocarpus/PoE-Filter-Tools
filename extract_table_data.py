import json
import requests
from pyquery import PyQuery as pq
from typing import List, Dict
from tkinter import Tk, Label, Entry, Button
from tkinter import messagebox

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

def extract_all_tables(url: str) -> None:
    """Extracts data from all the HTML tables in the target URL and saves it to separate JSON files."""
    # Use a session object to reuse the underlying TCP connection across requests
    with requests.Session() as session:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        # Make a single request to get the HTML for all the pages
        response = session.get(url, headers=headers)

        # Parse the HTML and extract the data from each table
        doc = pq(response.content)
        title = doc('title').text()  # Extract the title of the page
        title = title.split(" | ")[0]  # Use everything before the pipe character as the filename
        title = title.strip().replace(" ", "_")  # Replace spaces with underscores and remove leading/trailing whitespace
        tables = doc('.wikitable')
        for i, table in enumerate(tables):
            table_data = extract_table_data(pq(table))

            # Save the data to a JSON file with the modified title as the filename
            filename = f'{title}_table{i+1}.json'
            with open(filename, 'w') as f:
                json.dump(table_data, f, indent=2)

    messagebox.showinfo("Extraction Complete", "Tables have been extracted successfully!")
# Define a function to extract tables from a given URL
def get_url() -> None:
    # Retrieve the URL entered in the Entry widget, remove any leading or trailing whitespace, and assign it to a variable
    url = entry.get().strip()
    # Check if the URL is empty or contains only whitespace
    if not url:
        # If the URL is empty, return without doing anything further
        return
    # If the URL is not empty, close the GUI window and extract all tables from the given URL using the extract_all_tables() function
    window.destroy()
    extract_all_tables(url)

# Define a function to cancel and close the GUI window
def cancel() -> None:
    # Close the GUI window
    window.destroy()

# Create a new GUI window using the Tk() method
window = Tk()
# Set the title of the GUI window
window.title("URL Input")

# Create a Label widget with the text "Enter the URL:" and add it to the GUI window using the pack() method
label = Label(window, text="Enter the URL:")
label.pack()

# Create an Entry widget with a width of 50 characters and add it to the GUI window using the pack() method
entry = Entry(window, width=50)
entry.pack()

# Create a Button widget with the text "Extract Tables" and assign the get_url() function to the command parameter
button = Button(window, text="Extract Tables", command=get_url)
# Add the button to the GUI window using the pack() method
button.pack()

# Create a Button widget with the text "Cancel" and assign the cancel() function to the command parameter
cancel_button = Button(window, text="Cancel", command=cancel)
# Add the button to the GUI window using the pack() method
cancel_button.pack()

# Start the GUI event loop and keep the window open until it is closed by the user using the mainloop() method
window.mainloop()
