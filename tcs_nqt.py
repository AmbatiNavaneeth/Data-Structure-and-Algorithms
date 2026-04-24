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

1: Sweet Seventeen Given a maximum of four digits to the base 17(10 -> A, 11 -> B, 12 -> C, 16 -> G) as input, output its decimal val.
def base_17(s):
    map={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16}
    res=0
    power=0
    for ch in reversed(s):
        if ch.isdigit():
            val=int(ch)
        else:
            val=map[ch]
        res+=val*(17**power)
        power+=1
    return res   
print(base_17("23GF"))

Move zeros to end unsroted 
class Solution:
    def moveZeroes(self, nums: list[int]):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums
        
Move zeros to start unsroted 
class Solution:
    def moveZeroes(self, nums: list[int]):
        j=0
        for i in range(len(nums)):
            if nums[i]==0:
                  nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums

FOR SORT USE COUNT AND [0]*COUNT
                
DUTCH FLAG FOR 0 1 2
nums = [2,1,0,2,1,0,0,1,2,0]
low = 0
mid = 0
high = len(nums) - 1
while mid <= high:
    if nums[mid] == 0:
        nums[low], nums[mid] = nums[mid], nums[low]
        low += 1
        mid += 1
    elif nums[mid] == 1:
        mid += 1
    else:  # nums[mid] == 2
        nums[mid], nums[high] = nums[high], nums[mid]
        high -= 1
print(nums)

 ANOTHER METHOD CAN BE USE COUNT
 ANOTHER METHOD 
nums = [2,1,0,2,1,0,0,1,2,0]
# First pass → bring 0s to front
j = 0
for i in range(len(nums)):
    if nums[i] == 0:
        nums[i], nums[j] = nums[j], nums[i]
        j += 1
# Second pass → bring 2s to end
k = len(nums) - 1
for i in range(len(nums)-1, -1, -1):
    if nums[i] == 2:
        nums[i], nums[k] = nums[k], nums[i]
        k -= 1
print(nums)

Given an integer array Arr of size N the task is to find the countofelements whose value is greater than all of its prior elements. 
n=[9,8,7,6,5]
c=0
maxx=float('-inf')
for i in n:
    if i>maxx:
        c+=1
        maxx=i
    else:
        pass
print(c)

MULTIPLYING THE DIGITS
n=5244
if n>0:
    ans=1
    for ch in str(n):  abs(n)-to handle neg values
        ans*=int(ch)
    print(ans)




















