#question1
def area(radius):
    print(3.14*radius*radius)
radius=int(input("enter raidus of circle"))
area(radius)

#question2
limit=int(input("enter upper limit"))
for n in range(2,limit+1):
    sum=0
    for divisor in range(1,n):
        if n!=divisor:
            sum+=divisor
        if sum==n:
            print(n)
    
#question4
a=int(input("enter base number"))
b=int(input("enter power number"))
print(a**b)

#question5
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

l1=[2,3,4,5]
context={}
for ele in l1:
    context[str(ele)]=fact(ele)
n=int(input("enter the number "))
fact(n)
print(context)

