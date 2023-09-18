from collections import Counter

a = [12, 3, 4, 3, 5, 11, 12, 6, 7]

count = Counter(a)

print(count)

for x in count.keys():
    print(x)

print('####################')

for y in count.values():
    print(y)