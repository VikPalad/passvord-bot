import random
print("*****добро  пожаловать*****")
print("**this is a passvords bot**")
elements = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_length = int(input("**Enter pass length: "))
password = ""
for i in range(pass_length):
    password += random.choice(elements)
print("**your top secret code**")
print(password)
