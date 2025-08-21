# Write a function to swap keys and values in a dictionary, but if multiple keys have the same 
# value, store them as a list in the new dictionary.

def swap_keys_values(d):
    new_dict = {}
    for key, value in d.items():
        if value in new_dict:
            # If value already exists, append to list
            if isinstance(new_dict[value], list):
                new_dict[value].append(key)
            else:
                new_dict[value] = [new_dict[value], key]
        else:
            new_dict[value] = key
    return new_dict


# Test
data = {
    "a": 1,
    "b": 2,
    "c": 1,
    "d": 3,
    "e": 2
}

print(swap_keys_values(data))


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
