import time

def multiply_1(a: int, b: int):
    i = []
    while b > 1:
        c = b
        j = 0
        while c > 1:
            c = c >> 1
            j += 1
        i.append(j)
        b = b - (1 << j)
    if b == 1:
        i.append(0)
    shifted = [a << x for x in i]
    return sum(shifted)

def multiply_2(a: int, b: int):
    c = 0
    for _ in range(b):
        c += a
    return c

start = time.time()
print(multiply_1(423524434, 423524434), time.time() - start, 'sec')
start = time.time()
print(multiply_2(423524434, 423524434), time.time() - start, 'sec')
