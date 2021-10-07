#fibonacci series task
n=int(input("enter no of terms"))
n1,n2=0,1
count=0
if n<=0:
    print("enter the positive number")
elif n==1:
    print("sequence:",n)
    print(n1)
else:
    print("fibinocci series:")
    while count<=n:
        print(n1)
        sum=n1+n2
        n1=n2
        n2=sum
        count+=1
