def bubblesort(a):
    na = a
    i = 0
    while i < len(na) - 1:
        if na[i] > na[i + 1]:
            na[i], na[i + 1] = na[i + 1], na[i]
            i = 0
        else:
            i += 1
    return na

ia = list(map(int, input().split()))
print(*bubblesort(ia))
