## MAP FUNCTION
#  in python map function is used when we want to apply same fynction repeatedly on different set of elements 


def square(y):
    return y*y
# num=2
# print(square(num))

num=[1,2,3,4,5]
# for i in num:
#     print(square(i))
    
##NOTES

result= map(square,num)
# print(result)
print(list(result))

###
'''
1.Map is better option of loops 
2.Map is faster then loops
3.Map returns result as a list
'''
