"""

Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.



"""

a = sorted(list(map(str,input())))
lower =""
upper =""
numericodd =""
numericeven=""

for i in a: 
    if i.islower():
        lower+=i
    if i.isupper():
        upper+=i
    if i.isnumeric():
        if int(i)%2==1:
            numericodd+=i
        else:
            numericeven+=i
              

print(lower+upper+numericodd+numericeven)
    
        
        
