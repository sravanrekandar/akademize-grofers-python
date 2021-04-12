def print_multiplecation_table(n):
    for i in range(1, 5+1):
        print(f"{n} * {i} = {n*i}")


def main():
    print("===== Multiplecation Tables =====")
    print_multiplecation_table(2)
    print("---------")
    print_multiplecation_table(5)
    print("---------")
    print_multiplecation_table(10)


main()
