def insertionsort(a):
    """
    use insertion sort to sort list a
    input: list a
    output: a in non-descending order
    """
    if len(a) == 1:
        return a

    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        # search for insertion position
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    return a

if __name__ == '__main__':
    a = [3,4,1,66,7,2]
    print insertionsort(a)
            
