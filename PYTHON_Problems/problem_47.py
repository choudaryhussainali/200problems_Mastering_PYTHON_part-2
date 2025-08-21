# Task:
# Write a function log_message(msg) that writes the message with a timestamp into 'logs.txt'.

# Output in logs.txt:
# [2025-08-05 03:40 PM] User logged in.
# [2025-08-05 03:42 PM] Action completed.

from datetime import datetime

def log_message(msg):
    timestamp = datetime.now().strftime("[%Y-%m-%d %I:%M %p]")
    with open("logs.txt", "a") as f:
        f.write(f"{timestamp} {msg}\n")

log_message("User logged in.")
log_message("Action completed.")

# [2025-08-05 03:40 PM] User logged in.
# [2025-08-05 03:42 PM] Action completed.


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
