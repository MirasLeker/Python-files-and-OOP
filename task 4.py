class calculation: 
    def __init__(self, length, breadth): #initializing by constructor 
        self.length = length 
        self.breadth = breadth

    def display(self): 
        print ("Length:", self.length)
        print ("Breadth:", self.breadth)
    def area(self):
        return(self.length*self.breadth) #return value to perimeter
    def perimeter(self):
        return(2*self.length + 2*self.breadth) #return value to area

class Rectangle(calculation): #Rectangle inherits calculation
    pass   #in order to pass the class
l = int(input("Enter the length: ")) #giving the value
b = int(input("Enter the breadth: ")) #giving the value

r1 = calculation(l, b)
print("Rectangle object details are: ")

r1.display()
print("Area of Rectangle is: ", r1.area())
print("Perimeter of Rectangle is: ", r1.perimeter())
    
