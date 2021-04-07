def print_line(n):
    for i in range(n):
        print("_", end="")
    print()


def main():
    for i in range(20):
        print_line(i + 1)


main()
