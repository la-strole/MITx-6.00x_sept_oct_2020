import time


def hanoi(n, d1, d2, d3):
    if n == 1:
       pass
       # print(d1, d2)
    else:
        hanoi(n - 1, d1, d3, d2)
        hanoi(1, d1, d2, d3)
        hanoi(n - 1, d3, d2, d1)


t0 = time.time()
hanoi(25, 'd1', 'd2', 'd3')
print(f'time = {time.time() - t0}')