BILL DISCOUNT PROGRAM
n=int(input("enter bill:"))
if n<=1000:
    amount_pay=n-((n/100)*5)
    print(amount_pay)
elif 1001<=n<=5000:
    amount_pay=((n/100)*10)
    print(amount_pay)
elif n>=5001:
    amount_pay=((n/100)*15)
    print(amount_pay)
else:
    print("errror")
    
class Sol:
    def finalbill(self,n):
        if n<0:
            return "error"
        else:
            if n<=1000:
                amount_pay=n-((n/100)*5)
                return amount_pay
            elif 1001<=n<=5000:
                amount_pay=((n/100)*10)
                return amount_pay
            elif n>=5001:
                amount_pay=((n/100)*15)
                return amount_pay
            else:
                return None
obj=Sol()
n=-11
print(obj.finalbill(n))

PARKING CHARGES PROGRAM
n=int(input("enter:"))
if n<=2:
    print(n*100)
elif 2<n<=5:
    print(200+(n-2)*50)
elif n>5:
    print(350+(n-5)*20)
else:
    print("not chargable")

BALLOON CAPACITY
class Sol:
    def balloon_capacity(self,maxx,n):
        summ=0
        c=0
        for i in range(len(n)):
            if summ+n[i] <=maxx:
                summ+=n[i]
                c+=1
            else:
                break
        return c
obj=Sol()  
maxx=250
n=[40,39,94,10,20,58,76,45]
n.sort()
print(obj.balloon_capacity(maxx,n))
