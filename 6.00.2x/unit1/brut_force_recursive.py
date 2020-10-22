def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
    Returns a tuples of the total value of a solution to the 0/1 knapsack
    problem and the items of that solution"""
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        # Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        # Explore left branch
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCost())
        withVal += nextItem.getValue()
        # Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        # Explore better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result


class Foo:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        return f'Foo({self.value},{self.weight})'

    def getCost(self):
        return self.weight

    def getValue(self):
        return self.value

    def __le__(self, other):
        if self.getValue() < other.getValue:
            return True


menu = [(1, 2), (3, 6), (5, 3), (4, 8), (10, 2), (1, 20)]
consider = [Foo(x, y) for x, y in menu]
print(maxVal(consider, 10))


def my_recursion(queue: list, free_space: int, knapsack: list):
    """
    queue: list - list of instances of Foo class
    max_weight: int
    """
    if len(queue) == 0:
        if not knapsack:
            return [], 0
        elif free_space < 0:
            return [], 0
        else:
            return knapsack, sum([x.getValue() for x in knapsack])
    else:
        # 5 put queue[0] on knapsack, evolute freespace
        without_item = my_recursion(queue[1:], free_space, knapsack)
        knapsack_copy = knapsack[:]
        knapsack_copy.append(queue[0])
        with_item = my_recursion(queue[1:], free_space - queue[0].getCost(), knapsack_copy)
        if (with_item[1]) > without_item[1]:
            return with_item
        else:
            return without_item


print(my_recursion(consider, 10, knapsack=[]))
