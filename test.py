def compute_cube(num):
    print("%d cubed = %d" %(num, num**3))

def compute_square(num):
    print("%d squared = %d" %(num, num**2))

import multiprocessing

#print(multiprocessing.cpu_count()) #prints number of cores in local machine
if __name__ == "__main__":
    process1 = multiprocessing.Process(target = compute_square, args = (4,))
    process2 = multiprocessing.Process(target = compute_cube, args = (3,))
    process1.start()
    if(process1.is_alive):
        print("Process1 begins...")
    process2.start()
    if(process2.is_alive):
        print("Process2 begins...")
    process1.join() #wait for process1 to complete
    process2.join() # sames as above
    print("Processes complete!")