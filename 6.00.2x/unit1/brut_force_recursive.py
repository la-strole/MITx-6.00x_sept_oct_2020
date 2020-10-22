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

    def getCost(self):
        return self.weight

    def getValue(self):
        return self.value


menu = [(1, 2), (3, 6), (5, 3), (4, 8), (10, 2), (1, 20)]
consider = [Foo(x, y) for x, y in menu]
print(maxVal(consider, 10))