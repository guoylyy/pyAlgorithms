def shellsort(a):
	dist=len(a)/2
	while dist>0:
		for i in range(dist,len(a)):
			tmp=a[i]
			j=i
			while j>=dist and tmp<a[j-dist]:
				a[j]=a[j-dist]
				j-=dist
			a[j]=tmp
		dist/=2
	return a
    
if __name__ ==  '__main__':
    a = [12,3,1,5,56,345]
    print shellsort(a)
