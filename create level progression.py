import json

# Open the JSON file
with open('C:/Users/Goliath/Desktop/output1.json', 'r') as f:
    data = json.load(f)

# Initialize the output string
output = ''

# Loop through the JSON data
for i in range(len(data)):
    try:
        # Extract the name and req_level values from the current item
        item_name = data[i]['name']
        req_level = data[i]['req_level']
    except KeyError:
        # If the required keys are not present, print an error message and break out of the loop
        print('Error: The JSON file does not have the required keys')
        break

    if i+1 < len(data):
        # If there are more items in the JSON data, extract the req_level value from the next item
        next_item = data[i+1]
        req_level2 = next_item['req_level']
    else:
        # If there are no more items in the JSON data, set req_level2 to 100
        req_level2 = '100'

    # Add the Show command and item details to the output string
    output += f"Show\n\tBaseType \"{item_name}\"\n\tDropLevel >= {req_level}\n\tAreaLevel <= {req_level2}\n\n"

# Write the output string to a text file
with open('output.txt', 'w') as f:
    f.write(output)
