# Inputs
marks_1 = int(input("Enter marks1: "))
marks_2 = int(input("Enter marks2: "))
marks_3 = int(input("Enter marks3: "))

# Contants())
THRESHOLD = 35

# Calculations
total = marks_1 + marks_2 + marks_3
avg = total / 3
status = "PASSED"

if marks_1 < THRESHOLD or marks_2 < THRESHOLD or marks_3 < THRESHOLD:
    status = "FAILED"


grade = "A"

if avg < 70 and avg >= 50:
    grade = "B"
else:
    grade = "C"

# Output

print("==============================")
print("---- Report ----")
print("Marks_1   : " + str(marks_1))
print("Marks_2   : " + str(marks_2))
print("Marks_3   : " + str(marks_3))
print("Total     : " + str(total))
print("Percentage: " + str(avg))
print("Status    : " + status)
print("Grade     : " + grade)

