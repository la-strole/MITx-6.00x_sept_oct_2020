def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2 ** N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list
        of which item(s) are in each bag.
    """

    for i in range(2 ** len(items)):
        combo_bag1 = []
        combo_free = []
        # here we have bin combination 10010101
        for j in range(len(items)):
            if (i >> j) % 2 == 1:
                # if 1 in bin combination - append to bag1
                combo_bag1.append(items[j])
            else:
                # if binary representation == 0 - item will not go to bag 1
                # item can put on bag 2 or on free space
                combo_free.append(items[j])

        #print(f'bag1={combo_bag1}\nfree_items={combo_free}')
        for m in range(2 ** len(combo_free)):
            combo_bag2 = []
            for n in range(len(combo_free)):
                if (m >> n) % 2 == 1:
                    combo_bag2.append(combo_free[n])
            yield combo_bag1, combo_bag2


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



items = [str(x) for x in range(3)]

foo = brute_triple(items)

while True:
    try:
        print(next(foo))
    except StopIteration:
        break
