def fib():
    current, nxt = 0, 1

    while True:
        current, nxt = nxt, nxt+current
        yield current


for n in fib():
    if n > 300:
        break

    print(n, end=', ')