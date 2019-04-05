def compute_cube(num):
    print("%d cubed = %d" %(num, num**3))

def compute_square(num):
    print("%d squared = %d" %(num, num**2))

import multiprocessing

#print(multiprocessing.cpu_count()) #prints number of cores in local machine
if __name__ == "__main__":
    process1 = multiprocessing.Process(target = compute_square, args = (4,))
    process1.start()
    process1.join() #wait for process1 to complete
    print("Process1 complete!")