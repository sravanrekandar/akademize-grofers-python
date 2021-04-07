def print_sum(num):
    sum = (num * (num+1)) / 2
    print(f"Sum of first {num} Natural numbers = {sum}")


def main():
    n = int(input("Enter n: "))
    print_sum(n)


main()
