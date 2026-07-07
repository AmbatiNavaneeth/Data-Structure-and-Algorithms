sorting algorithm:
	
bubble sort:
input: [54, 26, 93, 17, 77, 31, 44, 55, 20]
Output:
54 26 93 17 77 31 44 55 20
26 54 93 17 77 31 44 55 20
26 54 17 93 77 31 44 55 20
26 54 17 77 93 31 44 55 20
26 54 17 77 31 93 44 55 20
26 54 17 77 31 44 93 55 20
26 54 17 77 31 44 55 93 20
26 54 17 77 31 44 55 20 93
26 17 54 77 31 44 55 20 93
26 17 54 31 77 44 55 20 93
26 17 54 31 44 77 55 20 93
26 17 54 31 44 55 77 20 93
26 17 54 31 44 55 20 77 93
17 26 54 31 44 55 20 77 93
17 26 31 54 44 55 20 77 93
17 26 31 44 54 55 20 77 93
17 26 31 44 54 20 55 77 93
17 26 31 44 20 54 55 77 93
17 26 31 20 44 54 55 77 93
17 26 20 31 44 54 55 77 93

code : 
    l= [54, 26, 93, 17, 77, 31, 44, 55, 20]
    n-len(l)
    for i in range(n):
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    print(l)
 

selection sort:

input: [8, 7, 6, 5, 4, 3, 2, 1, 0]
Output:
[8, 7, 6, 5, 4, 3, 2, 1, 0]
[0, 7, 6, 5, 4, 3, 2, 1, 8]
[0, 1, 6, 5, 4, 3, 2, 7, 8]
[0, 1, 2, 5, 4, 3, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8]

code : 
l = [8, 7, 6, 5, 4, 3, 2, 1, 0]
for i in range(len(l)-1):
    minn = i
    for j in range(i+1,len(l)):
        if l[j] < l[minn]:
            minn = j 
    l[i], l[minn] = l[minn], l[i]
print(l)


insertion sort:

Input : [3, 4, 2, 10, 12, 1, 5, 6, 8]
Output:
[3, 4, 2, 10, 12, 1, 5, 6, 8]
[3, 3, 4, 10, 12, 1, 5, 6, 8]
[2, 3, 4, 10, 12, 1, 5, 6, 8]
[2, 3, 4, 10, 12, 1, 5, 6, 8]
[2, 2, 3, 4, 10, 12, 5, 6, 8]
[1, 2, 3, 4, 10, 10, 12, 6, 8]
[1, 2, 3, 4, 5, 10, 10, 12, 8]
[1, 2, 3, 4, 5, 6, 10, 10, 12]
[1, 2, 3, 4, 5, 6, 8, 10, 12]

code:
l = [3, 4, 2, 10, 12, 1, 5, 6, 8]
for i in range(1,len(l)):
    k = l[i]
    j=i-1
    while j>=0 and k <l[j]:
        l[j+1]=l[j]
        j-=1

    l[j+1]=k 
print(l)


quick sort:
Ex: 
input : l = [9,8,7,6,5,4,3,2,1,0]
left:
----    + 
middle:
[0]
[1]
[2]
[3]
[4]
[5]
[6]
[7]
[8]      +

right:
[9, 8, 7, 6, 5, 4, 3, 2, 1]
[9, 8, 7, 6, 5, 4, 3, 2]
[9, 8, 7, 6, 5, 4, 3]
[9, 8, 7, 6, 5, 4]
[9, 8, 7, 6, 5]
[9, 8, 7, 6]
[9, 8, 7]
[9, 8]
[9]

output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

code:
def quick_sort(l):
    if len(l)<=1: 
		return l 
    pivot = l[-1]    #l[len(l)//2]  #l[0]
    left = []
    for i in l:
        if i <pivot: left.append(i)
    middle=[]
    for i in l:
        if i==pivot: middle.append(i)
    right=[]
    for i in l:
        if i > pivot: right.append(i)
    return quick_sort(left)+middle+quick_sort(right)
        
l = [99, 55, 0, 43, 2]
res = quick_sort(l)
print(res)


merge sort:

input:
l= [5, 4, 3, 2, 1, 0, 10 ]
Output:
      left [5, 4, 3]                                                        right [2, 1, 0, 10]
                               (sorted [0, 1, 2, 3, 4, 5, 10])

left [5]       right [4, 3]                                        left [2, 1]             right [0, 10]  

   (sorted [3, 4, 5])                                                     (sorted [0, 1, 2, 10])                                            

             left [4]   right [3]                               left [2]   right [1]       left [0]     right [10] 

               (sorted [3, 4])                                     (sorted [1, 2])            (sorted [0, 10])


merge sort code:
def merge(left,right):
    m_l = []
    i=j=0 
    while i<len(left)  and j<len(right):
        if left[i]<right[j]:
            m_l.append(left[i])
            i+=1 
        else:
            m_l.append(right[j])
            j+=1 
    m_l+=left[i:]
    m_l+=right[j:]
    return m_l

def merge_sort(l):
    if len(l)<=1: return l 
    mid = len(l)//2 
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    return merge(left,right)
    
l= [5, 4, 3, 2, 1, 0, 10 ]
print(merge_sort(l))
