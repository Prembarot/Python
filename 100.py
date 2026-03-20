# wap to take all unique value of 2 sets

stud1=[50,60,70,80,90]
stud2=[10,50,10,60,40,80,20]

print("List1",end="\n")
print("List1 :",stud1)
print("List2 :",stud2)

print("Set :",end="\n")          ### in set  there is no value of repeated value
print("Set1 :",set(stud1))
print("Set2 :",set(stud2))

## UNION OPERATION ON SET
print("Student1 U Student2")
s1=set(stud1)
s2=set(stud2)
allstud = s1.union(s2)
print(allstud)
