def binarysearchrecur(a,k,l,r):
    """
    impement recursive binary search
    input: an ordered list a, key k, left l, right r;
    output: the position of k; or -1(can not find k)
    """
    if l > r:
        print -1
    else:
        m = (l + r) / 2
        if k == a[m]:
            print m
        elif k < a[m]:
            binarysearchrecur(a, k, l,m - 1)
        else:
            binarysearchrecur(a, k, m + 1, r)


if __name__ == "__main__":
    a = [-12, -3, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 99, 1324, 4215124]
    l = 0
    r = len(a) - 1
    k = 123123
    binarysearchrecur(a, k, l, r)
    binarysearchrecur(a, 5, l, r)
    binarysearchrecur(a, 1324, l, r)
    
    
