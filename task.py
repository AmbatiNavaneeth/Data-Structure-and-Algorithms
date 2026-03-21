✅Max odd count 
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

✅arr=[10,20,30,20,10,30]
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

✅second smallest 
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

✅Check if All Elements Are Same
n=[1]
if len(n)<2:
    print(False)
i=0
j=len(n)-1
while i<j:
    if n[i]!=n[j]:
        print(False)
        break
    elif n[i]==n[j]:
        i+=1
        j-=1
else:
    print(True)


✅Find Frequency of All Elements
n=[1,2,3,4]
freq={}
for num in n:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
print(freq)

✅Flatten a Nested List
n=[[1,2],[3,4]]
ans=[]
for i in n:
    for j in i:
        ans.append(j)
print(ans)

✅Split a List into Even and Odd Lists
n=[1,2,3,4]
even=[]
odd=[]
for num in n:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print(even)
print(odd)

✅pairs which are equal to sum
n=[1,2,3,4,5,3]
n.sort()
k=6
i=0
j=len(n)-1
add=[]
while i<j:
    if n[i]+n[j]<k:
        i+=1
    elif n[i]+n[j]>k:
        j-=1
    else:
        add.append((n[i],n[j]))
        i+=1
        j-=1
print(add)
      without sorting  
seen=set()
res=[]
for num in n:
    if k-num in seen:
        res.append((k-num,num))
    seen.add(num)
print(res)


✅remove odds and evens
n=[1,2,3,4,5,6]
for num in n:
    if num%2!=0:
        n.remove(num)
    else:
        pass
print(n)
m=[1,2,3,4,5,6]
for num in m:
    if num%2==0:
        m.remove(num)
    else:
        pass
print(m)

✅Check prime numbers and indices in a list
def check_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5) + 1):
        if n%i==0:
            return False
    return True
        
nums=[1,2,3,4,5,6]
for i in range(len(nums)):
    if check_prime(nums[i]):
        print(nums[i],end=" ")

✅Return duplicates
nums=[1,2,2,3,4,4,5]
seen=[]
ans=[]
for num in nums:
    if num in seen:
        ans.append(num)
    else:
        seen.append(num)
print(ans)
 using dictionary
freq={}
for num in nums:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
ans=[]
for num in freq:
    if freq[num]>1:
        ans.append(num)
    else:
        pass
print(ans)
