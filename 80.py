# LAMDA FUNCTION 
#  syntax : name = lamda var : expression 
#  lamda function are anonymous functions meaning that a function without name .
#  as we already know the def keyword is used to define normal function in python. similarly lamda keyword is used to define  anonyms function in python
#  note: a lamda fn can take nay number of arguments but can only have one expression 

# def square(a):
#     return a*a

# a=int(input("Enter a :"))
# print("\nSquare :", square(a))

## Lmabda function 
square= lambda a :a*a
a=int(input("Enter a :"))
print("\nSquare :", square(a))