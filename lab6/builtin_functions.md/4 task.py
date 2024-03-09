import time
import math

def koren(num, ms):
    time.sleep(ms / 1000)
    res = math.sqrt(num)
    return res

num = 25100
ms = 2123

res = koren(num, ms)

print(f"Square root of {num} after {ms} milliseconds is {res}")