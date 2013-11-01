def selectionsort(a):
    """
    use selection sort to sort a list a
    input: list a
    ouput: list a in non-descending order
    """
    for i in range(0, len(a) - 1):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                # swap the two values
                temp = a[min]
                a[min] = a[j]
                a[j] = temp
    return a

# test part
if __name__ == '__main__':
    a = [199,23,65,190,-23,1,3,5]
    print(selectionsort(a))
