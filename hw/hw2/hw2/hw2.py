text=input("Enter a string: ")

letters=0
digits=0
spaces=0
upper=0
lower=0
length=len(text)

for char in text:  
    if char == ' ':  
        spaces+=1
    elif char.isdigit():  
        digits+=1
    elif char.isalpha():  
        letters+=1
        if char.isupper():
            upper+=1
        elif char.islower():
            lower+=1



print("number of characters:", length)
print("Number of letters:", letters)
print("Number of digits:", digits)
print("Number of spaces:", spaces)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)