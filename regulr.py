import re
text = "John is 23 years old and Mike is 25 years old"

numbers  = re.findall(r"\d+", text)
single_numbers = re.findall(r"\d", text)
print(numbers)
print(single_numbers)