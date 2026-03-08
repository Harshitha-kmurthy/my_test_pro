'''n=int(input("enter a num"))
arr1=[2,3,6,1,4,8]
res=[]
for i in range(len(arr1)-1):
    sum=arr1[i]+arr1[i+1]
    if sum==n:
       res.append(arr1[i])
       res.append(arr1[i+1])
    break   
print(res)     '''


'''n=int(input("enter a num"))
arr1=[2,3,6,1,4,8]
res=[]
for i in range(len(arr1)-1):
    for j in range(i+1,len(arr1) - 1):

        sum=arr1[i]+arr1[j]
        if sum==n:
           res.append(arr1[i])
           res.append(arr1[j])
    break
print(res)     

'''

n=int(input("enter a num"))
arr1=[2,3,6,1,4,8]
res=[]
i=0
while i<len(arr1)-1:
        sum=arr1[i]+arr1[i+1]
        if sum==n:
           res.append(arr1[i])
           res.append(arr1[i+1])
           break
        i+=1

print(res)     

