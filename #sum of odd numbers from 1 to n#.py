#sum of odd numbers from 1 to n#
n = int(input())
s = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        s += i

print(s)