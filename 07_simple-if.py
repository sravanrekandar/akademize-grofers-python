name = input("Enter Your Name: ")
age = input("Enter Your age: ")

age = int(age)

if age >= 18:
    print(f"Hello {name} you are eligible to vote.")

print("Thank you.")

"""
$ python 07_simple-if.py        
Enter Your Name: Sravan
Enter Your age: 12
Thank you.

$ python 07_simple-if.py
Enter Your Name: SRavan
Enter Your age: 22
Hello SRavan you are eligible to vote.
Thank you.
"""