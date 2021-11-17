import itertools
A=set({1,2,3,4})
for i in range(1,len(A)+1):
    a=set(itertools.combinations(A, i))
    print(a)
    
