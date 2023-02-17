import json

def parse_json_to_txt(json_file_path: str, output_file_path: str) -> None:
    """
    This function reads in a JSON file, extracts specific fields, and writes the extracted information
    to a text file in a specific format.

    Args:
        json_file_path (str): The file path of the JSON file to parse.
        output_file_path (str): The file path of the output text file.

    Returns:
        None
    """

    try:
        # Open the JSON file
        with open(json_file_path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in file {json_file_path}")
        return

    # Initialize the output string
    output = ''

    # Loop through the JSON data
    for i, item in enumerate(data):
        # Extract the name and req_level values from the current item
        item_name = item.get('name')
        req_level = item.get('req_level')

        # Check that the required keys are present
        if item_name is None or req_level is None:
            # If the required keys are not present, print an error message and continue to the next item
            print(f'Error: Item {i} does not have the required keys')
            continue

        # Extract the req_level value from the next item in the list
        next_item = data[i+1] if i+1 < len(data) else {}
        req_level2 = next_item.get('req_level', 100)

        # Add the Show command and item details to the output string
        output += f"Show\n\tBaseType \"{item_name}\"\n\tDropLevel >= {req_level}\n\tAreaLevel <= {req_level2}\n\n"

    # Write the output string to a text file, appending to existing content
    with open(output_file_path, 'a') as f:
        f.write(output)

for i in range(1, 11):
    input_file = f"output{i}.json"
    output_file = f"output{i}.txt"
    try:
        parse_json_to_txt(input_file, output_file)
    except FileNotFoundError as e:
        print(f"Error: {e.filename} not found")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in file {input_file}")
    except Exception as e:
        print(f"Error: {e}")

