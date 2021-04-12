# 3! = 3 x 2 x 1
# 3! = 1 x 2 x 3
# 5! = 5 x 4 x 3 x 2 x 1

def get_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i

    return fact


def main():
    print(f"3! = {get_factorial(3)}")
    print(f"5! = {get_factorial(5)}")


main()
