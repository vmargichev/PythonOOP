import math
class Calculator:
    
    def __init__(self):
        self.__result = 0

    def add(self, a):
        self.__result += a
        return self.__result

    def subtract(self, a):
        self.__result -= a
        return self.__result

    def multiply(self, a):
        self.__result = self.__result * a
        return self.__result

    def divide(self, a):
        if a == 0:
            raise ValueError("Cannot divide by zero")
        self.__result = self.__result / a
        return self.__result

    def modulo(self, a):
        if a == 0:
            raise ValueError("Cannot divide by zero")
        self.__result = self.__result % a
        return self.__result

    def power(self, a):
        self.__result = math.pow(self.__result, a)
        return self.__result

    def square_root(self):
        self.__result = math.sqrt(self.__result)
        return self.__result 

    def clear(self):
        self.__result = 0

    def get_result(self):
        return self.__result