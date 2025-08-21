# Exercise 17: Type-Based Mapping

# Take 5 values from the user. For each:

# If int → cube it

# If float → square root it

# If string → replace vowels with *

import math

values = [input(f"Enter value {i+1}: ") for i in range(5)]
result = []

for v in values:
    # Try int
    try:
        num = int(v)
        result.append(num ** 3)
        continue
    except ValueError:
        pass

    # Try float
    try:
        num = float(v)
        result.append(math.sqrt(num))
        continue
    except ValueError:
        pass

    # Treat as string
    transformed = ""
    for ch in v:
        if ch.lower() in 'aeiou':
            transformed += '*'
        else:
            transformed += ch
    result.append(transformed)

print("Mapped list:", result)


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
