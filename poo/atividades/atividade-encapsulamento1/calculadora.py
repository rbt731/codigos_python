class Calculadora:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2
    
    def soma(self):
        return self.__num1 + self.__num2
    
    def subtrair(self):
        if self.__num1 < self.__num2:
            print("insira o primeiro valor maior que o segundo")
        else:
            print(f"A subtração deles é {self.__num1 - self.__num2}") 
    
    def multi(self):
        return self.__num1 * self.__num2

    def divi(self):
        if self.__num2 <= 0:
            print("a divisão não pode ocorrer com 0")
        else:
            return self.__num1 / self.__num2