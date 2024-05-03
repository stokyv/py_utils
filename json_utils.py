import json

def load_json_file(file_path):
    """Load JSON data from a file into a Python dictionary."""
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


# loaded_data = load_json_file(json_file_path)

# print("Loaded JSON data:")
# print(loaded_data)
