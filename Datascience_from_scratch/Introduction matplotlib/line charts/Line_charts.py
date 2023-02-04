"""
* Lines charts is a good options for showing trends
"""
import matplotlib.pyplot as plt

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

#we can make multiple calls to plt.plot to show multiples series
plt.plot(xs, variance, 'g-', label='variance') #green solid line
plt.plot(xs, bias_squared, 'r-.', label='bias^2') #red dot dashed
plt.plot(xs, total_error, 'b:', label='Total error') #blue dotted line

#Because we've assigned labels to each series.
#we can get a legend for free (loc=9 wich means top center)

plt.legend(loc=9)
plt.xlabel("model complexity")
plt.xticks([])
plt.title("The bias-variance tradeoff")
plt.show()