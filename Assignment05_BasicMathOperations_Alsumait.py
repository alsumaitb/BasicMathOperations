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
    
    
        
            
    
        
            
        
    
    