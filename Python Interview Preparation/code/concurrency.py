# the output could be not clear
# it could be useful comment the part of code to obtain a clearer output

print("### Multithread example ###")

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)

def print_letters():
    for letter in 'ABCDE':
        time.sleep(1)
        print(letter)

# Create two threads
thread_numbers = threading.Thread(target=print_numbers)
thread_letters = threading.Thread(target=print_letters)

# Start the threads
thread_numbers.start()
thread_letters.start()

# Wait for both threads to finish
time.sleep(2)
thread_numbers.join()
thread_letters.join()



print("Both threads have finished.")




print()
print("############################################################")
print()
############################################################
############################################################

print("### Multiprocessing example ###")
import multiprocessing

def square(number):
    result = number * number
    print(f"The square of {number} is {result}")

if __name__ == "__main__":
    # List of numbers to calculate the square
    numbers = [1, 2, 3, 4, 5]

    # Create a process for each number
    processes = []
    for number in numbers:
        process = multiprocessing.Process(target=square, args=(number,))
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    print("All processes have finished.")
