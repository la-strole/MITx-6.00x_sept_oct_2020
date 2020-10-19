def merge(left: list, right: list):
    """
    left, right - sorted lists
    left    right   res
    [1,4,7] [2,3,10] []
    [4,7]   [2,3,10] [1]
    [4,7]   [3,10]   [1,2]
    [4,7]   [10]     [1,2,3]
    [7]     [10]     [1,2,3,4]
    []      [10]     [1,2,3,4,7]
    []      []       [1,2,3,4,7,10]
    O(n)
    """
    i = 0
    j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    if i == len(left):
        return res + right[j:]
    else:
        return res + left[i:]

#print(merge([2,3,10], [1,4,7]))


def sort_merge(L: list):
    """
    use recursive method to sort list
    base case - len(L) == 1 - list with one element is sorted
    """
    # base case
    if len(L) <= 1:
        return L
    else:
        middle = len(L) // 2
        left = L[:middle]
        right = L[middle:]
        return merge(sort_merge(left), sort_merge(right))

L = [2,3,10,1,4,7]
print(sort_merge(L))