#formating with width and alignment
#Some random codes for testing 
subtotal = 1598.4
sales_tax = 103.9
total = 1702.30

output = f"""
suntotal : ${subtotal:>7,.2f}
salesTax : ${sales_tax:<8,.4f}
total : ${total:>19,.6f}
"""

print(output)
string0 = "first string"
string1 = "second string"

print(" " in string0)
print("S" in string1)
print(min("abcf 01234de"))

lis = []
for i in range(32, 129):
    lis.append(chr(i))
    
import random as r

print(lis[0: 45])
r0 = r.randint(32, 129)
r1 = r.randint(32, 129)
r2 = r.randint(32, 129)
r3 = r.randint(32, 129)

print(f"""
The first set of list:
{lis[0: r0]}\n
The second set of list:
{lis[0: r1]}\n
The third set of list:
{lis[0: r2]}\n
And the fouth one:
{lis[0: r3]}
""")

#This block displays the current time on your computer.
import datetime as dt
print(dt.datetime.today())
