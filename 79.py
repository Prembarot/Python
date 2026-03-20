# 

def student_info():
    return "Prem", 100, ["Maths","Science"]

name,marks,subject = student_info()
print("Name :",name)
print("Marks :",marks)

for sub in subject:
    print(sub)
