
import sys
import clipboard
import json

"""
# Paste Data 'Ctrl + v'
paste = clipboard.paste()
print(paste)

# Copy Data 'Ctrl + c'
copy = clipboard.copy("Hello Man, How Are You")

print(clipboard.paste())
"""

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w") as file:
        json.dump(data, file)

def load_data(filepath):
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a Key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data Saved!")

    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data Copied to Clipboard")
        else:
            print("Key Does Not Exist.")

    elif command == "list":
        print(data)

    else:
        print("Unkown Command")

else:
    print("Please Pass Exactly One Command.")


