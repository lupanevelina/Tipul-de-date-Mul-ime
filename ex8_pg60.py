A=set(input("Elementele multimii A: "))
B=set(input("Elementele multimii B: "))
a=set()
b=set()
for i in A:
    if ord(str(i))>=48 and ord(str(i))<=57 :
        a.add(int(i))
for i in B:
    if ord(str(i))>=48 and ord(str(i))<=57 :
        b.add(int(i))
print("a)",a.intersection(b))
print("b)",a.union(b))
print("c)A-B: ",a.difference(b))
print("c)B-A: ",b.difference(a))




