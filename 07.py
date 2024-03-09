class BoundingRectangle:
    def __init__(self):
        self.min_x = None
        self.max_x = None
        self.min_y = None
        self.max_y = None

    def add_point(self, x, y):
        if self.min_x is None or x < self.min_x:
            self.min_x = x
        if self.max_x is None or x > self.max_x:
            self.max_x = x
        if self.min_y is None or y < self.min_y:
            self.min_y = y
        if self.max_y is None or y > self.max_y:
            self.max_y = y

    def width(self):
        if self.min_x is None or self.max_x is None:
            return 0
        return self.max_x - self.min_x

    def height(self):
        if self.min_y is None or self.max_y is None:
            return 0
        return self.max_y - self.min_y

    def bottom_y(self):
        if self.min_y is None or self.max_y is None:
            return None
        return self.min_y

    def top_y(self):
        if self.min_y is None or self.max_y is None:
            return None
        return self.max_y

    def left_x(self):
        if self.min_x is None or self.max_x is None:
            return None
        return self.min_x

    def right_x(self):
        if self.min_x is None or self.max_x is None:
            return None
        return self.max_x


rect = BoundingRectangle()
rect.add_point(-1, -2)
rect.add_point(3, 4)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())