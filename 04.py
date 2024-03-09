class OddEvenSeparator:
    def __init__(self):
        self.number_even = []
        self.number_odd = []

    def add_number(self, number):
        if number % 2 == 0:
            self.number_even.append(number)
        else:
            self.number_odd.append(number)

    def even(self):
        return self.number_even

    def odd(self):
        return self.number_odd


separator = OddEvenSeparator()
separator.add_number(1)
separator.add_number(5)
separator.add_number(6)
separator.add_number(8)
separator.add_number(3)
print(' '.join(map(str, separator.even())))
print(' '.join(map(str, separator.odd())))