#sum until it exceeds 100#
s = 0

while True:
    s += int(input())

    if s > 100:
        break

print(s)