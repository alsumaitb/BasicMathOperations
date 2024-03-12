# Assignment 05, BasicMathOperations

import math
class BasicMathOperations:
    
    def greetUser(self, firstname, lastname):
        print(f"Hello {firstname} {lastname} !")
        
    def addNumbers(self):
        user_prompt_1 = int(input("Enter first number: "))
        user_prompt_2 = int(input("Enter second number: "))
        
        return user_prompt_1 + user_prompt_2
    
    def performOperation(self, num1, num2, operator):
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1*num2
        elif operator == "/":
            return num1/num2
        else:
            print("Invalid operator")
            
    def squareNumber(self, num):
        return num**2 
    
    def factorial(self,num):
        result = 1
        for integer in range(num,1,-1):
            result = integer*result
        return result
    
    def counting(self):
        start = int(input("Enter first number: "))
        end = int(input("Enter second number: "))
        for i in range(start, end+1):
            print(i)
            
    def calculateSquare(self, num):
        return num**2 
    
    def calculateHypotenuse(self, a, b):
        c = math.sqrt(self.calculateSquare(a) + self.calculateSquare(b))
        return c
    
    def areaofRectangle(self, width, height):
       return height*width
   
    def powerofNumber(self, base, exponent):
        return base**exponent
    
    def typeofArgument(self, argument):
        return type(argument)
    
def main():
  
    bmo = BasicMathOperations()
    while True:
    
        print("1. Greet User\n2. Add number\n3. Perform Operation\n4. Square number\n5. Factorial\n6. Counting\n7. Calculate Hypotenuse\n8. Rectangle Area\n9. Power of Number\n10. Type of Argument\n11. Nothing")
        user_choice = input("Pick the task number you would like to execute: ")
       
        if user_choice == "1":
            firstname = input("Enter first name: ")
            lastname = input("Enter last name: ")
            bmo.greetUser(firstname, lastname)
       
        elif user_choice == "2":
            bmo.addNumbers()
        
        elif user_choice == "3":
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            operator = input("Enter math operator(+,-,*,/): ")
            bmo.performOperation(num1, num2, operator)
       
        elif user_choice == "4":
            num = int(input("Enter number: "))
            bmo.squareNumber(num)
        
        elif user_choice == "5":
            num = int(input("Enter number: "))
            bmo.factorial(num)
       
        elif user_choice == "6":
            bmo.counting()
        
        elif user_choice == "7":
            a = int(input("Enter a of right triangle: "))
            b = int(input("Enter b of right triangle: "))
            bmo.calculateHypotenuse(a, b)
        
        elif user_choice == "8":
            width = int(input("Enter width of rectangle: "))
            height = int(input("Enter height of rectangle: "))
            bmo.areaofRectangle(width, height)
        
        elif user_choice == "9":
            base = int(input("Enter base: "))
            exponent = int(input("Enter exponent: "))
            bmo.powerofNumber(base, exponent)
        
        elif user_choice == "10":
            argument = input("Enter any data type: ")
            bmo.typeofArgument(argument)
       
        elif user_choice == "11":
            break
       
        else:
            print("Invalid choice")
            
        
   
        
        
            
    
        
            
        
    
    