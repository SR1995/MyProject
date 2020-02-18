def sort(A,i,j):
	if A[j]<A[i] and i<=0:
		A[i],A[j] = A[j],A[i]
		j = i
		i = i-1
		sort(A,i,j)
	else:
		return
A = [5,4,3,2,1]
i = 0
j = 1
sort(A,i,j)
print(A)