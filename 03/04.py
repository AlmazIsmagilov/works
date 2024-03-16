class Date:
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def __sub__(self, other):
        res = (self.month - other.month) * 30 + (self.day - other.day)
        return res


jan5 = Date(1, 5)
jan1 = Date(1, 1)

print(jan5 - jan1)
print(jan1 - jan5)
print(jan1 - jan1)
print(jan5 - jan5)