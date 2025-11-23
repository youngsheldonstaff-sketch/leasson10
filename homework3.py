
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
c = float(input("Enter the third number (c): "))


print("\nOriginal values: a = {}, b = {}, c = {}".format(a, b, c))

a, b, c = c, a, b

print("Swapped values:  a = {}, b = {}, c = {}".format(a, b, c))
