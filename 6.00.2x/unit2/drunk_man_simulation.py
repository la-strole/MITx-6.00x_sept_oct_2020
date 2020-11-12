from random import choice
import matplotlib
import matplotlib.pyplot as plt


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

    def get_location(self, d):
        """
        return x,y: tuple - current location of d: Drunk
        """
        return self.field[d].get_location()

class styleIterator:
    def __init__(self, styles: list):
        self.index = 0
        self.styles = styles

    def next_style(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result


def show_distance_drunk(dist: list, count: int, type_of_drunk):
    """
    dist: list - how many random steps make
    count: int - how many times repeat each dist trip
    type_of_drunk - Normal or Cold Drunk
    return: avg dist from (0.0) for last trip dist[-1]
    """
    start = Location(0, 0)

    for distance in dist:
        #print(f'distance = {distance}')
        answer = []
        for i in range(count):
            f = Field()
            man = type_of_drunk('Homer')
            f.add_drunk(man)
            for i in range(distance):
                f.move_drunk(man)
            answer.append(f.get_distance(man, start))
        answer.sort()
        #print(f'min= {answer[0]},\t max= {answer[-1]},\t avg= {sum(answer) / len(answer)}')
    return int(sum(answer) / len(answer))


trip_dist = [5, 100, 1000, 10000]
trip_count = 1000


# show_distance_drunk(trip_dist, trip_count, Normal_Drunk)
# show_distance_drunk(trip_dist, trip_count, Cold_Drunk)


def x_geomerty_progress(max_number_steps):
    """
    returns list of numbers from 1 to max_number
    """
    x = 1
    result = [1]
    while x < max_number_steps:
        result.append(int(x * 1.3))
        x *= 1.3
    return sorted(list(set(result)))


def get_x_y_coordinates(max_number_steps=10000, currancy_count=100, type_of_drunk=Normal_Drunk):
    x_list = x_geomerty_progress(max_number_steps)
    y_list = []
    for x in x_list:
        y_list.append(show_distance_drunk([x], currancy_count, type_of_drunk))
        print(f'{int((len(y_list)/len(x_list)) * 100)} percent complete')
    return x_list, y_list


def plot_graph_1():
    # data for plotting
    x1, y1 = get_x_y_coordinates()

    fig, ax = plt.subplots()
    ax.plot(x1, y1, linestyle='solid', label='Normal Drunk walk')
    ax.set(xlabel='number of steps', ylabel='avg distance from the center', title='Normal/Cold Drunk walk simulation')
    x2, y2 = get_x_y_coordinates(type_of_drunk=Cold_Drunk)
    ax.plot(x2, y2, linestyle='dotted', label='Cold Drunk walk')
    ax.grid()
    ax.legend()
    plt.show()


def plot_graph_2():
    # take data
    number_of_steps = 10000
    count = 1000
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    man1 = Normal_Drunk('Homer')
    man2 = Cold_Drunk('Nata')
    for item in range(count):
        f = Field()
        f.add_drunk(man1)
        f.add_drunk(man2)
        for i in range(number_of_steps):
            f.move_drunk(man1)
            f.move_drunk(man2)
        x1.append(f.get_location(man1)[0])
        y1.append(f.get_location(man1)[1])
        x2.append(f.get_location(man2)[0])
        y2.append(f.get_location(man2)[1])
        print(f'{int(len(x1)/count*100)} percent complete')

    minimum = min(x1+x2+y1+y2)
    maximum = max(x1+x2+y1+y2)


    fig, ax = plt.subplots()
    ax.set(xlabel='x', ylabel='y', title=f'Normal/Cold drunk end positions after {number_of_steps} moving')
    ax.set_xlim(minimum, maximum)
    ax.set_ylim(minimum, maximum)
    ax.scatter(x1, y1, c='m', s=2, label='Normal Drunk', marker=r',')
    ax.scatter(x2, y2, c='c', s=2, label='Cold Drunk')
    ax.set_box_aspect(1)
    ax.grid()
    ax.legend()
    plt.show()

# plot_graph_1()
plot_graph_2()