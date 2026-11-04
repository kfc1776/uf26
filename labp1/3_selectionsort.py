def selectionsort(a):
    for i in range(len(a) // 2):
        min_idx = i
        max_idx = i
        for j in range(i + 1, len(a) - i):
            if a[j] < a[min_idx]:
                min_idx = j
            if a[j] > a[max_idx]:
                max_idx = j
                
        a[i], a[min_idx] = a[min_idx], a[i]
        
        if max_idx == i:
            max_idx = min_idx
            
        end_idx = len(a) - 1 - i
        a[end_idx], a[max_idx] = a[max_idx], a[end_idx]

ia = list(map(int, input().split()))
selectionsort(ia)
print(*ia)

"""
# не работает
def selectionsort(a):
    l, r = 0, len(a) - 1
    min_idx = 0
    max_idx = 0
    for i in range(len(a)):
        if a[i] < a[min_idx]:
            min_idx = i
        if a[i] > a[max_idx]:
            max_idx = i
    a[l], a[min_idx] = a[min_idx], a[l]
    a[r], a[max_idx] = a[max_idx], a[r]
    l += 1
    r -= 1
    if not is_sorted(a):
        a = [a[l]] + selectionsort(a[l:r+1]) + [a[r]]
    return a
"""
