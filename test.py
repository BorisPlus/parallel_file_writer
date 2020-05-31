from multiprocessing import Pool
import random
import time


file_out = 'output.txt'


def f(process_id):
    # process_id - это просто id процесса, который пишет в файл
    while True:
        # выбираем рандомно t от 1 до 10
        t = random.choice(range(1, 3))
        # спим t
        time.sleep(t)
        # пишем в файл последовательнось
        with open(file_out, 'a') as file:
            file.write('process with ID "%s" write DATA "%s"' % (process_id, t))
            file.write('\n')


if __name__ == '__main__':
    # сколько процессов будут писать в файл
    processes_count = 6
    # запустим
    with Pool(processes_count) as p:
        print(p.map(f, range(1, processes_count)))
