import numpy as np
import matplotlib.pyplot as plt
import re

# cities in our weather data
CITIES = [
    'BOSTON',
    'SEATTLE',
    'SAN DIEGO',
    'PHILADELPHIA',
    'PHOENIX',
    'LAS VEGAS',
    'CHARLOTTE',
    'DALLAS',
    'BALTIMORE',
    'SAN JUAN',
    'LOS ANGELES',
    'MIAMI',
    'NEW ORLEANS',
    'ALBUQUERQUE',
    'PORTLAND',
    'SAN FRANCISCO',
    'TAMPA',
    'NEW YORK',
    'DETROIT',
    'ST LOUIS',
    'CHICAGO'
]

INTERVAL_1 = list(range(1961, 2006))
INTERVAL_2 = list(range(2006, 2016))

"""
Begin helper code
"""


class Climate(object):
    """
    The collection of temperature records loaded from given csv file
    """

    def __init__(self, filename):
        """
        Initialize a Climate instance, which stores the temperature records
        loaded from a given csv file specified by filename.

        Args:
            filename: name of the csv file (str)
        """
        self.rawdata = {}

        f = open(filename, 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')

            date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))

            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature

        f.close()

    def get_yearly_temp(self, city, year):
        """
        Get the daily temperatures for the given year and city.

        Args:
            city: city name (str)
            year: the year to get the data for (int)

        Returns:
            a numpy 1-d array of daily temperatures for the specified year and
            city
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return np.array(temperatures)

    def get_daily_temp(self, city, month, day, year):
        """
        Get the daily temperature for the given city and time (year + date).

        Args:
            city: city name (str)
            month: the month to get the data for (int, where January = 1,
                December = 12)
            day: the day to get the data for (int, where 1st day of month = 1)
            year: the year to get the data for (int)

        Returns:
            a float of the daily temperature for the specified time (year +
            date) and city
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]


"""
End helper code
"""


# Problem 1
def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).
    Args:
        x: a list with length N, representing the x-coords of N sample points
        y: a list with length N, representing the y-coords of N sample points
        degs: a list of degrees of the fitting polynomial
    Returns:
        a list of numpy arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    models = []
    assert len(x) == len(y), f'generate_models(): len x and len y are not equal'
    assert type(x) == list, f'generate_models(): type of first argument {type(x)} is not a list'
    assert type(y) == list, f'generate_models(): type of first argument {type(y)} is not a list'
    assert type(degs) == list, f'generate_models(): type of first argument {type(degs)} is not a list'
    for degree in degs:
        assert type(degree) == int, f'generate_models(): type of first argument {type(degree)} is not a integer'
        x = np.array(x)
        y = np.array(y)
        models.append(np.polyfit(x, y, degree))
    return models


# Problem 2
def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    Args:
        y: list with length N, representing the y-coords of N sample points
        estimated: a list of values estimated by the regression model
    Returns: tuple

        a float for the R-squared error term
        a raound float SSE (sum(y-exper)**2)
    """
    assert len(y) == len(estimated), f"r_squared(y, estimated), len y != len estimated"
    sse = sum((a - b) ** 2 for a, b in zip(y, estimated))
    mean = np.mean(y)
    divider = sum((a - mean) ** 2 for a in y)
    return float(1 - (sse / divider)), round(float(sse), 2)


# Problem 3
def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-square for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        R-square of your model evaluated on the given data points
    Args:
        x: a list of length N, representing the x-coords of N sample points
        y: a list of length N, representing the y-coords of N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a numpy array storing the coefficients of
            a polynomial.
    Returns:
        best_model, r
    """
    r = 0
    assert len(x) == len(y), f'evaluate_models_on_training(x, y, models): len x != len y'
    for model in models:
        new_r = r_squared(y, np.polyval(model, x))[0]
        if new_r > r:
            best_model = model
            r = new_r
    # print(f'best_model = {best_model}, r = {r}')
    return best_model, r


def plottting_data(x, y, marker, ax, style='dotted'):
    """
    data from file
    """
    ax.set(xlabel='date', ylabel='temperature', title='global_climate_change')
    ax.plot(x, y, linestyle=style, c='b', label=f'measured data, mean = {round(np.mean(y), 1)}', marker=marker)
    return ax


