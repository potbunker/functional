def fizzbuzz(number):
    fizz = lambda x: 'fizz' if x % 3 == 0 else ''
    buzz = lambda x: 'buzz' if x % 5 == 0 else ''
    pazz = lambda x: 'pazz' if x % 7 == 0 else ''
    return str(number) + ': ' + ''.join([fizz(number), buzz(number), pazz(number)])

for x in range(2000):
    print fizzbuzz(x)



