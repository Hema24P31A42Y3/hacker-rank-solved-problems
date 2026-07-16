from itertools import product
k,m= map(int,input().split())
lists = []
for _ in range(k):
    row = list(map(int,input().split()))
    lists.append(row[1:])
maximum = 0
for combination in product(*lists):
    total= 0
    for num in combination:
        total += num ** 2
    value = total % m
    if value > maximum:
        maximum = value
print(maximum)
