n = int(input())

A = [True]*n

for i in range(2, (int)(n**(1/2) + 1)):
    if A[i] is True:
        for j in range (i*2, n, i):
            A[j] = False

count = 0
for i in range (2, n):
    if A[i] is True:
        count += 1

print(count)
