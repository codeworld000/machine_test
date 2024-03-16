row=int(input("enter the row"))
col=int(input("enter the colum"))
for i in range(row):
    if i == 0:
        for j in range(col):
            if j % 2==0:
                print(" ___",end=" ")
            else: 
                print("   ",end="")
   
    if col % 2 == 0:
        if i==0:
            print() 
            for l in range(col):
            
                if l==0 or  l % 2 == 0:
                    print("/  ",end=" ") 
            
                else:
                    print("\\___",end="")
                
            print()
            for h in range(col+1):
                    if h==0 or h %2 ==0 or h==col:
                        print("\\",end="")
                    else:
                         print("___/",end="   ")
        else:
        
            print() 
            for l in range(col+1):
            
                if l==0 or  l % 2 == 0 :
                    print("/  ",end=" ") 
                elif l==col:
                    print("\\",end="")
                else:
                    print("\\___",end="")
                
            print()
            for h in range(col+1):
                    if h==0 or h %2 ==0 or h==col:
                        print("\\",end="")
                    else:
                         print("___/",end="   ")
       
            
    else:
        print()
        for l in range(col+1):
            if l==0 or l % 2 == 0:
                print("/  ",end=" ") 
            elif l==col:
                print("\\",end="")
            else:
                print("\\___",end="")
            
        print()
        for h in range(col):
                if h==0 or h%2==0:
                  print("\___/",end="")
                else:
                    print("   ",end="")
        
print()
