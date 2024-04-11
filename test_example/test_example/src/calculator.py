from .custom_ex import IncorrectInputError


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