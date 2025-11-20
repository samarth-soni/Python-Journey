# if elif esle ladder ---
a = int(input("Enter your age: "))

if(a%2 == 0):   # If statement no: 1 (Independant)
    print("a is even")

else:
    print("a is odd")

if(a>18):      # if statement no: 2  (Independant)
    print("You can proceed")

elif(a<0):
    print("Are you Mad?")    
    print("Invalid Age")    


else:
    print("You can't proceed")