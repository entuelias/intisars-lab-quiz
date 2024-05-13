def deleteElement(array,index):

    for i in range(len(array)):
        if i == index:
            array.pop(index)
    return array

print(deleteElement([3,7,1,9,4],9))

