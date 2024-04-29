# Think of any Secret number, and I'll find that out!
import random

multiply_number = random.randrange(2,5)
add_number = random.randrange(2,11, 2)
divide_number = random.randrange(2,5, 2)

input("\nThink of any Secret number: (hit Enter)")
input(f"Multiply it by {multiply_number}: (hit Enter)")
input(f"add {add_number}: (hit Enter)")

remain_number = float(input(f"Divide by {divide_number}, and what is remain?: "))
secret_number = float((remain_number * divide_number - add_number) // multiply_number)
print(f"---------------------------\nYour Secret Number is: {secret_number}\n---------------------------")
