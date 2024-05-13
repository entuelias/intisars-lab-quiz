def bubble_sort(arr):
    size = len(arr)
    for i in range(size - 1):
        for j in range(i + 1, size):
            if arr[j] < arr[i]:
                arr[i], arr[j]  = arr[j], arr[i]
    size -= 1
    return arr
x = bubble_sort(['A','S','C',"I",'I'])
print(x)