#negative number and stop at 0#
while True:
    n = int(input())

    if n == 0:
        break
    if n < 0:
        continue

    print(n)