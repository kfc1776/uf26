def heapify(a, i, n):
    l = 2 * i + 1
    r = 2 * i + 2

    m = i

    if l < n and a[l] > a[m]:
        m = l
    
    if r < n and a[r] > a[m]:
        m = r

    if m != i:
        a[i], a[m] = a[m], a[i]
        heapify(a, m, n)


def heapsort(a):
    for i in range(len(a) // 2 - 1, -1, -1):
        heapify(a, i, len(a))

    for i in range(len(a) - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, 0, i)

ia = list(map(int, input().split()))
heapsort(ia)
print(*ia)
