def get_reverse(n):
    i = n
    rev = 0

    while i > 0:
        rem = i % 10
        rev = rev * 10 + rem
        i = i // 10

    return rev


def main():
    print(f"1234 <--> {get_reverse(1234)} ")
    print(f"5335 <--> {get_reverse(5335)} ")


main()

"""
n       i       rev                 rem 
-----------------------------------------
1234    1234    0                     4
                0 * 10 + 4 = 4
        123                           3
                4 * 10 + 3 = 43
        12                            2
                43 * 10 + 2 = 432
        1                              1
                432 * 10 + 1 = 4321
        0


10) 1234 (123
    123
    ----
    4

10) 1 (0
    0
   ---
    1

"""
