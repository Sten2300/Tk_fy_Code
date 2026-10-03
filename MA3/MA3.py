""" MA3.py

Student:
Mail:
Reviewed by:
Date reviewed:

"""
import random
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
from statistics import mean 
from time import perf_counter as pc
from numba import njit


# Exc1
def approximate_pi(n):
    # n is the number of points
    lst_x_circ = []
    lst_y_circ = []
    lst_x_sqre = []
    lst_y_sqre = []

    for _ in range(n):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)

        if x**2 + y**2 <=1: # if inside circle
            lst_x_circ.append(x) 
            lst_y_circ.append(y)
        else:
            lst_x_sqre.append(x)
            lst_y_sqre.append(y)

    n_c = len(lst_x_circ) #length of x values in closed circle.

    pi_approx = 4*n_c/n #approx as per Monte Carlo method.

    ### print of number of points and pi approximation
    print(f"Number of points checked {n}")
    print(f'Approximation of pi was: {round(pi_approx,5)}')

    plt.figure()
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.scatter(lst_x_circ,lst_y_circ, color="r", s=1, label = "Inside")
    plt.scatter(lst_x_sqre,lst_y_sqre, color = "b", s=1, label = "Outside")
    plt.title(f"Monte Carlo Approx: n={n}, approx={pi_approx}")
    plt.savefig(f"mc_pi_{n}.png")
    plt.close()

    return pi_approx

# Exc2, approximation
def sphere_volume(n, d, r = 1):
    # n is the number of points
    # d is the number of dimensions of the sphere 
    # r is the radius 
    lst_lst_p = [[random.uniform(-r,r) for _ in range(d)] for _ in range(n)] # list of n elements with d points
    lst_dist_squared = map(lambda p: sum(x**2 for x in p), lst_lst_p) # sums the square of each list of d elements
    lst_inside = list(filter(lambda x: x <= r**2, lst_dist_squared)) #filters out x>r^2

    return ((2*r)**d)*(len(lst_inside)/n)


#Exc2, real value
def hypersphere_exact(n, d, r = 1):
    # n is the number of points
    # d is the number of dimensions of the sphere 
    vol = (m.pi**(d/2)*(r**d)/(m.gamma(d/2+1)))
    return vol

#Exc3: numba version


@njit   
def sphere_volume_numba(n:int, d:int)->float:
    # n is the number of points
    # d is the number of dimensions of the sphere
    p_inside = 0
    for _ in range(n):
        cur_sum = 0
        for _ in range(d):
            cur_sum += random.uniform(-1,1)**2
        if cur_sum <= 1:
            p_inside += 1
    return (2**d)*(p_inside/n)


    return

#Exc4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n, d, np=10):
    # n is the number of points
    # d is the number of dimensions of the sphere
    # np is the number of processes
    lst_n_chunk = [n//np]*np 
    lst_d = [d]*np
    with future.ProcessPoolExecutor(max_workers=np) as ex:
        lst_res = list(ex.map(sphere_volume, lst_n_chunk, lst_d))

    return sum(lst_res) / np 
    
def main():
    # Exc1
    # dots = [1000, 10000, 100000]
    # for n in dots:
    #     approximate_pi(n)

    # Exc2
    # n = 100000
    # d = 2
    # print(f'Approx volume of {d} dimentional sphere = {sphere_volume(n, d, 4)}')  #originally only sphere_volume(n, d)
    # print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d, 4)}") # + radius of 4.

    # n = 100000
    # d = 11
    # print(f'Approx volume of {d} dimentional sphere = {sphere_volume(n, d)}')
    # print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")

    # Exc3
    # n = 1000000
    # d = 11
    # for i in range(3): # regular
    #     start = pc()
    #     sphere_volume(n, d)
    #     stop = pc()
    #     print(f"Exc3: non-numba time {i+1} of {d} dim and {n}: {stop-start}")

    # for i in range(3): #numba
    #     start = pc()
    #     sphere_volume_numba(n, d)
    #     stop = pc()
    #     print(f"Exc3: the numba time {i+1} of {d} dim and {n}: {stop-start}")        
    #     #analys: Mycket snabbare efter första kompliering, medan non-numba är konstant samma


    # Exc4
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n, d)
    stop = pc()
    print(f"Exc4: Sequential time of dim {d} and n = {n}: {stop-start}")
    start2 = pc()
    sphere_volume_parallel2(n,d)
    stop2 = pc()
    print(f'Exc4: Parallell time of dim {d} and pts= {n}: {stop2 -start2}')

    
    

if __name__ == '__main__':
	main()
