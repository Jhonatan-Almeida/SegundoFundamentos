for n in range(2, 101):
    if all(n % d for d in range(2, int(n**.5) + 1)):
        print(n)