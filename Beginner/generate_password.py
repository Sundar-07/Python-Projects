"""
to create a password, declare a string of numbers + uppercase + lowercase + special characters. 
Take a random sample of the string of a length given by the user
"""

import random

password_length = int(input("Enter your password length: "))

# your own alphabets or symbols etc./

sym_alphs = "abcdefghijklmnopqrtuvwxyzASDFGHJKLPOIUYTREWQZXCVBNM!@#$%^&*_+12345"

"""
The sample() method returns a list
with a randomly selection of a specified number of items from a sequnce.

syntax: random.sample(sequence, k)

sequence	Required. A sequence. Can be any sequence: list, set, range etc.
k	Required. The size of the returned list
"""

final_pass = "".join(random.sample(sym_alphs,password_length))

print(final_pass)