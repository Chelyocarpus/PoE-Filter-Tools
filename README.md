# PoE-Filter-Stuff

Tools to help with my Path of Exile filter creation. Work in Progress.

## Overview
- extract_table_data.py

This is a script that extracts data from HTML tables in a specific URL using the PyQuery library. The script loops through all the tables in the webpage, extracts data from each table, and saves the data to separate JSON files using the built-in json library. The data is returned as a list of dictionaries, where each dictionary represents a row in the table, with keys representing column headers and values representing the data in the corresponding cells.


- parse_json_to_txt.py

This script processes JSON files, extracting specific fields and converting them into a formatted text file. The main function prompts the user for a base file name, iterates through a series of JSON files, and processes each using the parse_json_to_txt function. If any JSON files have missing required fields, they are marked with an error in the output file name. Finally, the script merges all successfully processed output files into a single merged file, excluding those with errors.

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
