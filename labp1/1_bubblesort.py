def bubblesort(a):
    i = 0
    while i < len(a) - 1:
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            i = 0
        else:
            i += 1
    return a

ia = list(map(int, input().split()))
print(*bubblesort(ia))
