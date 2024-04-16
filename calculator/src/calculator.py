from .custom_ex import IncorrectInputError
import math 

class Calculator:
    def add(self, *args: float) -> float:  # type: ignore
        return sum(args)

    def sub(self, *args: float) -> float:
        try:
            result = args[0]  
            for num in args[1:]:
                result -= num  
            return result 
        except TypeError:
            raise IncorrectInputError('Wrong Input') 
        

    


    def multiply(self, *args: float):  # (1,2,3)
        try:
            result: float = 1
            for i in args:
                result *= i
            return result
        except TypeError:
            raise IncorrectInputError("Wrong Input")

    def division(self, *args: float):
        try:
            result: float = args[0]
            for i in args[1:]:
                result /= i
            return result
        except TypeError:
            raise IncorrectInputError("Wrong Input")
        
    
    def percentage(self, total: float, percentage: float) -> float:
        try:
            return (percentage / 100) * total
        except TypeError:
            raise IncorrectInputError('Wrong Input')
        
    def exponential(self, base: float, exponent: float) -> float:
        if base < 0:
            raise NegativeBaseError('Base cannot be negative')
        return math.pow(base, exponent) 