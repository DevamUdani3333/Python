#write a python program to find largest number from given three numbers

a = int(input('Enter first number : ')) 
b = int(input('Enter second number : ')) 
c = int(input('Enter third number : ')) 
largest = 0 
if a > b and a > c : largest = a 
elif b > c : largest = b 
else : largest = c 
print(largest, "is the largest of three numbers.")