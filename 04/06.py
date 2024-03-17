class Transport:
    def move(self):
        pass


class WaterTransport(Transport):
    def swim(self):
        pass


class AirTransport(Transport):
    def fly(self):
        pass


class Aviation(AirTransport):
    def fly_fast(self):
        pass


class Airship(AirTransport):
    def float_slowly(self):
        pass


class GroundTransport(Transport):
    def move_on_ground(self):
        pass


class RailTransport(GroundTransport):
    def rails(self):
        pass


class RoadTransport(GroundTransport):
    def roads(self):
        pass


class BicycleTransport(GroundTransport):
    def pedal(self):
        pass


class AnimalPoweredTransport(GroundTransport):
    def be_drawn_by_animals(self):
        pass


class SpaceTransport(Transport):
    def atmosphere(self):
        pass


class Rocket(SpaceTransport):
    def space(self):
        pass