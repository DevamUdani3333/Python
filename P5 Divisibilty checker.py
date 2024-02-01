#write a python program to find whether the entered number is divisible by 7 or not.

num = int(input("Enter the number whose divisibility needs to be checked:"))

div = int(input("Enter the number with which divisibility needs to be checked:"))

if num % div == 0:
    print("The number is divisible.")
else:
    print("The number is not divisible.")