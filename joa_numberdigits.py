import math

numbers = 258745
digits = len(str(numbers))

print(digits)

digits = int(math.log10(numbers))+1

print(digits)

number = int(input("Introduce un número:"))

if number % 2 == 0:
    print("Es par")
else:
    print("Es impar")
