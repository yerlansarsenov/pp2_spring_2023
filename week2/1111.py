n = int(input())

for i in range(1, n + 1):
    m = ''
    if i % 15 == 0:
        m = 'FizzBuzz'
    elif i % 3 == 0:
        m = 'Fizz'
    elif i % 5 == 0:
        m = 'Buzz'
    else:
        m = i
    end = '.' if i == n else ', '
    print(m, end=end)
    if i % 10 == 0:
        print()
