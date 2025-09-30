password=input("Enter a password:")
lower=False
upper=False
digit=False
spcl_char=False
for ch in password:
    if ch.islower():
        lower=True        
    elif ch.isupper():
        upper=True
    elif ch.isdigit():
        digit=True
    elif ch in "@#$%&*": 
        spcl_char=True
if all([len(password)>=8,upper,lower,digit,spcl_char]):
    print("Strong Password")
else:
    print("Weak Password")