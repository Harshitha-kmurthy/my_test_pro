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

'''

''' Instructions
    Inside the editor, complete the following steps:
    Create a class called Person
    Add an __init__ method that takes name and age as parameters
    Add a method called greet that prints "Hello, my name is " followed by the name
    Create an object p1 of the class with name "John" and age 36
    Call the greet method on p1     '''
'''

class Person:
  def __init__(self ,name,age):
      self.name=name
      self.age=age
  def greet(self):
      print(f"hello my name is {self.name}")
p1=Person("john",36)
p2=Person("riya",20)
p1.greet()
p2.greet()
'''

'''
#without __init__()
class Person1:
    def greet1(abc):
       print(f"hello my name is {abc.name1}")

p2=Person1()
p2.name1="xyz"
p2.age=47
p2.greet1()   '''

'''
# calling methods with self

class Party:
      def __init__(self,name):
           self.name=name

      def rec(self):
           return  "hello " + self.name

      def greet(self):
            message=self.rec()
            print(message + "  welcome to party")

p1=Party("friend")
p1.greet()                


menu = {'Pizza': 89.0, 'Pasta': 60.0, 'Burger': 79.0, 'Salad': 30.0}
total = 0.0
print("Menu:", menu)

while True:
        item = input("Order item (or 'exit'): ").title()
        
        if item == 'Exit':
            break

        if item in menu:
            try:
                qty = int(input(f"Quantity for {item}: "))
                if qty < 0:
                    print("Quantity cannot be negative.")
                    continue
                total += menu[item] * qty
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Item not found.")

    
print(f"Total: ₹{total:.2f}")



# super() = Function used in a child class to call methods from a parent 
# to extend the functionality of inherited methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cm^2")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")
        super().describe()

circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=6)
triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)

circle.describe()
#square.describe()
#triangle.describe()

''


class menu:
    def __init__(self):
        self.menu={'pizza':100,'burger':70,'pepsi':40,'combo':150}

    def menudisp(self):
        print("menu:",self.menu)

class order(menu):
    def __init__(self):
        super().__init__()
        self.total=0

    def caltotal(self):
      while True:
           item = input("Order item (or 'exit'): ")
           if item == 'exit': break
           if item in self.menu:
                 qty = int(input(f"Quantity for {item}: "))
                 self.total += self.menu[item] * qty
           else:
                print("Item not found.")      

    def totaldis(self):
        print(f"total amount:{self.total}")

o1=order()
o1.menudisp()
o1.caltotal()
o1.totaldis()    
                       

  
