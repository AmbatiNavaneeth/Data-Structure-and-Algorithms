Max odd count 
nums="12354"  
c=0
max_len=0
for i in range(len(nums)):
    if int(nums[i])%2!= 0:
        c+=1
        max_len=max(max_len,c)
    else:
        c=0
print(max_len)

✅ Code for sum of digits:
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

arr=[10,20,30,20,10,30]
freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
ans=[]
for key in freq:
    if freq[key]>=2:
        ans.append(key)
print(ans)

second smallest 
nums=[1,3,4,5,6]
s=float("inf")
ss=float("inf")
for num in nums:
    if num<s:
        ss=s
        s=num
    elif num<ss and num!=s:
        ss=num
if ss==float("inf"):
    print(-1)
else:
    print(ss)
