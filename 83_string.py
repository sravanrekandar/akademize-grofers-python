message = "This is a lorem ipsum text."

print(message)
print(message[0], message[1], message[2], message[3])
print(len(message))
print(message[5:15])
print(message[5:])
print(message[:15])

print("Index of first space: ", message.index(' '))

first_space_index = message.index(' ')
print("Text after first space:", message[first_space_index + 1:])

last_space_index = message.rindex(' ')
print("Text after last space:", message[last_space_index + 1:])

words = message.split(" ")
print(words)

"""
https://www.w3schools.com/python/python_ref_string.asp
https://docs.python.org/3/library/stdtypes.html#string-methods
https://www.digitalocean.com/community/tutorials/an-introduction-to-string-functions-in-python-3
"""
