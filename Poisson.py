import numpy as np
import scipy.stats
import matplotlib.pyplot as plt


def plotPoisson():
    # Window parameters
    xMin = -500
    xMax = 500
    yMin = -500
    yMax = 500

    # Dimensions
    xDel = xMax-xMin
    yDel = yMax-yMin
    totarea = xDel*yDel

    # Intensity of the Poisson process
    lambda0 = 200

    # Number of Nodes
    numbPoints = 100

    # X coordinates of Poisson points
    x = xDel*scipy.stats.uniform.rvs(0, 1, ((numbPoints, 1)))+xMin

    # Y coordinates of Poisson points
    y = yDel*scipy.stats.uniform.rvs(0, 1, ((numbPoints, 1)))+yMin

    # Plotting
    plt.scatter(x, y, edgecolor='blue', facecolor='cyan', alpha=0.75)

    # Labelling
    plt.xlabel("X AXIS")
    plt.ylabel("Y AXIS")

    # Showing the plot
    plt.show()
