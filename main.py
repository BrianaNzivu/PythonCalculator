'''
This is a simple GUI Python calculator project.
'''

def Add (x,y):
    sumNumber = x + y
    return sumNumber

def Multiply (x,y):
    multiplyNumber = x * y
    return multiplyNumber

def divide (x,y):
    divideNumber = x / y
    return divideNumber

def Subtract (x,y):
    subtractNumber = x - y
    return subtractNumber

print('1.Add\n 2.Subtract\n 3.Add \n 4.Multiply')
option = input('Choose an option:')
x = float(input('Enter the first number'))
y = float(input('Enter the second number'))

if option == '1':
    print(Add(x, y))
elif option == '2':
    print()

