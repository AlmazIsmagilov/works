class BigBell:
    def __init__(self):
        self.sounds = 0

    def sound(self):
        if self.sounds % 2 == 0:
            print("ding")
            self.sounds += 1
        else:
            print("dong")
            self.sounds += 1


bell = BigBell()
bell.sound()
bell.sound()
bell.sound()