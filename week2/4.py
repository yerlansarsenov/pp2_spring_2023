s = input()

counts = {}
for w in s.split():
    if w in counts:
        counts[w] += 1
    else:
        counts[w] = 1

print(counts)