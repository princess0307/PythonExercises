
def sum(number):
    sum=0
    while(number>0):
        rem=number%10
        sum=sum+rem
        number=number/10
    return sum
a=int(raw_input("enter the number\n"))
ans=sum(a)
print ans
     
        
