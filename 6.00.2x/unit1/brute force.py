import knapsack_problem

def brute_force_iteration_method(n: list, maximum: int):
    """
    n: list - [(value, weight),...], value, weight - assumes to be int
    return best values for knapsack
    """
    assert type(n) == list
    assert type(maximum) == int

    number_of_items = len(n)
    # define generator of bin numbers
    bin_numbers = (('{:0' + f'{number_of_items}' + 'b}').format(x) for x in range(2 ** number_of_items))
    # for each bin number - make multiplication with list and control of current weight < maximum and choose the best
    best_bin_num = ''
    best_total_value = 0
    while True:
        try:
            bin_num = next(bin_numbers)
        except StopIteration:
            break
        total_weight = 0
        total_value = 0
        for i in range(number_of_items):
            total_value += int(bin_num[i]) * n[i][0]
            total_weight += int(bin_num[i]) * n[i][1]
            if total_weight > maximum:
                break
        else:
            if total_value > best_total_value:
                best_total_value = total_value
                best_bin_num = bin_num
    # return the best
    return f'best_value={best_total_value}, best_composition={best_bin_num}'


if __name__ == '__main__':
    menu = [(1, 2), (3, 6), (5, 3), (4, 8), (10, 2), (1, 20)]
    max_weight = 10
    print(brute_force_iteration_method(menu, max_weight))
