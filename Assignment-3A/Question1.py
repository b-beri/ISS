n = int(input("Enter an even number(>2): "))
if(n % 2 != 0 or n < 2):
    print("Bad Entry....")
else:
    for i in range(2, n+1, 2):
        #Variation 1 - LOOPING
        for j in range(i//2):
            print(" ", end="")
        for k in range(n-i+2):
            print("*", end="")
        print()
    
    #Variation 2 - STRING MULTIPLICATION
    for i in range(n, 0, -2):
        space = " "*(i//2)
        star = "*"*(n-i+2)
        print(space,star,sep="")
