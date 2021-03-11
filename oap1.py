from array import *

# K - матрица жесткости системы, размерность 3x3
# q - вектор-столбец неизвестных узловых перемещений
# f - вектор-столбец известных внешних нагрузок

# Жесткости элементов
EF1 = 3
EF2 = 7

# Внешнее усилие
F = 10

# Матрицы жесткости элементов
# Внешняя нумерация - строки; внутренняя - столбцы
#  EF1 -EF1
# -EF1  EF1
K1 = [[EF1, -EF1],
      [-EF1, EF1]]
K2 = [[EF2, -EF2],
      [-EF2, EF2]]

print("K1:", K1)
print("K2:", K2)

# Матрица жесткости системы
K = [[K1[0][0], K1[0][1],            0],
     [K1[1][0], K1[1][1] + K2[0][0], K2[0][1]],
     [0,        K2[1][0],            K2[1][1]]]

print("K:", K)

# Граничные условия, примененные к глобальной матрице жесткости системы:
K[0][0] = 1
K[0][1] = 0
K[1][0] = 0

K[2][2] = 1
K[2][1] = 0
K[1][2] = 0

print("K:", K)

# Вектор внешних узловых увилий:
f = [0, F, 0]

print("f:", f)

# Неизвестное перемещение во втором узле:
# u2
u1 = 0
u2 = f[1] / K[1][1]
u3 = 0

u = [u1, u2, u3]

print("u:", u)


def scalar_product(a, b):
    return a[0]*b[0]+a[1]*b[1]


def approximation(x, u):
    l = 1
    N1 = 1 - x / l
    N2 = x / l
    N = [N1, N2]
    return scalar_product(N, u)


print("Перемещения для первого элемента")
print("0", approximation(0, [u1, u2]))
print("0.25", approximation(0.25, [u1, u2]))
print("0.5", approximation(0.5, [u1, u2]))
print("0.75", approximation(0.75, [u1, u2]))
print("1", approximation(1, [u1, u2]))

print("Перемещения для второго элемента")
print("0", approximation(0, [u2, u3]))
print("0.25", approximation(0.25, [u2, u3]))
print("0.5", approximation(0.5, [u2, u3]))
print("0.75", approximation(0.75, [u2, u3]))
print("1", approximation(1, [u2, u3]))
