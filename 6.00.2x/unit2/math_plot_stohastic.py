import matplotlib.pyplot as plt
import random

x = []
for i in range(100000):
    l = [random.randint(0, 1) for x in range(30)]
    x.append(l.count(1))


# the histogram of the data
plt.hist(x)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')

plt.grid(True)
plt.show()