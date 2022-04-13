from sympy import *
import numpy as np
from lab4.LinRegr import *
from lab4.PolRegres import *
from lab4.ExpRegres import *
from lab4.AdjGrad import *
from lab4.brent import *
import math



class User:
    def userAnswer(self):
        """
        Функция создана дл упрощения работы пользователя с данной программой, тут представлены подсказки и премеры ввода
        данных.

        Returns
        ===========
        Обращается к нужной функции метода и передает ей необходимые параметры.
        """
        print(
            "Каким методом регрессии хотите воспользоваться?\n"
            "1 - Линейная регрессия\n"
            "2 - Полиномиальная регрессия\n"
            "3 - Экспоненциальная регрессия\n")

        user_answer = int(input())

        # Линейная регрессия
        if user_answer == 1:
            y = []
            print("Введите кол-во строк в матрице(n). Например 3")
            n = int(input())
            print("Введите кол-во столбцов в матрице(m). Например 3")
            m = int(input())
            print("Введите массив предсказываемых данных y = (y1, y2, ..., yn)")
            for i in range(n):
                print(f'Введите {i} значение. Например 1')
                y.append(float(input()))
            print("Введите массив предикантов X размерностью n x m")
            X = []
            for i in range(n):
                xij = []
                for j in range(m):
                    print(f'Введите x{i, j}')
                    xij.append(float(input()))
                X.append(xij)

            L = 0.95
            sigma = 0.1
            print("Хотите ввести параметр, отвечающий за вид регуляризации? 1 - да / 0 - нет")
            q = -1
            while q < 0 or q > 1:
                q = int(input())
                if q < 0 or q > 1:
                    print("Неправильный ввод. 1 - да / 0 - нет")

            if q == 1:
                print("Введите L1, или L2, или norm ")
                reg = 'j'
                while reg != "L1" and reg != "L2" and reg != "norm":
                    reg = input()
                    if reg != "L1" and reg != "L2" and reg != "norm":
                        print("Такой комманды нет. Введите снова. L1, или L2, или norm")

                if reg == "L1" or reg == "L2":
                    print(
                        "Введите коэффициент регуляции. Например 0.95. Значение должно быть >=0. (чем больше, тем сильнее регуляризация)")
                    L = -1
                    while L < 0 or L > 1:
                        L = float(input())
                        if L < 0 or L > 1:
                            print("Некорректно введен коэффициент регуляции. Значение должно быть >=0.")

                elif reg == "norm":
                    print(
                        "Введите предполагаемое стандартное отклонение остатков. Например 0.1. Значение должно быть >=0 и <=1. (чем больше, тем слабее регуляризация)")
                    sigma = -1
                    while sigma < 0 or sigma > 1:
                        sigma = float(input())
                        if sigma < 0 or sigma > 1:
                            print(
                                "Некорректно введено предполагаемое стандартное отклонение остатков. Значение должно быть >=0 и <=1.")
            elif q == 0:
                reg = 'None'

            functionss = LinRegr()
            functionss.find(np.array(y).reshape(-1, 1), X, n, m, reg, L, sigma)


        # Полиномиальная регрессия
        elif user_answer == 2:
            y = []
            print("Введите кол-во строк в матрице(n). Например 3")
            n = int(input())
            print("Введите кол-во столбцов в матрице(m). Например 3")
            m = int(input())
            print("Введите массив предсказываемых данных y = (y1, y2, ..., yn)")
            for i in range(n):
                print(f'Введите {i} значение. Например 1')
                y.append(float(input()))
            print("Введите массив предикантов X размерностью n x m")
            X = []
            for i in range(n):
                xij = []
                for j in range(m):
                    print(f'Введите x{i, j}')
                    xij.append(float(input()))
                X.append(xij)

            L = 0.95
            sigma = 0.1

            print("Введите степень полинома (целое число больше нуля). Например: 2")
            deg = int(input())
            q = -1

            print("Хотите ввести параметр, отвечающий за вид регуляризации? 1 - да / 0 - нет")
            q = -1
            while q < 0 or q > 1:
                q = int(input())
                if q < 0 or q > 1:
                    print("Неправильный ввод. 1 - да / 0 - нет")

            if q == 1:
                print("Введите L1, или L2, или norm ")
                reg = 'j'
                while reg != "L1" and reg != "L2" and reg != "norm":
                    reg = input()
                    if reg != "L1" and reg != "L2" and reg != "norm":
                        print("Такой комманды нет. Введите снова. L1, или L2, или norm")

                if reg == "L1" or reg == "L2":
                    print(
                        "Введите коэффициент регуляции. Например 0.95. Значение должно быть >=0. (чем больше, тем сильнее регуляризация)")
                    L = -1
                    while L < 0 or L > 1:
                        L = float(input())
                        if L < 0 or L > 1:
                            print("Некорректно введен коэффициент регуляции. Значение должно быть >=0.")

                elif reg == "norm":
                    print(
                        "Введите предполагаемое стандартное отклонение остатков. Например 0.1. Значение должно быть >=0 и <=1. (чем больше, тем слабее регуляризация)")
                    sigma = -1
                    while sigma < 0 or sigma > 1:
                        sigma = float(input())
                        if sigma < 0 or sigma > 1:
                            print(
                                "Некорректно введено предполагаемое стандартное отклонение остатков. Значение должно быть >=0 и <=1.")
            elif q == 0:
                reg = 'None'

            functionss = PolRegres()
            functionss.find(np.array(y).reshape(-1, 1), X, n, m, deg, reg, L, sigma)

        # Экспоненциальная регрессия
        elif user_answer == 3:

            y = []
            print("Введите кол-во строк в матрице(n). Например 3")
            n = int(input())
            print("Введите кол-во столбцов в матрице(m). Например 3")
            m = int(input())
            print("Введите массив предсказываемых данных y = (y1, y2, ..., yn)")
            for i in range(n):
              print(f'Введите {i} значение. Например 1')
              y.append(math.log1p(float(input())))
            print("Введите массив предикантов X размерностью n x m")
            X = []
            for i in range(n):
              xij = []
              for j in range(m):
                  print(f'Введите x{i, j}')
                  xij.append(float(input()))
              X.append(xij)

            L = 0.95
            sigma = 0.1
            print("Хотите ввести параметр, отвечающий за вид регуляризации? 1 - да / 0 - нет")
            q = -1
            while q < 0 or q > 1:
               q = int(input())
               if q < 0 or q > 1:
                   print("Неправильный ввод. 1 - да / 0 - нет")

            if q == 1:
               print("Введите L1, или L2, или norm ")
               reg = 'j'
               while reg != "L1" and reg != "L2" and reg != "norm":
                   reg = input()
                   if reg != "L1" and reg != "L2" and reg != "norm":
                       print("Такой комманды нет. Введите снова. L1, или L2, или norm")

               if reg == "L1" or reg == "L2":
                   print("Введите коэффициент регуляции. Например 0.95. Значение должно быть >=0. (чем больше, тем сильнее регуляризация)")
                   L = -1
                   while L < 0 or L > 1:
                       L = float(input())
                       if L < 0 or L > 1:
                           print("Некорректно введен коэффициент регуляции. Значение должно быть >=0.")

               elif reg == "norm":
                   print("Введите предполагаемое стандартное отклонение остатков. Например 0.1. Значение должно быть >=0 и <=1. (чем больше, тем слабее регуляризация)")
                   sigma = -1
                   while sigma < 0 or sigma > 1:
                       sigma = float(input())
                       if sigma < 0 or sigma > 1:
                           print("Некорректно введено предполагаемое стандартное отклонение остатков. Значение должно быть >=0 и <=1.")
            elif q == 0:
               reg = 'None'

            functionss = ExpRegres()
            functionss.find(np.array(y).reshape(-1, 1), X, n, m, reg, L, sigma)

        else:
            print('Введен неверный номер')
