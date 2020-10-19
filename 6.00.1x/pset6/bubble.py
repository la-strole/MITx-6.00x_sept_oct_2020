def booble_search(L:list):
    count = True
    while count:
        count = False
        for item in range(1, len(L)):
            if L[item-1] > L[item]:
                L[item-1], L[item] = L[item], L[item-1]
                count = True
   

L = [1,4,8,4,3,2,6,7,3,4,10]
booble_search(L)
print(L)

