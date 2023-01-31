a = {1, 2, 3, 4, 5, 6, 7, 8, 9}

n = int(input())

for i in range(n):
    q = input().split(' ')
    if q[0] == 'pop':
        a.pop()
    elif q[0] == 'remove':
        a.remove(int(q[1]))
    elif q[0] == 'discard':
        a.discard(int(q[1]))

s = sum(a)
print(s)
