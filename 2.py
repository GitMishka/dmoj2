from heapq import heapify, heappop

n = int(input().strip())
numbers = []

for _ in range(n):
    numbers.append(int(input().strip()))

heapify(numbers)

while numbers:
    print(heappop(numbers))
