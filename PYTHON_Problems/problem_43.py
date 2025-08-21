# Task:
# Print the current date and time in this format:
# "Today is: 05-Aug-2025 | Time: 03:35 PM"

# Use datetime module with formatting.

from datetime import datetime

now = datetime.now()

formatted = now.strftime("Today is %d-%b-%Y | Time: %I-%M-%p ")
print(formatted)

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
