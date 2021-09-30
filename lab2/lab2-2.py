import math


class Rational:
    def __init__(self, numerator=1, denominator=2):
        if isinstance(numerator, int) and isinstance(denominator, int):
            self.__numerator = numerator
            if denominator:
                self.__denominator = denominator
        if math.gcd(self.__numerator, self.__denominator) != 1:
            divisor = math.gcd(self.__numerator, self.__denominator)
            self.__numerator = int(self.__numerator / divisor)
            self.__denominator = int(self.__denominator / divisor)

    def demonstrate_fraction(self):
        print(str(self.__numerator) + '/' + str(self.__denominator))

    def demonstrate_float(self):
        print(self.__numerator / self.__denominator)


obj1 = Rational(6, 8)
obj1.demonstrate_fraction()
obj1.demonstrate_float()
obj2 = Rational()
obj2.demonstrate_fraction()
obj2.demonstrate_float()



