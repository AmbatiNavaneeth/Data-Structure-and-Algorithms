# nums=[1,1,0,1,1,1]
# c=0
# m=float("-inf")
# for num in nums:
#     if num==1:
#         c+=1
#         m=max(m,c)
#     else:
#         c=0
# print(m)

# nums=[2,2,1,1,1,1,2,2]
# freq={}
# for num in nums:
#     freq[num]=freq.get(num,0)+1
# for i in freq:
#     if freq[i]>len(nums)//2:
#         print(i)
#     else:
#         pass

nums=[1,3,4,2,1,1]
freq={}
for num in nums:
     freq[num]=freq.get(num,0)+1
for key in freq:
    if freq[key]>1:
        print(key)
    else:
         None
