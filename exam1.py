def check_duplicate():
    count = 0
    target = int(input("enter the number to be searched:"))

    n=int(input("how many numbers you want to enter:"))
    seq = []
    for i in range(1,n+1):
        x=int(input(f"enter the{i} element:  "))
        seq.append(x)
    for i in range(len(seq)):
        if seq[i] == target:
            count += 1
    return count
print(check_duplicate())






