
from multiprocessing import cpu_count, Pool
from time import time, sleep
from concurrent.futures import ProcessPoolExecutor


def factorize(*numbers: int) -> list[int]:
    factorize_numbers = []

    def factorize_one_number(number: int):
        result_numbers = []

        for i in range(1, number + 1):
            if number % i:
                continue
            else:
                result_numbers.append(i)

        return result_numbers

    for num in numbers:
        factorize_numbers.append(factorize_one_number(num))
    
    return factorize_numbers

    

# a, b, c, d  = factorize(128, 255, 99999, 10651060)

# assert a == [1, 2, 4, 8, 16, 32, 64, 128]
# assert b == [1, 3, 5, 15, 17, 51, 85, 255]
# assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
# assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

if __name__ == '__main__':
    timer = time()
    print('Start of simple calc')
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    print(f'Results: \n a = {a}, \n b = {b}, \n c = {c} \n d = {d}')
    print(f'Calculate time = {time() - timer}')

    sleep(2)

    timer = time()
    print('Start of multiprocessing calc')
    
    # with Pool(processes=cpu_count()) as pool:
    #     a, b, c, d = pool.map(factorize, (128, 255, 99999, 10651060))
    #     pool.close()
    #     pool.join()

    with ProcessPoolExecutor(cpu_count()) as executor:
        a, b, c, d = executor.map(factorize, (128, 255, 99999, 10651060))
        
    print(f'Results: \n a = {a}, \n b = {b}, \n c = {c} \n d = {d}')
    print(f'Multiprocessing calculate time = {time() - timer}')