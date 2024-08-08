import csv
import numpy as np
import matplotlib.pyplot as plt


# data
theta = np.linspace(-2 * np.pi, 2 * np.pi, 10_000)
cos = np.cos(theta)
sin = np.sin(theta)

# exporting data
with open('data.csv', 'w', newline = '') as file:
    writer = csv.DictWriter(file, fieldnames = [
        "theta", "cos", "sin"
        ])
    writer.writeheader()

    for i in range(len(theta)):
        writer.writerow({
            "theta": theta[i], "cos": cos[i], "sin": sin[i]
            })
