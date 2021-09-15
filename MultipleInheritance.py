class Calculation1:
    def Summation(self, a, b):
        return a + b


class Calculation2:
    def Multiplication(self, a, b):
        return a * b


class Derived(Calculation1, Calculation2):
    def Divide(self, a, b):
        return a / b


d = Derived()
print(d.Summation(5, 10))
print(d.Multiplication(5, 10))
print(d.Divide(5, 10))

