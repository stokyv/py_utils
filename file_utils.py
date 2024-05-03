import os
import os
from datetime import datetime
import json

##list all contents of a folderin absolute file path format
def list_files(starting_directory):
    result = []
    for root, dirs, files in os.walk(starting_directory):
        for file in files:
            # get the full path
            file_path = os.path.join(root, file)
            # print(file_path)
            result.append(file_path)
        # print(f'Folder: {root}')
        # print(f'Files: {files}')
    return result

# Usage
# path = r'D:\test1'
# result = list_files(path)
# result


def count_files_by_directory(starting_directory):
    for root, dirs, files in os.walk(starting_directory):
        print(f"Directory: {root}, File count: {len(files)}")

# Usage
# count_files_by_directory(path)

def find_files(starting_directory, file_extension):
    found_files = []
    for root, dirs, files in os.walk(starting_directory):
        for file in files:
            if file.endswith(file_extension):
                found_files.append(os.path.join(root, file))
    return found_files

# Usage
# result = find_files(path, ".txt")
# print("Found .txt files:")
# for file_path in result:
#     print(file_path)


def write_to_txt(lst, txt_file_path):
    with open(txt_file_path, 'w') as f:
        for line in lst:
            f.write(line + '\n')
    print('Content written to {txt_file_path}')


##write contents of a folder in a dictionary format
#return the contents of a folder in the dictionary format
def list_files1(starting_directory):
    result = []
    for root, dirs, files in os.walk(starting_directory):
        for file in files:
            # Join the current root path with the filename to get the full path
            file_path = os.path.join(root, file)
            # print(file_path)
        # print(f'Folder: {root}')
        # print(f'Files: {files}')
        result.append((root, files))
    data = {}
    for root, files in result:
        data[root] = files
    return data

# Usage
# data = list_files1(path)
# data


import json
from datetime import datetime


def write_data_with_timestamp(data, file_path):
    """
    Write contents of a folder to a json file
    """
    # Create a dictionary with data and timestamp
    data_with_timestamp = {
        #call isoformat() to turn datetime obj into a string
        "timestamp": datetime.now().isoformat(), 
        "data": data,        
    }

    # Serialize dictionary to JSON format
    json_data = json.dumps(data_with_timestamp, indent=2)

    # Write JSON data to file
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json_data)

# data = list_files1(path)
# write_data_with_timestamp(data, 'output.json')
##load data
# loaded_data = load_json_file(json_file_path)
