# wap to input marks of 3 sub and print whwether student is pass or not idf marks of each subject must be greater then 40 


physics=int(input("marks of physics :"))
chemistry=int(input("marks of chemistry :"))
maths=int(input("marks of maths :"))
total_marks= physics+chemistry+maths
print("Total marks :",total_marks)
percentage= (total_marks*100)/300
print("Percentage :", percentage) 
if percentage>=90 :
    print(percentage,"Grade A")
elif percentage>=80 and percentage<90 :
    print(percentage,"Grade B ")
elif percentage>=70 and percentage<80 :
    print(percentage,"Grade C ")
elif percentage>=60 and percentage<70 :
    print(percentage,"Grade D ")
else :
    print(percentage,"Grade E ")
    
