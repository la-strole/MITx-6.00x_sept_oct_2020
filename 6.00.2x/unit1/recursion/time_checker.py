from timeit import timeit
b = 10
c = 0
print(timeit("""
try:
    a = b / c
except ZeroDivisionError:
    pass
"""
,globals=globals(), number=10000000))

