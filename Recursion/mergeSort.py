def merge(array1, array2):
    mergedArray = []
    visited = []
    while len(array1) !=0 and len(array2) !=0:
        for i in array1:
            if i < array2[0]:
                mergedArray.append(i)
                visited.append(i)
            else:
                mergedArray.append(array2[0])
                array2.remove(array2[0])
        for k in visited:
            array1.remove(k)
        visited=[]
    remaining = array1+array2
    mergedArray.extend(remaining)
    return mergedArray

print(merge([5, 9, 150], [1, 16, 17, 20, 23, 25, 26, 34, 54, 65, 78, 99]))