# Exercise 18: Number to Words Converter

# Ask the user to enter an integer between 0–999. Convert it into words using type conversion and string manipulation (e.g., 123 → "one two three").

num = input("Enter an integer between 0–999: ")

if num.isdigit() and 0 <= int(num) <= 999:
    word_list = [int(digit) for digit in num]  # convert each digit
    num_words = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    result = " ".join([num_words[d] for d in word_list])
    print("Number in words:", result)
else:
    print("Invalid input! Enter a number between 0 and 999.")


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
