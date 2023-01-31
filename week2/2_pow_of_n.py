def task1(products):
    print('I have')
    for p in products:
        print(p, ', ')
    print(' in my shopping cart')

def task2():
    a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    n = int(input())
    for i in range(n):
        c = input()
        if c == 'pop':
            a.pop()
        elif c == 'remove':
            e = int(input())
            a.remove(e)
        elif c == 'discard':
            e = int(input())
            a.discard(e)
    print(sum(a))


n = int(input())

ans = 1

for i in range(1, n + 1):
    ans *= 2

print(ans)
