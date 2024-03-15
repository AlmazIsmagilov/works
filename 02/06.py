class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_w(self):
        return self.w

    def get_h(self):
        return self.h

    def intersection(self, other):
        left_x = max(self.x, other.x)
        bottom_y = max(self.y, other.y)
        right_x = min(self.x + self.w, other.x + other.w)
        top_y = min(self.y + self.h, other.y + other.h)

        if right_x <= left_x or top_y <= bottom_y:
            return None

        return Rectangle(left_x, bottom_y, right_x - left_x, top_y - bottom_y)


rect1 = Rectangle(0, 0, 10, 10)
rect2 = Rectangle(10, 0, 10, 10)
rect3 = rect1.intersection(rect2)

if rect3 is None:
    print('No intersection')
else:
    print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())