#This code aims at reversing some specific digit entered by the user.

def two(num):
    num0 = int(num)
    num2 = num0 % 10
    num1 = int(num0 / 10)
    print(f'The reversed form of {num} is {num2}{num1}')

def three(num):
    num0 = int(num)
    num3 = num0 % 10
    num2 = int((num0 % 100) / 10)
    num1 = int(num0 / 100)
    print(f'The reversed form of {num0} is {num3}{num2}{num1}')

def four(num):
    num0 = int(num)
    num4 = num0 % 10
    num3 = int((num0 % 100) / 10)
    num2 = int((num0  % 1000) / 100)
    num1 = int(num0 / 1000)
    print(f'The reversed form of {num0} is {num4}{num3}{num2}{num1}')

while True: 
    num = input("Enter the number to be reversed: ")
    if len(num) == 2:
        two(num)
    if len(num) == 3:
        three(num)
    if len(num) == 4:
        four(num)
    if len(num) == 5:
        five(num)
