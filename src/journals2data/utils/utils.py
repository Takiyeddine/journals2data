from typing import Any, List, Dict
import json
import csv
import datetime

# json manipulations
def json_file_to_data(json_file_path: str):
    """
    Loads a json file and returns its data
    """
    with open(json_file_path) as json_file:
        data = json.load(json_file)
    return data

def print_pretty_json(json_data: Dict[Any, Any]):
    """
    Print a python json object (dict) prettified
    """
    json_formatted_str: str = json.dumps(json_data, indent=4)
    print(json_formatted_str)

def save_json_to_file(json_data: dict, filepath: str):
    """
    Saves a json object (as a dict) to a file
    """
    # serialization
    json_str: str = json.dumps(json_data, indent=4)

    # saving to file
    with open(filepath, "w") as file:
        file.write(json_str)

# csv manipulations
def write_in_csv(data: Dict[Any, Any], csv_file_name: str):
    """
    Write a dictionary of URLs to a CSV file with provided name
    """
    with open(csv_file_name, mode='a', encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter=';')

        writer.writerow([data["date"], data["status"]])

# list manipulations
def print_list(list: List[Any]):
    from pprint import pprint
    pprint(list)

# str manipulations
def get_str_time_now(for_logging: bool = True) -> str:
    time_str: str
    if(for_logging):
        time_str = "[time: " + \
            datetime.datetime.now().strftime(
                "%S_%M_%H_%d_%m_%Y"
            ) + "]"
    else:
        time_str = datetime.datetime.now().strftime(
            "%S_%M_%H_%d_%m_%Y"
        )
    return time_str

def limit_line_str(string: str, limit: int = 50) -> str:
    string = string.replace("\n", "")
    if(len(string) > limit):
        string = string[:limit - 1]
    return string