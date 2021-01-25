import numpy as np
import scipy.interpolate as spi
import matplotlib.pyplot as plt


def optical_cable():
    data = np.loadtxt('./sea2020.csv', delimiter=',', encoding='gb2312')
    x = data[:, 0]
    y = data[:, 1]

    ix3 = np.arange(0, 5000 + 1, 0.1)  # x轴以5为间距，细化差值网格
    ipo3 = spi.splrep(x, y, k=3)
    iy3 = spi.splev(ix3, ipo3)
    plt.plot(x, [-n for n in y], 'r*', ix3, [-n for n in iy3])

    sum_dist = 0
    for i in range(50000):
        # print(iy3[i + 1])
        dist = np.sqrt((iy3[i + 1] - iy3[i]) ** 2 + 0.1 ** 2)
        sum_dist += dist
    plt.title("Simulation of Optical Cable on Seabed")
    plt.xlabel("Width (m)")
    plt.ylabel("Depth (m)")
    plt.legend(["Sample data point", "Cubic spline interpolation curve"],
               loc='upper right')

    print('所需光缆的长度的近似值为：{:.2f} m'.format(sum_dist))
    plt.savefig('./Q1.png')
    plt.show()


if __name__ == "__main__":
    # Question 1
    optical_cable()
