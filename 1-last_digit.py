import random
number = random.randint(-10000, 100000)

" assigns a random number each time its executed"
last_digit = number % 10

:if  number < 0: last_digit = -last_digit

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} is greater than five")

elif last_digit == 0:
    print(f"last digit of {number} is {last_digit} and is 0")
else:
    print(f"last digit of {number} is {last_digit} and is less than 6 and not 0")
