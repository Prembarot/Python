#  write a login module and pass username and pssword if username and password matches it should print welcome admin and success=true and if it fails it should return invalid credential and success= false

# a="admin"
# b="1234"
# def login_module(username,password):
#     if a==username and b==password:
#         print("Login succesfull")
#         print("Username :",a)
#         print("Password :",b)
#         return ("success" :True)
#     else:
#         return ("success":False,"message":"invalid credentials")
# x=str(input("Enter username:"))
# y=str(input("Enter passweod:"))
# login_module(x,y)
        
def login(username,password):
    if(username=="admin" and password=="1234"):
        print("welcome admin")
        return {"success" :True}
    else:
        return {"success":False,"message":"invalid credentials"}

username=input("enter the username :")
password=input("enter the password :")
x=login(username,password)
print(x)

