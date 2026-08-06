#largest number in a list#
a = [12, 45, 67, 23, 89, 34]
l = a[0]

for i in a:
    if i > l:
        l = i

print(l)