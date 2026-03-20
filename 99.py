# wap to take 2 list and find non matching elements from list 

stud1=[50,60,70,80,90]
stud2=[10,5,10,60,40,80,20]

print("List1",end="\n")
print("List1 :",stud1)
print("List2 :",stud2)

print("Set :",end="\n")          ### in set  there is no value of repeated value
print("Set1 :",set(stud1))
print("Set2 :",set(stud2))

## SET DIFFERENCE OPERATION ON SET
print("Student1 - Student2")
print(list(set(stud1)-set(stud2)))
print("Student2 - Student1")
print(list(set(stud2)-set(stud1)))
