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

''' Instructions
    Inside the editor, complete the following steps:
    Create a class called Person
    Add an __init__ method that takes name and age as parameters
    Add a method called greet that prints "Hello, my name is " followed by the name
    Create an object p1 of the class with name "John" and age 36
    Call the greet method on p1     '''


class Person:
  def __init__(self ,name,age):
      self.name=name
      self.age=age
  def greet(self):
      print(f"hello my name is {self.name}")
p1=Person("john",36)
p1.greet()








  