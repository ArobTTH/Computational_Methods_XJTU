import numpy as np


def sparse_matrix():
    def gauss_solve(arr_A, arr_B, n, width):
        arr_x = np.zeros(n)
        for k in range(n - 1):
            if arr_A[k][k] == 0:
                print('Zero. Failed.')
                return -1
            for i in range(k + 1, int(min((n, k + width + 1)))):
                temp = arr_A[i][k] / arr_A[k][k]
                for j in range(k, int(min((n, k + 2 * width + 2)))):
                    arr_A[i][j] = arr_A[i][j] - temp * arr_A[k][j]
                arr_B[i] = arr_B[i] - temp * arr_B[k]

        arr_x[n - 1] = arr_B[n - 1] / arr_A[n - 1][n - 1]
        for k in range(n - 1, -1, -1):
            temp = arr_B[k]
            for j in range(k + 1, int(min((n, k + width + 1)))):
                temp = temp - arr_A[k][j] * arr_x[j]
            arr_x[k] = temp / arr_A[k][k]
        return arr_x

    def exchange(a_temp, a, rows, width):
        for i in range(rows):
            a[i][i] = a_temp[i][width]
            for j in range(1, width + 1):
                if a_temp[i][width + j] != 0:
                    a[i][i + j] = a_temp[i][width + j]
                if a_temp[i][width - j] != 0:
                    a[i][i - j] = a_temp[i][width - j]

    # 非压缩矩阵
    def un_compression_matrix(filepath):

        # 读取文件的数据项
        file_info = np.fromfile(filepath, dtype=np.int32, count=6)
        n = file_info[3]
        width = file_info[4]

        mat_data = np.fromfile(filepath, dtype=np.float32)[6:]
        mat_a = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                mat_a[i, j] = mat_data[i * n + j]
        mat_b = mat_data[n * n:]
        mat_x = gauss_solve(mat_a, mat_b, n, width)
        print(filepath, ': ', mat_x)
        np.savetxt('2000阶非压缩矩阵计算结果.csv', mat_x, fmt='%f', delimiter=" ")

    # 压缩矩阵
    def compression_matrix(filepath):
        file_info = np.fromfile(filepath, dtype=np.int32, count=6)
        n = file_info[3]
        width = file_info[4]
        mat_data = np.fromfile(filepath, dtype=np.float32)[6:]
        mat_a = np.zeros((n, n))
        mat_atemp = np.zeros((n, (2 * width + 1)))
        for i in range(n):
            mat_atemp[i, :] = mat_data[i * (2 * width + 1):(i + 1) *
                                                           (2 * width + 1)]
        exchange(mat_atemp, mat_a, n, width)
        mat_b = mat_data[n * (2 * width + 1):]
        mat_x = gauss_solve(mat_a, mat_b, n, width)
        print(filepath, ': ', mat_x)
        np.savetxt('5000阶压缩矩阵计算结果.csv', mat_x, fmt='%f', delimiter=" ")

    un_compression_matrix('./data20201.dat')
    compression_matrix('./data20202.dat')
    un_compression_matrix('./data20203.dat')
    compression_matrix('./data20204.dat')


if __name__ == "__main__":
    # Question 3
    sparse_matrix()
