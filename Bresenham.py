from matplotlib import pyplot as plt
import pandas as pd

startsPoint = [-21, 14]
endPoint = [7,-7]


def calcBresenham(origin: list, destination: list):
    dx = abs(destination[0] - origin[0])
    dy = abs(destination[1] - origin[1])

    m = dy/dx

    checker = True

    xCoords = [origin[0]]
    yCoords = [origin[1]]

    mm = False

    steps = 1
    if (origin[0] > destination[0]) or (origin[1] > destination[1]):
        steps = -1

    if m < 1:
        Neworigin = [origin[1], origin[0]]
        Newdest = [destination[1], destination[0]]
        origin = Neworigin
        destination = Newdest
        dx = abs(destination[0] - origin[0])
        dy = abs(destination[1] - origin[1])
        mm = True

    p0 = 2 * dx - dy
    x = origin[0]
    y = origin[1]


    for i in range(abs(destination[1] - origin[1])):

        if checker:
            xPrev = origin[0]
            pPrev = p0
            p = p0
            checker = False
        else:
            xPrev = x
            pPrev = p

        if p >= 0:
            x = x + steps

        p = pPrev + 2*dx - 2*dy*(abs(x-xPrev))
        y = y + 1

        if mm:
            xCoords.append(y)
            yCoords.append(x)
        else:
            xCoords.append(x)
            yCoords.append(y)

    return [xCoords, yCoords]

def showPlot(item: list):
    plt.plot(item[0], item[1], marker="o", markersize=5, markerfacecolor="red")
    plt.show()



data = calcBresenham(startsPoint, endPoint)
pdDataFrame = pd.DataFrame({'X Coordinate': data[0], 'Y Coordinate': data[1]})
print(pdDataFrame)

### pdDataFrame.to_excel("Bresenham_Result.xlsx")  # only use when trying to save new dataframe

showPlot(data)

