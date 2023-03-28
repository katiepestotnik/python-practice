def reverse_string (str):
    return str[::-1]

print(reverse_string('hello'))

def fizz_buzz (num):
    for i in range(num):
        result = 'Nope'
        if i % 3 == 0 and i % 5 == 0:
            result = 'fizzbuzz'
        elif i % 3 == 0:
            result = 'fizz'
        elif i % 5 == 0:
            result = 'buzz'
        print(f'{i} = {result}')
fizz_buzz(16)

def calculator(num1, num2, operator):
    if(operator == '+'):
        return f'{num1} + {num2} = {num1 + num2}'
    if(operator == '-'):
        return f'{num1} - {num2} = {num1 - num2}'
    if(operator == '*'):
        return f'{num1} * {num2} = {num1 * num2}'
    if(operator == '/'):
        return f'{num1} / {num2} = {num1 / num2}' if num2 != 0 else 'Can\'t divide by 0'
print(calculator(2,0,'/'))
import random, math
def random_number(low, max):
    while True:
       random_num =  math.floor(random.random() * max)
       if random_num >= low and random_num <= max:
            return random_num

print('this is random', random_number(10, 20))