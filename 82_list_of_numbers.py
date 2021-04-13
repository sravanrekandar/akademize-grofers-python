import sys
numbers = [2, 45, 76, 8, 33, 9, 6, 55]

sum = 0
product = 1
max = -sys.maxsize
min = sys.maxsize

for item in numbers:
    sum += item
    product *= item
    if item > max:
        max = item
    if item < min:
        min = item

avg = sum / len(numbers)


print(f"Sum of {numbers} = {sum}")
print(f"Average = {avg}")
print(f"Max = {max}")
print(f"Min = {min}")
