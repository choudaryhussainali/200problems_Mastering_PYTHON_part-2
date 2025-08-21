# Task:
# Create a function `explore_module(module_name)` that takes a module name (e.g., math, os)
# and prints all the available functions and classes in it.

# Sample Input:
# explore_module("math")

# Output:
# ['acos', 'asin', 'atan', ..., 'sqrt']


import importlib

def explore_module(module_name):
    try:
        module = importlib.import_module(module_name)
        print(dir(module))
    except ImportError:
        print("Module not found.")

explore_module("math")

# Output:
# ['acos', 'asin', 'atan', ..., 'sqrt']


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
