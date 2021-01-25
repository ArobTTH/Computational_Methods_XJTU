import numpy as np
import matplotlib.pyplot as plt


def covid_19_analysis():
    # (1)
    x = np.arange(0, 306 + 1)
    x1 = np.arange(0, 306 + 0.1, 0.1)
    y = np.loadtxt('./alltime_world.csv', delimiter=',')
    y = y[:, 2]

    plt.plot(x, y, 'b*')

    p2 = np.polyfit(x, y, 2)  # 二次函数拟合
    y2 = np.polyval(p2, x1)
    plt.plot(x1, y2, '-r')  # 作二次函数的拟合曲线
    z_2 = np.poly1d(p2)

    p3 = np.polyfit(x, y, 3)  # 三次函数拟合
    y3 = np.polyval(p3, x1)
    plt.plot(x1, y3, '-g')  # 作三次函数的拟合曲线
    z_3 = np.poly1d(p3)

    p4 = np.polyfit(x, y, 4)  # 四次函数拟合
    y4 = np.polyval(p4, x1)
    plt.plot(x1, y4, '-y')  # 作四次函数拟合曲线
    z_4 = np.poly1d(p4)

    plt.axis([0, 400, 0, 7e7])

    plt.title("Fitting results for the number of confirmed cases worldwide")
    plt.xlabel("Days")
    plt.ylabel("Number of people diagnosed")
    plt.legend(
        ["Data Points", "Quadratic", "Cubic", "Quartic"],
        loc='upper right')
    plt.show()

    print('二次函数拟合的函数解析式为\n y = {:}\n 二次函数拟合预测2021年1月1日，全球将有{:.0f}人被感染\n'.format(z_2, z_2(339)))
    print('三次函数拟合的函数解析式为\n y = {:}\n 三次函数拟合预测2021年1月1日，全球将有{:.0f}人被感染\n'.format(z_3, z_3(339)))
    print('四次函数拟合的函数解析式为\n y = {:}\n 四次函数拟合预测2021年1月1日，全球将有{:.0f}人被感染\n'.format(z_4, z_4(339)))

    # (2)
    x = np.arange(0, 280 + 1)
    x1 = np.arange(0, 280 + 0.1, 0.1)
    y = np.loadtxt('./alltime_american.csv',
                   delimiter=',',
                   encoding='gb2312',
                   usecols=2)

    plt.plot(x, y, 'b*')

    p2 = np.polyfit(x, y, 2)  # 二次函数拟合
    y2 = np.polyval(p2, x1)
    plt.plot(x1, y2, '-r')  # 作二次函数的拟合曲线
    z_2 = np.poly1d(p2)

    p3 = np.polyfit(x, y, 3)  # 三次函数拟合
    y3 = np.polyval(p3, x1)
    plt.plot(x1, y3, '-g')  # 作三次函数的拟合曲线
    z_3 = np.poly1d(p3)

    p4 = np.polyfit(x, y, 4)  # 四次函数拟合
    y4 = np.polyval(p4, x1)
    plt.plot(x1, y4, '-y')  # 作四次函数拟合曲线
    z_4 = np.poly1d(p4)

    plt.axis([0, 400, 0, 2e7])

    plt.title("Fitting results for the number of confirmed cases in American")
    plt.xlabel("Days")
    plt.ylabel("Number of people diagnosed")
    plt.legend(
        ["Data Points", "Quadratic", "Cubic", "Quartic", ],
        loc='upper right')
    plt.show()

    print('二次函数拟合的函数解析式为\n y = {:}\n 二次函数拟合预测2021年1月1日，美国将有{:.0f}人被感染\n'.format(z_2, z_2(339)))
    print('三次函数拟合的函数解析式为\n y = {:}\n 三次函数拟合预测2021年1月1日，美国将有{:.0f}人被感染\n'.format(z_3, z_3(339)))
    print('四次函数拟合的函数解析式为\n y = {:}\n 四次函数拟合预测2021年1月1日，美国将有{:.0f}人被感染\n'.format(z_4, z_4(339)))


if __name__ == "__main__":
    # Question 2
    covid_19_analysis()
