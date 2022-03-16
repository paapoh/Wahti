import json


with open("data/listings.json", "r") as openfile:
    json_object = json.load(openfile)


def write_json(name: str, url: str, filename="data.json"):

    new_data = json.dumps({name: url}, indent=4)

    with open(filename, "r+") as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)
