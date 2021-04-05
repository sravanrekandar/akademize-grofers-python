a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b:
    if a > c:
        print(f"Max = {a}")
    else:
        print(f"Max = {c}")
else:
    if b > c:
        print(f"Max = {b}")
    else:
        print(f"Max = {c}")
