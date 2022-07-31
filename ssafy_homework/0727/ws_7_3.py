class Calculator():
    def add(self, first, second):
        result = first + second
        return result

    def substract(self, first, second):
        result = first - second
        return result

    def multuply(self, first, second):
        result = first * second
        return result

    def divide(self, first, second):
        if second != 0:
            result = round(first / second, 2)
            return result
        elif second == 0:
            return '0으로 나눌 수 없습니다.'

c = Calculator()
print(c.add(1, 2))
print(c.substract(2, 1))
print(c.multuply(3, 4))
print(c.divide(4, 0))