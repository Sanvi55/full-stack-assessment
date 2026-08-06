#sum of numbers until 0 is entered#
s = 0
n = int(input())

while n != 0:
    s += n
    n = int(input())

print(s)