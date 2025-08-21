# Input: start = 3, end = 12  
# Output: 4 6 8 10 12




def find_even_numbers(start, end):
  even_numbers = []
  for num in range(start, end + 1):
    if num % 2 == 0:
      even_numbers.append(num)
  return even_numbers

# Example usage
start_num = 3
end_num = 12
result = find_even_numbers(start_num, end_num)
print(*result)

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
