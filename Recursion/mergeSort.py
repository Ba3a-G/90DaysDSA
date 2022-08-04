from merge import *

def mergeSort(array):
    if len(array) < 2:
        return array

    midPoint = len(array)//2
    leftPortion = mergeSort(array[:midPoint])
    rightPortion = mergeSort(array[midPoint:])
    return merge(leftPortion, rightPortion)

#Driver Code
testCases = [
    [-2, 5, 4, 3, 3, 21],
    [],
    [21, 20, 19, 18],
    [1, 5000, 10000, 20000],
    [1, "a", 20, 19],
    [1.5, 7, 1000.5]
]

for i in testCases:
    try:
        print(mergeSort(i))
    except Exception as e:
        print(e)