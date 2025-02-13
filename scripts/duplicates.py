# this input list contains duplicates
mylist = [
    # First list
    "485754433959F09B",
    "4857544339D7D69B",
    "48575443391A1E9B",
    "485754433930689B",
    "4857544339089E9B",
    # Second list
    "485754433959F09B",
    "4857544339D7D69B",
    "48575443391A1E9B",
    "485754433930689B",
    "4857544339089E9B"
]

# find the length of the list
print(len(mylist))
8

# create a set from the list
myset = set(mylist)

# find the length of the Python set variable myset
print(len(myset))
6