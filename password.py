
import pwinput
d={"ram":"1234","mohan":"3456","hari":"124"}
u=input("Enter your username\n")
for i in d.keys():
    if(u==i):
        # p=int(input("enter your password\n"))
        p=pwinput.pwinput("Enter your password")
        if(p==d[i]):
            print("you login")
            break
        elif(p!=d[i]):
            print("wrong password") 
    elif(u!=i):
        continue
    else:
        print("your username not found") 
        
