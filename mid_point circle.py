# Midpoint circle drawing algo

import matplotlib.pyplot as plt


def mid_circle(x0, y0, r):
    x = 0
    y = r

    x_plt = []
    y_plt = []

    print(x, y)

    d = 1 - r

    while (x < y):
        if (d < 0):
            x += 1
            d = d + 2 * x + 3
        else:
            x += 1
            y -= 1
            d = d + 2 * (x - y) + 5

        print(x, y)
        x_plt.append(x + x0)
        y_plt.append(y + y0)
        plt.scatter(x_plt, y_plt)

        x_plt.append(y + x0)
        y_plt.append(x + y0)
        plt.scatter(x_plt, y_plt)

        x_plt.append(-y + x0)
        y_plt.append(x + y0)
        plt.scatter(x_plt, y_plt)

        x_plt.append(-x + x0)
        y_plt.append(y + y0)
        plt.scatter(x_plt, y_plt)

        x_plt.append(-x + x0)
        y_plt.append(-y + y0)
        plt.scatter(x_plt, y_plt)

        x_plt.append(-y + x0)
        y_plt.append(-x + y0)
        plt.scatter(x_plt, y_plt)

        x_plt.append(y + x0)
        y_plt.append(-x + y0)
        plt.scatter(x_plt, y_plt)

        x_plt.append(x + x0)
        y_plt.append(-y + y0)
        plt.scatter(x_plt, y_plt)


mid_circle(4, 5, 7)
plt.title("Output of Mid point circle drawing algorithm")
plt.show()