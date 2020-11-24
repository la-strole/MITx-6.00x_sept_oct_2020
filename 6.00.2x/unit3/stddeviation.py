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
    result.append(find_probability(mean - stddev, mean + stddev)[0])
    # 2. 95% of data whiting +- 2*stddev from mean
    result.append(find_probability(mean - 1.96 * stddev, mean + 1.96 * stddev)[0])
    # 3. 99.7% of data withing +- 3*stddev
    result.append(find_probability(mean - 3 * stddev, mean + 3 * stddev)[0])
    return result


def prove_CLT():
    population = [random.randint(0, 100) for x in range(10 ** 6)]

    samples_count = 10
    sample_length = 10

    means = []
    for i in range(samples_count):
        sample = [random.choice(population) for x in range(sample_length)]
        sample_mean = sum(sample) / len(sample)
        means.append(sample_mean)

    # check if means is normally distributed
    # draw population distribution and sample distribution
    hist_size = 20

    plt.subplot(2, 1, 1)
    plt.xlabel('set of means')
    plt.ylabel('probability')
    plt.hist(population, hist_size, weights=[1 / len(population) for x in range(len(population))])

    plt.subplot(2, 1, 2)
    plt.xlabel('set of means')
    plt.ylabel('probability')
    plt.title(f'PDF of CLT. size of sample - {sample_length}, number of samples - {samples_count}')
    plt.hist(means, hist_size, weights=[1 / len(means) for x in range(len(means))])
    plt.show()

    # this distribution will have mean close to the mean of population
    samples_mean = sum(means) / len(means)
    population_mean = sum(population) / len(population)
    print(f'mean of population = {population_mean}\n'
          f'mean of sample  = {samples_mean}')

    # the variance of the samples will be close to the variance of the population divided by the sample size
    variance_of_sample = sum([(x - samples_mean) ** 2 for x in means]) / sum(means)
    variance_of_popoulation = sum([(x - population_mean) ** 2 for x in population]) / sum(population)
    print(f'variance of the means = {variance_of_sample}\n'
          f'variance of population = {variance_of_popoulation}\n'
          f'variance of population divided by the sample size = {variance_of_popoulation / sample_length}')


def Buffon_laplas_pi_proof():
    number_needles = 10 ** 3
    inside = 0
    outside_inside = number_needles
    for i in range(number_needles):
        x = random.random()
        y = random.random()
        if ((x ** 2) + (y ** 2)) <= 1:
            inside += 1
    print(f'inside = {inside}, outside+inside={outside_inside}')
    pi_by_Buffon = (4 * inside) / outside_inside
    return pi_by_Buffon


# plot_PDF_random(100000)
# print(prove_imeristic_rule())
# prove_CLT()
print(Buffon_laplas_pi_proof())
