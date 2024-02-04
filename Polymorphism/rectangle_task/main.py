class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_left_x(self):
        if self.x1 > self.x2:
            return self.x2
        else:
            return self.x1

    def get_right_x(self):
        if self.x1 > self.x2:
            return self.x1
        else:
            return self.x2

    def get_top_y(self):
        if self.y1 > self.y2:
            return self.y1
        else:
            return self.y2

    def get_bottom_y(self):
        if self.y1 > self.y2:
            return self.y2
        else:
            return self.y1
        
    def overlaps(self, rect):
        if self.get_left_x() == rect.get_right_x() or self.get_left_x() < rect.get_right_x():
            if self.get_right_x() == rect.get_left_x() or self.get_right_x() > rect.get_left_x():
                if self.get_top_y() == rect.get_bottom_y() or self.get_top_y() > rect.get_bottom_y():
                    if self.get_bottom_y() == rect.get_top_y() or self.get_bottom_y() < rect.get_top_y():
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
        

