def Power(n):
    if(n==0):
        return False
    else:
        while(n!=1):
            if(n%2!=0):
                return False
            n=n/2
    return True
                
n=int(input())
if(Power(n)):
    print("yes")
else:
    print("no")
