# Think of any Secret number
import random
multiply_number = random.randrange(1,6)
add_number = random.randrange(5,20)
divide_number = random.randrange(2,4)

input("Think of any Secret number: (then, hit Enter)")
input(f"Multiply it by {multiply_number}: (hit Enter)")
input(f"add {add_number}: (hit Enter)")
input(f"divide by {divide_number}: (hit Enter)")

remain_number = float(input("Now, what is remain?: "))
secret_number = float((remain_number * divide_number - add_number) // multiply_number)
print(f"\nYour Secret Number is: {secret_number}")