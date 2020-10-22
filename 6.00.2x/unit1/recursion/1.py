def rec(a, b):
    if a == b:
        return b
    else:
        # print(b)
        return rec(a, b - 1)


print(rec(1, 8))


def accerman_function(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return accerman_function(m - 1, 1)
    elif m > 0 and n > 0:
        return accerman_function(m - 1, accerman_function(m, n - 1))


print(accerman_function(2, 2))


def power_two(n):
    if n > 1:
        if n / 2 == 1:
            return 'Yes'
        else:
            return power_two(n / 2)
    else:
        return 'No'


print(power_two(15))


def summa(n):
    # base case - for 0-9 int
    if n // 10 == 0:
        return n % 10
    else:
        return summa(n // 10) + summa(n % 10)


print(summa(127))


def right_to_left(n):
    if n // 10 == 0:
        print(n)
        return n % 10
    else:
        print(n % 10, end='')
        return right_to_left(n // 10)


right_to_left(753)


def left_to_right(n):
    if n // 10 == 0:
        print(n, end='')
        return n % 10
    else:
        return left_to_right(n // 10), left_to_right(n % 10)


left_to_right(753)
