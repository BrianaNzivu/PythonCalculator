'''
This is a simple GUI Python calculator project.
'''

# Function for Addition
def Add (x,y):
    sumNumber = x + y
    return sumNumber

# Function for Multiplication
def Multiply (x,y):
    multiplyNumber = x * y
    return multiplyNumber

# Function for Division
def divide (x,y):
    divideNumber = x / y
    return divideNumber

# Function for Subtraction
def Subtract (x,y):
    subtractNumber = x - y
    return subtractNumber

print('1.Add\n 2.Subtract\n 3.Divide \n 4.Multiply')

# Asks user for which operation to be performed
option = input('Choose an option:')

# Two numbers
x = float(input('Enter the first number'))
y = float(input('Enter the second number'))

# Performs operations
if option == '1':
    print(Add(x, y))
elif option == '2':
    print(Subtract(x, y))
elif option == '3':
    print(divide(x, y))
elif option == '4':
    print(Multiply(x, y))
else:
    print('Invalid input')

