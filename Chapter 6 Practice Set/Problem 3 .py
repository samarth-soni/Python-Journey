# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

a = input("Enter the mail Keywords: ")
s2 = "Make a lot of money"
s3 = "buy now"
s4 = "subscribe this"
s5 = "click this"

if(s2 in a or s3 in a or s4 in a or s5 in a ):
    print("this is spam")

else:
    print("All Ok")


