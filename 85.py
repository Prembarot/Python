# 
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
l3=[11,12,13,14,15]
def add(l1,l2,l3):
    return l1+l2+l3
r=map(add,l1,l2,l3)
print(list(r))
