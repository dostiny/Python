a = 3
b = 6
c = -5

formula1 = (-b + ((b ** 2 - 4 * a * c ) ** 1/2)) / (2 * a)
formula2 = (-b - ((b ** 2 - 4 * a * c ) ** 1/2)) / (2 * a)

formula1 = round(formula1, 4)
formula2 = round(formula2, 4)

formula = (formula1, formula2)
print(formula)