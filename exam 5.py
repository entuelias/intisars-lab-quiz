def merge(seq, left_half, right_half):
    n = int(input("how many numbers you want to enter:"))
    seq = []
    for i in range(1, n + 1):
        x = int(input(f"enter the{i} element:  "))
        seq.append(x)
    print(seq)

    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            seq[k] = left_half[i]
            i += 1
        else:
            seq[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        seq[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        seq[k] = right_half[j]
        j += 1
        k += 1


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call on the left and right halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the two sorted halves
        merge(arr, left_half, right_half)
print(merge())