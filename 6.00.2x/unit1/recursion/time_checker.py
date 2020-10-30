from timeit import timeit
number_iter = 10000000
print(timeit("""
items = [1,2,3,4,5,6,7,8]
def to_ternary(n):
    if n < 3:
        return str(n)
    else:
        return to_ternary(n//3) + str(n % 3)


def brute_triple(items):
    for dec_num in range(3**len(items)):
        mask = ('{:>0' + f'{len(items)}'+'}').format(to_ternary(dec_num))
        bag1 = []
        bag2 = []
        for value in range(len(items)):
            if mask[value] == '0':
                bag1.append(items[value])
            elif mask[value] == '1':
                bag2.append(items[value])
        yield bag1, bag2
brute_triple(items)
"""
,globals=globals(), number=number_iter))

print(timeit("""
items = [1,2,3,4,5,6,7,8]
def yieldAllCombos(items):
    N = len(items)
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            val = ternShift(i, j) % 3
            if val == 1:
                bag1.append(items[j])
            elif val == 2:
                bag2.append(items[j])
        yield (bag1, bag2)

def ternShift(operand, shift):
    if shift == 0:
        return operand
    else:
        return int(operand//3**shift)
        
yieldAllCombos(items)
"""
,globals=globals(), number=number_iter))

print(timeit("""
items = [1,2,3,4,5,6,7,8]
def yieldAllCombos(items):
    N = len(items)
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            val = int(i // 3**j) % 3
            if val == 1:
                bag1.append(items[j])
            elif val == 2:
                bag2.append(items[j])
        yield (bag1, bag2)
yieldAllCombos(items)
"""
,globals=globals(), number=number_iter))