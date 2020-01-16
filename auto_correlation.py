import numpy as np
import matplotlib.pyplot as plt


sampling_rate = 4000                                    # SAMPLING RATE
t = np.arange(-10, 10, 0.01)                            # TIME INTERVAL for t
x_t = np.cos((100.0 * np.pi * t) / sampling_rate)       # Signal x(t) = cos(100pi t)
energy_x_t = np.sum(np.abs(x_t)**2)                     # Energy of x(t) for normalization, via parseval's theorem
correlation_coefficients = []                           # Array to hold correlation results
phase = np.arange(-2.0*np.pi, 2.0*np.pi, 2.0*np.pi/40)  # Phase iteration range, -2pi to 2pi

# print(len(phase))

for i in range(len(phase)):
    x_t_delayed = np.cos((100.0 * np.pi * t + phase[i]) / sampling_rate) # delayed version of x(t)
    correlation_coeff = np.correlate(x_t, x_t_delayed)                   # Using numpy's correlate function to calculate correlation
    correlation_coeff /= energy_x_t                                      # Normalizing
    print('Correlation coefficient = ' + str(correlation_coeff))         # debug
    correlation_coefficients.append(correlation_coeff)                   # save to list

#plt.axis([-10,10,-1, 1])
plt.plot(phase, correlation_coefficients)
plt.xlabel('Phase')
plt.ylabel('CORRELATION COEFFICIENTS')
plt.show()


# print(str(correlation_coefficients))
# print('\n\n')
