from random import choice


class Drunk:
    def __init__(self, name):
        self.name = str(name)

    def __str__(self):
        return self.name

    def moving(self):
        pass


class Normal_Drunk(Drunk):

    def __init__(self, name):
        Drunk.__init__(self, name)

    def moving(self):
        return choice([(-1, 0), (1, 0), (0, 1), (0, -1)])


class Cold_Drunk(Drunk):
    def __init__(self, name):
        Drunk.__init__(self, name)

    def moving(self):
        return choice([(-1, 0), (1, 0), (0, 0.9), (0, -1.1)])


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_location(self):
        return self.x, self.y

    def set_location(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, other):
        """
        returns distance between current location and other location
        """
        assert isinstance(other, Location), f'Location.get_distance():{other} is not Location instance'
        return ((other.get_location()[0] - self.x) ** 2 + (other.get_location()[1] - self.y) ** 2) ** 0.5

    def location_after_move(self, dif_x, dif_y):
        """
        dif_x: float - how to change x coordinate
        dif_y: float - how to change y coordinate
        returns new instance of Location class with new coordinates
        """
        return Location(self.x + dif_x, self.y + dif_y)


class Field:
    def __init__(self):

        self.field = {}

    def add_drunk(self, d, l=Location(0, 0)):
        """
        d: Drunk
        l: start Location 0,0 - by default
        """
        assert isinstance(d, Drunk), f'Field.__init__(): {d} is not instance of Drunk class'
        assert isinstance(l, Location), f'Field.__init__(): {l} is not instance of Location class'
        if d in self.field.keys():
            raise ValueError('This Drunk already in dictionary')
        else:
            self.field[d] = l

    def move_drunk(self, d):
        """
        changes drunk positions (as value of dictionary field[d])
        uses new location function from Location class
        uses dif_x, dif_y from function moving() of Drunk subclases - Cold_drunk, Normal_Drunk
        """
        assert isinstance(d, Drunk), f'Filed.move_drunk(): {d} not instance of Drunk class'
        assert d in self.field.keys(), f'Filed.move_drunk(): {d} not in fileld dictionary keys'
        # new  location for drunk d after movement
        self.field[d] = self.field[d].location_after_move(*d.moving())

    def get_distance(self, d, start):
        """
        start: Location - instance of Location to be start
        d: Drunk
        """
        assert isinstance(d, Drunk)
        assert d in self.field.keys()
        assert isinstance(start, Location)
        return self.field[d].get_distance(start)




def show_distance_normal_drunk(dist, count):
    start = Location(0, 0)

    for distance in dist:
        print(f'distance = {distance}')
        answer = []
        for i in range(count):
            f = Field()
            man = Normal_Drunk('Homer')
            f.add_drunk(man)
            for i in range(distance):
                f.move_drunk(man)
            answer.append(f.get_distance(man, start))
        answer.sort()
        print(f'min= {answer[0]},\t max= {answer[-1]},\t avg= {sum(answer)/len(answer)}')


def show_distance_cold_drunk(dist, count):
    start = Location(0, 0)

    for distance in dist:
        print(f'distance = {distance}')
        answer = []
        for i in range(count):
            f = Field()
            man = Cold_Drunk('Homer')
            f.add_drunk(man)
            for i in range(distance):
                f.move_drunk(man)
            answer.append(f.get_distance(man, start))
        answer.sort()
        print(f'min= {answer[0]},\t max= {answer[-1]},\t avg= {sum(answer)/len(answer)}')




trip_dist = [5, 100, 1000, 10000]
trip_count = 10000
show_distance_normal_drunk(trip_dist, trip_count)
show_distance_cold_drunk(trip_dist, trip_count)