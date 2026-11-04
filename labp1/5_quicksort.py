# https://colab.research.google.com/drive/1ULH3YEQSQmRpcqgomgli-b80yC35ihSE?usp=sharing

def qs(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    l = [x for x in arr[1:] if x < pivot]
    r = [x for x in arr[1:] if x >= pivot]
    return qs(l) + [pivot] + qs(r)


ia = list(map(int, input().split()))
print(*qs(ia))
