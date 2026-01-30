import json
"""
Personal Info Saver

Save your name, age, favorite colour to JSON
Load it back and print it
Skills: Basic dump/load

"""

"""
The code here Saves your name, age, favorite colour to JSON.

personal_data={"name": "Shade Akinremi", "age": 29, "favorite colour": "mustard yellow" }
file = open("data-file.json","w")
json.dump(personal_data, file)
file.close()
print("Done!")

"""

# The code here loads the saved data back to the console.

file=open("data-file.json", "r")
personal_data_from_file=json.load(file)
file.close()
print(personal_data_from_file)