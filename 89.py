# without filter

# def fun(numbers):
#     num=[1,2,32,4,50]
#     for val in numbers:
#         if val in num:
#             print(val)
    
# sequence=[1,2,3,4,5,6,7,8,9,10]
# fun(sequence)


#  with filter 
def fun(val):
    num=[1,2,32,4,50]
    # for val in numbers:
    if val in num:
        return True
    else:
        return False
    
sequence=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(fun,sequence)))