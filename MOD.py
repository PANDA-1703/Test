def MOD(a, b):
    if (a >= 0 and b > 0) or (a >= 0 and b < 0):
        return a % b
    for c in range(0, abs(a)):
        if (abs(a) < abs(b)*c):
            d = abs(b)*c-abs(a)
            return d
        if (abs(a) == abs(b) * c):
            return 0
    print(d)
    return 0


x = int(input("1-ое число: "))
y = int(input("2-ое число: "))
mod = MOD(x, y)
print(mod)
