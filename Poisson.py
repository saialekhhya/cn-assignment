import numpy as np
import scipy.stats
import matplotlib.pyplot as plt


def plotPoisson(length, width, numNodes, numDeadNodes=0):
    # Window parameters
    xMin = -500
    yMin = -500

    # Dimensions
    xDel = length
    yDel = width
    totarea = xDel*yDel

    # X coordinates of Poisson points
    x = xDel*scipy.stats.uniform.rvs(0, 1, ((numNodes, 1)))+xMin

    # Y coordinates of Poisson points
    y = yDel*scipy.stats.uniform.rvs(0, 1, ((numNodes, 1)))+yMin

    # Plotting
    plt.scatter(x, y, edgecolor='blue', facecolor='cyan', alpha=0.75)

    # Labelling
    plt.xlabel("X AXIS")
    plt.ylabel("Y AXIS")

    # Showing the plot
    plt.show()
