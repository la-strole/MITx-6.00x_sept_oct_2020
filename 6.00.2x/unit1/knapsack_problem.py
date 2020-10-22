class Item(object):
    def __init__(self, name='default name', value=0, weight=0):
        assert type(value) == int, f'item.__init_(): value is not integer'
        assert type(weight) == int, f'item.__init_(): weight is not integer'
        assert value > 0 and weight > 0, f'item.__init_(): weight or value is not positive'
        assert type(name) == str, f'item.__init_(): name is not string'
        self.value = value
        self.weight = weight
        self.name = name

    def __str__(self):
        return f'{self.name}\tvalue={self.value}\tweight={self.weight}'

    def __repr__(self):
        return f'Item(name={self.name}, value={self.value}, weight={self.weight})'

    def get_value(self):
        return self.value

    def get_weight(self):
        return self.weight

    def get_name(self):
        return self.name


def make_I_vector(name, value, weight):
    assert type(name) == list
    assert type(value) == list
    assert type(weight) == list
    assert len(value) == len(name) == len(weight)

    return [Item(name[x], value[x], weight[x]) for x in range(len(name))]


def greedy_flexible_knapsack(i_vector, maxW, sort_key):
    i_vector_copy = sorted(i_vector, key=sort_key, reverse=True)
    result = []
    total_weight = 0
    i = 0
    while total_weight <= maxW:
        if i_vector_copy[i].get_weight() <= maxW - total_weight:
            result.append(i_vector_copy[i])
        total_weight += i_vector_copy[i].get_weight()
        i += 1
    return result


if __name__ == '__main__':
    names = ['one', 'two', 'tree', 'four', 'five', 'six']
    values = [1, 3, 5, 4, 10, 1]
    weights = [2, 6, 3, 8, 2, 20]

    i_Vector = make_I_vector(names, values, weights)
    answer = greedy_flexible_knapsack(i_Vector, maxW=10, sort_key=lambda x: x.get_value())
    print(answer)
