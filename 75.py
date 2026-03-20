# 

stmt = input("Enter any statement: ")

def count_vowels(s):
    vowels = "aeiouAEIOU"
    cnt = 0
    for ch in s:
        if ch in vowels:
            cnt += 1
    return cnt

print("Number of vowels:", count_vowels(stmt))