def plotting_single_model(x, best_model, text_to_label, color,  ax):
    try:
        ax.plot(x, np.polyval(best_model, x), c=color, label=text_to_label)
    except NameError:
        print(f'evaluate_models_on_training(x, y, models) - best model not found')
    return ax


def model_statistic(model, x, y):
    """
    returns so,e statistic of using this model on who;le interval
    model - numpy.ndarray()
    x, y - list of values
    """
    assert len(x) == len(y)

    estimated_y = np.polyval(model, x)
    R2, SSE = r_squared(y, estimated_y)
    MSE = round(SSE / len(x), 3)
    mean = round(np.mean(y), 2)
    return round(R2, 2), round(SSE, 2), MSE, mean

def cross_validation(interval_1, interval_2):
    """
    try to make the best model for interval1 and fit it to interval2 and vice versa
    interval_1, interval_2 - slices of years
    return: None
    """
    degree = [0, 1]
    x1 = interval_1
    y1 = [raw_data.get_daily_temp('BOSTON', 1, 10, year) for year in x1]
    x2 = interval_2
    y2 = [raw_data.get_daily_temp('BOSTON', 1, 10, year) for year in x2]

    fig, ax = plt.subplots()
    ax = plottting_data(x1, y1, 'o', ax)
    ax = plottting_data(x2, y2, 's', ax, style='solid')

    best_model, r1 = evaluate_models_on_training(x1, y1, generate_models(x1, y1, degree))
    estimated = np.polyval(best_model, x2)
    r2, sse = r_squared(y2, estimated)
    statistic = model_statistic(best_model, x1+x2, y1+y2)
    print(f'interval1 - training, interval2 - test. model = {best_model}, training_r = {round(r1, 3)}, '
          f'test_r = {round(r2, 3)}, difference = {round(abs(r1 - r2), 3)}')
    text_to_label = f'interval 1 - training, interval2 - testing\nr1={round(r1, 3)}, r2={round(r2, 3)}, ' \
                    f'difference={round(abs(r1 - r2), 3)}\nfor whole intervals:\n' \
                    f'R2={statistic[0]}, SSE={statistic[1]}, MSE={statistic[2]}, mean={statistic[3]}'
    color = 'r'
    ax = plotting_single_model(x1 + x2, best_model, text_to_label, color, ax)

    best_model, r2 = evaluate_models_on_training(x2, y2, generate_models(x2, y2, degree))
    estimated = np.polyval(best_model, x1)
    r1 = r_squared(y1, estimated)[0]
    print(f'interval1 - training, interval2 - test. model = {best_model}, training_r = {r2}, test_r = {r1}, '
          f'difference = {abs(r1 - r2)}')
    statistic = model_statistic(best_model, x1 + x2, y1 + y2)
    text_to_label = f'interval2 - training, interval1- testing\nr1={round(r1, 3)}, r2={round(r2, 3)}, ' \
                    f'difference={round(abs(r1 - r2), 3)}\nfor whole intervals:\n' \
                    f'R2={statistic[0]}, SSE={statistic[1]}, MSE={statistic[2]}, mean={statistic[3]}\n'
    color = 'g'
    ax = plotting_single_model(x1 + x2, best_model, text_to_label, color, ax)

    ax.axhline(statistic[3])
    ax.grid()
    ax.legend()
    plt.show()


if __name__ == '__main__':
    ### Begining of program
    raw_data = Climate('data.csv')

    # Problem 3
    y = []
    x = INTERVAL_1
    for year in INTERVAL_1:
        y.append(raw_data.get_daily_temp('BOSTON', 1, 10, year))
    models = generate_models(x, y, [1])
    best_model, r = evaluate_models_on_training(x, y, models)

    cross_validation(INTERVAL_1, INTERVAL_2)
"""
    # Problem 4: FILL IN MISSING CODE TO GENERATE y VALUES
    x1 = INTERVAL_1
    x2 = INTERVAL_2
    y = []
    # MISSING LINES
    
    models = generate_models(x, y, [1])
    evaluate_models_on_training(x, y, models)
"""
