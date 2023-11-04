a = int(input('Please enter first number :'))
b = input('Please enter Math operation : "/" or "*" or "+" or "-"')
c = int(input('Please enter second number :'))
if b == '/' and c == 0:
    print("You can't divide by 0")
elif b == '/':
    print('Your result is :', a / c)
elif b == '*':
    print('Your result is :', a * c)
elif b == '+':
    print('Your result is :', a + c)
elif b == '-':
    print('Your result is :', a - c)
