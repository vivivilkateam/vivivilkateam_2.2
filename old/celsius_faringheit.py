class Temperature:

    def __init__(self, celsius):
        self.__celsius = celsius
        self.__fahrenheit = celsius * 9/5 + 32

    def get_fahrenheit(self):
        return self.__fahrenheit


    def get_celsius(self):
        return self.__celsius

temp = Temperature(25)
print(temp.get_fahrenheit())
print(temp.get_celsius())