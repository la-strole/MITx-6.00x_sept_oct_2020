def selection(L:list):
    L_copy = []
    length = len(L)
    for item in range(length):
        L_copy.append(min(L))
        L.remove(L_copy[-1])
    return L_copy


def selection_from_professor(L:list):
    L_copy = L.copy()
    suffixSt = 0
    while suffixSt != len(L_copy):
        for i in range(suffixSt, len(L_copy)):
            if L_copy[i] < L_copy[suffixSt]:
                L_copy[suffixSt], L_copy[i] = L_copy[i], L_copy[suffixSt]
        suffixSt += 1
    return L_copy

L = [1,5,7,23,8,9,3,11]

print(selection(L))
L = [1,5,7,23,8,9,3,11]
print(selection_from_professor(L))
