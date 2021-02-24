import json

infile = open("eq_data_1_day_m1.json", "r")
outfile = open("readable_eq_data.json", "w")

# The json.load() function converts the data into a
# format Python can work with: in this case
# a giant dictionary

eq_data = json.load(infile)

# the json.dump() function takes a JSON data object and a file object, and
# file. The indent=4 argument tells dump() to format the data using indent
# the data's structure.

json.dump(eq_data, outfile, indent=4)

print(eq_data["metadata"])
