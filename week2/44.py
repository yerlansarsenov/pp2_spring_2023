
s = input()
arr = s.split()

d = {}
for w in arr:
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

print(d)

'apple sun sun golang'

{
    'apple': 1,
    'sun': 2,
    'golang': 1
}
