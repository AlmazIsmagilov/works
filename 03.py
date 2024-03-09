class Balance:
    def __init__(self):
        self.add_right_count = 0
        self.add_left_count = 0

    def add_right(self, weight):
        self.add_right_count += weight

    def add_left(self, weight):
        self.add_left_count += weight

    def result(self):
        if self.add_right_count == self.add_left_count:
            return "="
        elif self.add_right_count > self.add_left_count:
            return "R"
        else:
            return "L"


balance = Balance()
balance.add_right(10)
balance.add_left(5)
balance.add_left(5)
print(balance.result())
balance.add_left(1)
print(balance.result())