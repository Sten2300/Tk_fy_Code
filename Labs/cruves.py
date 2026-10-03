import matplotlib.pyplot as plt
import numpy as np

# Add title
plt.title('hujo0715', fontweight="bold", size = 20, pad=10)

# x values
x = np.linspace(-10, 10, 100)

# f(x) curves to plot (arrays of y values)
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
linear = x
quadratic = x*x
sinus = 10*np.sin(2*x)


# Plot functions
plt.plot(x,linear,color="red", label="x")
plt.plot(x, quadratic, color="blue", label="x^2")
plt.plot(x,sinus,color="green", label="10*sin(2x)")

#display legend
plt.legend()

# Display the generated figure
plt.show()

