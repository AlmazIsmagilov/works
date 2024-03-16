class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        return sum(coefficients[i] * x**i for i, coefficient in enumerate(self.coefficients))

    def __add__(self, other):
        return Polynomial(self.coefficients + other.coefficients)