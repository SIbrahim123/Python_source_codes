#unified code camp question for 15 days of code.
#a program that count the number of words per minute.

words = input("Write here: ")
count = 0

for word in words:
    count += 1
    print(word, count)
print(count)
#divide the total word count by 200
minute = int(count / 200)
_count = count - minute
print("\nCount - minute is: ",_count)
seconds = int(((_count) * 0.60) * 100)

print(f"Thats a {minute} minutes, {seconds} seconds read")

