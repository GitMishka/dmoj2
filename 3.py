P = int(input().strip())
N = int(input().strip())
R = int(input().strip())

total = N
day = 0

while total <= P:
    N = N * R
    total += N
    day += 1

print(day)
