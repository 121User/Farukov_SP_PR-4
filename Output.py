import os.path
import datetime

timeFile: float = os.path.getmtime('Degrees.txt')

file = open('Degrees.txt', 'r')
file.read()
try:
    if __name__ == '__main__':
        while True:
            tFile: float = os.path.getmtime('Degrees.txt')

            if timeFile != tFile:
                timeFile = tFile
                tFile = tFile.__round__()
                dateFile: datetime = datetime.datetime.fromtimestamp(tFile)

                res, _ = file.readline().split(' - ')

                print(f'{dateFile} >> {res}')
except ValueError:
    print('Файл пуст')
finally:
    file.close()