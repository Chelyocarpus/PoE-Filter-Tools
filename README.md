# PoE-Filter-Stuff

Tools to help with my Path of Exile filter creation. Work in Progress.

## Overview
- extract_table_data.py

This is a script that extracts data from HTML tables in a specific URL using the PyQuery library. The script loops through all the tables in the webpage, extracts data from each table, and saves the data to separate JSON files using the built-in json library. The data is returned as a list of dictionaries, where each dictionary represents a row in the table, with keys representing column headers and values representing the data in the corresponding cells.


- parse_json_to_txt.py

The script defines a function parse_json_to_txt that reads in a JSON file, extracts specific fields, and writes the extracted information to a text file in a specific format. The function takes in two arguments, the file path of the JSON file to parse and the file path of the output text file. It returns None. The function is then called in a loop to parse multiple JSON files and write the extracted data to separate text files. The function handles errors related to file not found, invalid JSON, and other exceptions. The output text file contains a formatted string for each item in the JSON file.

## ToDo-List
[See what has to be done](https://github.com/Chelyocarpus/PoE-Filter-Stuff/issues?q=is%3Aissue+is%3Aopen+label%3AToDo) and contribute if you wish to do so.

## Contribute

Whether you're a seasoned developer or just getting started, there are plenty of ways you can help out.
If you notice any bugs or have any feature requests, please open an [issue](https://github.com/Chelyocarpus/PoE-Filter-Stuff/issues) on the repository. This helps me keep track of what needs to be fixed or improved.
If you want to contribute code directly, you can do so by opening a [pull request](https://github.com/Chelyocarpus/PoE-Filter-Stuff/pulls).

## Changelog
[![Button Changelog]][Changelog]

<!----------------------------------------------------------------------------->

[Changelog]: https://github.com/Chelyocarpus/PoE-Filter-Stuff/discussions/categories/changelog

[Button Changelog]: https://img.shields.io/badge/Changelog-4285F4?style=for-the-badge&logoColor=white&logo=Git
