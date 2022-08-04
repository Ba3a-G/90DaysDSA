def merge(array1, array2):
    sorted=[]
    h=k=0

    while h < len(array1) and k < len(array2):
        m, n = array1[h], array2[k]
        if m < n:
            sorted.append(m)
            h+=1
        else:
            sorted.append(n)
            k+=1

    sorted.extend(array1[h:]) if k == len(array2) else sorted.extend(array2[k:])
    return sorted

if __name__ == "__main__":
    array1 = [2, 5, 8]
    array2 = [-5, 0, 2, 12, 15]
    print(f"I merge two sorted arrays, like {str(array1)} and {str(array2)} to give {merge(array1, array2)}.")

