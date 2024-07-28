import json
import os

def parse_json_to_txt(json_file_path: str, output_file_path: str) -> bool:
    """
    This function reads in a JSON file, extracts specific fields, and writes the extracted information
    to a text file in a specific format.

    Args:
        json_file_path (str): The file path of the JSON file to parse.
        output_file_path (str): The file path of the output text file.

    Returns:
        bool: Returns True if an error occurred due to missing keys, otherwise False.
    """

    try:
        # Open the JSON file
        with open(json_file_path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in file {json_file_path}")
        return True

    # Initialize the output string
    output = ''
    error_occurred = False

    # Loop through the JSON data
    for i, item in enumerate(data):
        # Extract the name and req_level values from the current item
        item_name = item.get('name')
        req_level = item.get('req_level')

        # Check that the required keys are present
        if item_name is None or req_level is None:
            # If the required keys are not present, print an error message and continue to the next item
            print(f'Error: Item {i} does not have the required keys')
            error_occurred = True
            continue

        # Extract the req_level value from the next item in the list
        next_item = data[i+1] if i+1 < len(data) else {}
        req_level2 = next_item.get('req_level', 100)

        # Add the Show command and item details to the output string
        output += f"Show\n\tBaseType \"{item_name}\"\n\tDropLevel >= {req_level}\n\tAreaLevel <= {req_level2}\n\n"

    # Modify the output file name if there was an error
    if error_occurred:
        base, ext = os.path.splitext(output_file_path)
        output_file_path = f"{base}_error{ext}"

    # Write the output string to a text file, appending to existing content
    with open(output_file_path, 'a') as f:
        f.write(output)

    return error_occurred

def merge_output_files(base_name: str, output_dir: str) -> None:
    """
    Merges all non-error output files into a single _merged file.

    Args:
        base_name (str): The base name for the files.
        output_dir (str): The directory containing the output files.

    Returns:
        None
    """
    merged_file_path = os.path.join(output_dir, f"{base_name}_merged.txt")
    with open(merged_file_path, 'w') as merged_file:
        for output_file in sorted(os.listdir(output_dir)):
            if output_file.startswith(base_name) and output_file.endswith(".txt") and "_error" not in output_file:
                with open(os.path.join(output_dir, output_file), 'r') as f:
                    merged_file.write(f.read())

def main():
    # Let the user specify the base name for the files
    base_name = input("Enter the base name for the files: ")

    # Directory for the output files
    output_dir = "."

    # Determine the range of files dynamically
    i = 1
    while os.path.exists(f"{base_name}_table{i}.json"):
        i += 1

    # Process each file
    for j in range(1, i):
        input_file = f"{base_name}_table{j}.json"
        output_file = f"{base_name}_output{j}.txt"
        try:
            parse_json_to_txt(input_file, output_file)
        except FileNotFoundError as e:
            print(f"Error: {e.filename} not found")
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in file {input_file}")
        except Exception as e:
            print(f"Error: {e}")

    # Merge all non-error output files
    merge_output_files(base_name, output_dir)

if __name__ == "__main__":
    main()
