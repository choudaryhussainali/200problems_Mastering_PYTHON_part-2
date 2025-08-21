# Input: "Hussain Ali" → Output: 4

Name = str(input("Enter Your STRING :- "))
count = 0

for i in Name:
    if i in ["a","e","i","o","u"]:
        count += 1


if count == 0:
    print("No Vowels found in Your STRING")

else:
    print(f"Total {count} vowels in your string")



# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
