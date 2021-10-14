import Poisson as pois
import Nodes as nodes


if __name__ == "__main__":

    length = 1000
    width = 1000

    numNodes = 100
    numDeadNodes = 0
    ctrlPktSize = 200

    pois.plotPoisson(length, width, numNodes, numDeadNodes)
