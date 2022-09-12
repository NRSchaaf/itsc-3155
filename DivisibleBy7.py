# First number
num1 = int(input('Enter lower number: '))

# Second number
num2 = int(input('Enter upper number: '))

counter = num1   # initialize counter with first number

# check until end of the range is achieved
x = range(num1, num2)

while x < num2:
    if x % 7 == 0 and x / 5 != 0:
        print(x)
