def insertionsort(a):
    for i in range(1, len(a)):
        k = a[i]
        j = i - 1
        while j >= 0 and a[j] > k:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = k

ia = list(map(int, input().split()))
insertionsort(ia)
print(*ia)
