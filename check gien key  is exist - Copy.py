#Write a Python script to check if a given key already exists in a dictionary.

my_dict = {"apple": 1, "banana": 2, "orange": 3}
def key_exists(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False
if key_exists(my_dict, "apple"):
    print("The key 'apple' exists in the dictionary.")
else:
    print("The key 'apple' does not exist in the dictionary.")
