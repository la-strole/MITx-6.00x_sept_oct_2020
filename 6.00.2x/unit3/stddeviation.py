import random
import matplotlib.pyplot as plt
import scipy.integrate
import math


# calculate standard deviation
def stddev(L: list):
    assert len(L) > 0
    new_L = L.copy()
    mean = sum(new_L) / len(new_L)
    std_dev = (sum([(x - mean) ** 2 for x in new_L]) / len(new_L)) ** 0.5
    return std_dev


# calculate coeficient of deviation
def coefficient_of_variation(L):
    std_dev = stddev(L)
    return std_dev / (sum(L) / len(L))


# print(coefficient_of_variation([10, 4, 12, 15, 20, 5]))


def make_list(sample_size):
    """
    sample_size: int - len of list
    return: list - list of random values, length ample size
    """
    return [random.random() for i in range(sample_size)]


def plot_PDF_random(size):
    """
    L: list - list to plot
    """
    hist_size = 40
    plt.title('PDF')
    # random.random() PDF
    L = [random.random() for x in range(size)]
    plt.subplot(3, 1, 1)
    plt.ylabel('random() PDF')
    plt.hist(L, hist_size)
    # random + random PDF
    L = [random.random() + random.random() for x in range(size)]
    plt.subplot(3, 1, 2)
    plt.ylabel('random + random')
    plt.hist(L, hist_size)
    # gauss distribution PDF
    plt.subplot(3, 1, 3)
    plt.ylabel('Gauss')
    plt.hist([random.gauss(0, 30) for x in range(size)], hist_size)

    plt.show()


def prove_imeristic_rule():
    result = []
    # make function of gauss distribution mean = 0 standard deviation = 30
    mean = 0
    stddev = 30

    def gauss_function(x):
        factor1 = (1.0 / (stddev * ((2 * math.pi) ** 0.5)))
        factor2 = math.e ** -(((x - mean) ** 2) / (2 * stddev ** 2))
        return factor1 * factor2

    # find integral min = - stddev max = stddev
    # probability that x is in min - max interval = integral
    def find_probability(minimum, maximum):
        return scipy.integrate.quad(gauss_function, minimum, maximum)

    # 1. 68% of data whiting +- stddev from mean
    result.append(find_probability(mean-stddev, mean+stddev)[0])
    # 2. 95% of data whiting +- 2*stddev from mean
    result.append(find_probability(mean - 1.96*stddev, mean + 1.96*stddev)[0])
    # 3. 99.7% of data withing +- 3*stddev
    result.append(find_probability(mean - 3*stddev, mean + 3*stddev)[0])
    return result

plot_PDF_random(100000)
print(prove_imeristic_rule())

