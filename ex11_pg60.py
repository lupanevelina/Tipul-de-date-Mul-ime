import itertools
A=set({"A","B","C","D"})
for i in range(1,len(A)+1):
    a=set(itertools.combinations(A, i))
    print(a)