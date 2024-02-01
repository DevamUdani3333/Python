#write a python program to find whether the given number is given is odd or evendef test_odd_even():
    
def test_odd_even():
    try:
        num = int(input("Enter any number to test whether it is odd or even: "))
        if num % 2 == 0:
            print("The number is even")
        else:
            print("The provided number is odd")
    except ValueError:
        print("Invalid input. Please enter an integer.")

test_odd_even()


while True:
    try:
        num = int(input("Enter any number to test whether it is odd or even (or type 'quit' to stop): "))
        if num % 2 == 0:
            print("The number is even")
        else:
            print("The provided number is odd")
    except ValueError:
        if input.lower() == 'quit':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter an integer or type 'quit' to stop.")

test_odd_even()