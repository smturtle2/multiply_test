import time

def multiply_1(a: int, b: int):
    d = 0
    while b > 1:
        c = b
        j = 0
        while c > 1:
            c = c >> 1
            j += 1
        d += a << j
        b = b - (1 << j)
    if b == 1:
        d += a << 1
    return d

def multiply_2(a: int, b: int):
    c = 0
    for _ in range(b):
        c += a
    return c

a, b = 423524434, 130493446
start = time.time()
print(f'{a * b} | {time.time() - start:.4e} sec')
start = time.time()
print(f'{multiply_1(a, b)} | {time.time() - start:.4e} sec')
start = time.time()
print(f'{multiply_2(a, b)} | {time.time() - start:.4e} sec')
