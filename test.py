import numpy as np
import matplotlib.pyplot as plt

# Duration in minutes for the x-axis
time = np.logspace(0, np.log10(8*60), 500)  # 8 hours, log scale for x-axis

# Hypothetical power output model: starts high and decreases over time
# We will use a reciprocal function to model this
start_power = 1500  # High initial power
end_power = 200  # Power after 8 hours
decay_rate = (start_power - end_power) / (8*60)  # Linear decay for simplicity

# Power output over time
power = start_power / (1 + (time * decay_rate / start_power))

# Plotting the power curve
plt.figure(figsize=(15, 6))
plt.plot(time, power, label='Cyclist Power Output')
plt.xscale('log')  # Logarithmic scale for the x-axis
plt.yscale('log')  # Logarithmic scale for the y-axis
plt.title('Power Curve of a Cyclist')
plt.xlabel('Time (minutes)')
plt.ylabel('Power (Watts)')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.show()

