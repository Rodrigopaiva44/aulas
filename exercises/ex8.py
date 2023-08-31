class TemperatureConverter:
    def __init__(self, temp):
        self.temp = temp

    def to_f(self):
        f = (9/5) * self.temp + 32
        return f
    
    def to_c(self):
        c = (5/9)*(self.temp - 32)
        return c
    
    @classmethod
    def get_temp(cls):
        choice = input('Do you want to convert temperature to Celsius or Fahrenheit (C/F)\n').upper()
        if choice == 'C':
            cel = float(input('Enter the Fahrenheit temperature: '))
            result = cls(cel).to_c()
            return result
        elif choice == 'F':
            far = float(input('Enter the Celsius temperature: '))
            result = cls(far).to_f()
            return result


def main():
    temp = TemperatureConverter.get_temp()
    print(temp)
    
main()
