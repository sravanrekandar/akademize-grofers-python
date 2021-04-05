a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b and a > c:
    print(f"Max = {a}")
elif b > a and b > c:
    print(f"Max = {b}")
else:
    print(f"Max = {c}")
