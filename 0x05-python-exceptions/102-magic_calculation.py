#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for d in range(1, 3):
        try:
            if d > a:
                raise Exception('Too far')
            result += a ** b / d
        except Exception:
            result = b + a
            break
    return result 
