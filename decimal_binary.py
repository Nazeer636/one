def decimal_binary(n):
    if n>1:
        decimal_binary(n//2)
        
    if n%2==0:
    
        print(0,end=" ")
    else:
        print(1,end=" ")

decimal_number=int(input("enter a decimal number"))
decimal_binary(decimal_number)
