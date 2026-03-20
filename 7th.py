# wap to input marks of pcm and print there total and percentage 
# the physics=80, chemistry = 80 ,maths=80 and total =1000, per=80


physics=int(input("marks of physics :"))
chemistry=int(input("marks of chemistry :"))
maths=int(input("marks of maths :"))
total_marks= physics+chemistry+maths
print("Total marks :",total_marks)
percentage= (total_marks*100)/300
print("Percentage :", percentage) 
print(f"Physics= {physics} chemistry={chemistry} maths={maths} total_marks={total_marks} percentage={percentage}")