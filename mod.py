import time

# idea
# 10 * 10 -> 10 * [8 + 2] -> 10 * 2 ** 3 + 10 * 2 ** 1 -> 10 << 3 + 10 << 1
# first:    find max shift
# second:   calculate validation
# last:     shift left by valid value and sum
# optimization:
#   when find max shift, use binary search
#   when calculate validation, immediately shift and sum
# optimization 2:
#   find valid value by binary search

def _multiply_1(a: int, b: int):
    if b == 0:
        return 0
    if b == 1:
        return a
    
    # find max shift
    _min = 1
    _max = _min
    while (b >> _max) > 0:
        _max = _max << 1
    p = 1
    while _max - _min > 1:
        p = (_max + _min) >> 1
        c = b >> p
        if c > 1:
            _min = p
        elif c == 1:
            break
        else:
            _max = p
    
    # find valid, shift and sum
    d = 0
    while b > 0:
        _max = p + 1
        _min = 0
        _p = 1
        while _max - _min > 1:
            _p = (_max + _min) >> 1
            c = 1 << _p
            if c < b:
                _min = _p
            else:
                _max = _p
        b -= 1 << _p
        d += a << _p
        p = _p - 1

    return d

def multiply_1(a: int, b: int):
    return _multiply_1(a, b) if b >= 0 else ((-1 ^ _multiply_1(a, (-1 ^ b) + 1)) + 1)

def multiply_2(a: int, b: int):
    c = 0
    for _ in range(b):
        c += a
    return c

def compare_multiply(a: int, b: int):
    start = time.time()
    print(f'{a * b} | {time.time() - start:.4e} sec')
    start = time.time()
    print(f'{multiply_1(a, b)} | {time.time() - start:.4e} sec')
    #start = time.time()
    #print(f'{multiply_2(a, b)} | {time.time() - start:.4e} sec')

compare_multiply(32, 33)
