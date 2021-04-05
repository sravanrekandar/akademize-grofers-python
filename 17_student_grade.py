# Inputs
marks_1 = int(input("Enter marks1: "))
marks_2 = int(input("Enter marks2: "))
marks_3 = int(input("Enter marks3: "))

# Contants())
THRESHOLD = 35

# Calculations
total = marks_1 + marks_2 + marks_3
avg = total / 3
if marks_1 >=THRESHOLD and marks_2 >=THRESHOLD and marks_3 >=THRESHOLD:
    status = "PASSED" 
else:
    status = "FAILED"

# Output

print("==============================")
print("---- Report ----")
print("Marks_1   : " + str(marks_1))
print("Marks_2   : " + str(marks_2))
print("Marks_3   : " + str(marks_3))
print("Total     : " + str(total))
print("Percentage: " + str(avg))
print("Status    : " + status)

