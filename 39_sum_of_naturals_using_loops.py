def get_sum(n):
    s = 0
    for i in range(1, n+1):
        s = s + i

    return s


def main():
    n = int((input("Enter n: ")))
    sum = get_sum(n)
    print(f"Sum of first {n} Natural numbers = {sum}")


main()

"""
i           s
-----------------
            0
1           0 + 1 = 1 
2           1 + 2 = 3
3           3 + 3 = 6 
"""
