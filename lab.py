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