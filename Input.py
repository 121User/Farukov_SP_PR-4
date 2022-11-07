import multiprocessing
from multiprocessing import Process
from multiprocessing.queues import Queue


# Запись в файл
def writing(num, deg, result, sumDig):
    file = open('Degrees.txt', 'a')
    file.write(f'{num}^{deg}={result} : {sumDig}\n')
    file.close()
# Сумма цифр числа
def sumDigits(num):
    sumD = 0
    for i in range(num + 1):
        sumD += i
    return sumD
# Формирование результата
def resCalc(que):
    while True:
        if not que.empty():
            num, deg = que.get()
            res: int = num ** deg
            sumD: int = sumDigits(res)

            writing(num, deg, res, sumD)


# # Вывод числа, степени и результата вычисления в скрипте Output
# def resOutput(conn):
#
#     res: int = number ** degrees
#
#     stringRes = f'{number}^{degrees} = {res}'
#     return stringRes


try:
    if __name__ == '__main__':
        queue: Queue = multiprocessing.Manager().Queue() # Очередь для расчетов


        pr1: Process = Process(target=resCalc, args=(queue,))
        pr1.daemon = True
        pr1.start()

        while True:
            number, degrees = input('Введите число и степень: ').split()

            queue.put((int(number), int(degrees)))

except ValueError:
    print('Число и/или степень введены некорректно')