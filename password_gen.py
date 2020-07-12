#This program prints a set of random characters that can be used as passwords
#This program will be used to write a password generating application as the
#integration continues.

upper_case = []
for i in range(65, 91):
    upper_case.append(chr(i))

lowercase = []
for i in range(97, 123):
    lowercase.append(chr(i))

numbers = []
for i in range(48, 58):
    numbers.append(chr(i))

symbols = []
for i in range(32, 48):
    symbols.append(chr(i))

for i in range(58, 65):
    symbols.append(chr(i))

for i in range(91, 97):
    symbols.append(chr(i))

for i in range(123, 129):
    symbols.append(chr(i))

upper = f"All the uppercase letters in the ascii table \n{upper_case}"
lower = f"All the lower case \n{lowercase}"
num = f"All the numbers in the ascii table \n{numbers}"
sym = f"Symbols \n{symbols}"

print(upper)
print(lower)
print(num)
print(sym)

count = 0
for i in symbols:
    count += 1

print(f"\nThere are {count} symbols in the symbols list.")
