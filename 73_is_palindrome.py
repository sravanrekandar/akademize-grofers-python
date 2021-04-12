def get_reverse(n):
    i = n
    rev = 0

    while i > 0:
        rem = i % 10
        rev = rev * 10 + rem
        i = i // 10

    return rev


def is_palindrome(n):
    return n == get_reverse(n)


def main():
    print(f"1234 <--> {is_palindrome(1234)} ")
    print(f"5335 <--> {is_palindrome(5335)} ")


main()
