# Multi-Processing
# Multiprocessing is a technique where we run separate task parallely on seprate memory or cpu(or cores of cpu), also known as true parallelism.
# let us run the same program we saw in multi_threading

import multiprocessing
import time

def calculate_square(numbers):
    for n in numbers:
        time.sleep(0.2)
        print('Square:', n * n)

def calculate_cube(numbers):
    for n in numbers:
        time.sleep(0.2)
        print('Cube:', n * n * n)

# This block is essential for multiprocessing to work safely across all OS
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    start = time.time()

    p1 = multiprocessing.Process(target=calculate_square, args=(numbers,))
    p2 = multiprocessing.Process(target=calculate_cube, args=(numbers,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()

    print("Total time: ", end - start)