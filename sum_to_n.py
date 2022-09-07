from enum import unique
import numpy as np
import pandas as pd

import itertools

#5 digit sums - 
# N - (1, 2, 3, 4)
# divided by factorial?






def number_of_sums(N, m, count=0):
    if m==2:
        for i in np.arange(1, N/2):
            count += 1
    else:      
        count = number_of_sums(N - m, m - 1, count=count)
        return (N - m) / (m) * number_of_sums(N - m, m - 1, count=count) #this only works for 3..
    return count


def brute_force_3(N):
    count = 0
    list_of_vals = []
    for i in np.arange(1, N+1):
        for j in np.arange(1, N - i + 1):
            for k in np.arange(1, N - (i + j) + 1):
                val = np.array([i, j, k])
                val.sort()
                #print(i,j,k, val, list_of_vals)
                if i + j + k == N and i!=j and i!=k and j!=k:
#                    print(i,j,k, val, list_of_vals)
                    if not check_in_list(val, list_of_vals):
 #                       print('added', i,j,k)
                        list_of_vals.append(val)
                        count += 1
    #print(list_of_vals)
    return count

def brute_force_4(N):
    count = 0
    list_of_vals = []
    for i in np.arange(1, N+1):
        for j in np.arange(1, N - i + 1):
            for k in np.arange(1, N - (i + j) + 1):
                for l in np.arange(1, N - (i + j + k) + 1):
                    val = np.array([i, j, k, l])
                    val.sort()
                    #print(i,j,k, val, list_of_vals)
                    if i + j + k + l== N and i!=j and i!=k and j!=k and l!=i and l!=j and l!=k:
    #                    print(i,j,k, val, list_of_vals)
                        if not check_in_list(val, list_of_vals):
    #                       print('added', i,j,k)
                            list_of_vals.append(val)
                            count += 1
    #print(list_of_vals)
    return count

def brute_force_5(N):
    count = 0
    list_of_vals = []
    for i in np.arange(1, N+1):
        for j in np.arange(1, N - i + 1):
            for k in np.arange(1, N - (i + j) + 1):
                for l in np.arange(1, N - (i + j + k) + 1):
                    for m in np.arange(1, N - (i + j + k + l) + 1):
                        val = np.array([i, j, k, l, m])
                        val.sort()
                        #print(i,j,k, val, list_of_vals)
                        if i + j + k + l + m == N and i!=j and i!=k and j!=k and l!=i and l!=j and l!=k and m!=i and m!=j and m!=k and m!=l:
        #                    print(i,j,k, val, list_of_vals)
                            if not check_in_list(val, list_of_vals):
        #                       print('added', i,j,k)
                                list_of_vals.append(val)
                                count += 1
    #print(list_of_vals)
    return count

def check_in_list(val, list_of_vals):
    check = False
    for lval in list_of_vals:
        if (val == lval).all():
            return True
    return check

def py_iter_combs(eN, m, exclude=None):
    comb_list = []
    combs_iter = itertools.combinations(np.arange(1, eN+1), m)
    for comb in combs_iter:
        if np.sum(comb)==eN and not exclude in comb:
            comb_list.append(comb)
    comb_list = pd.DataFrame(comb_list)
    return comb_list#len(comb_list)

def return_iter(eN, m):
    looping = True
    count = 1
    unique_list = [] #ensure each entry is always sorted..
    while looping:
        cur_list = [count]
        remainder = eN - count
        if remainder >= count: #ensure sorted
            cur_list = cur_list + [remainder]
        else:
            unique_list.append(cur_list)
            looping = False
        count += 1

#need to break problem into smaller 2 iter problems?
### Three iter problem

#eN = 10
# 1 - 
# then can choose two other items that sum to 9, but cannot use 1.

#2 - then can choose two other items that sum to 8, but cannot use 2

#etc.

def func(eN, m, starting_list=[]):
    #running_list = {}
    #running_list[count] = pd.DataFrame([])
    count = 1
    running_list = []
    looping = True
    while count < eN - m and looping:
        comb_list = py_iter_combs(eN - count, 2, exclude=count)
        comb_list.loc[:, -1] = count
        res = comb_list.values
        res.sort()
        for i in res.astype(str):
            comb_to_add = ','.join(i)
            if not comb_to_add in running_list:
                running_list.append(comb_to_add)
                #print(comb_to_add)
        count += 1
        #import ipdb;ipdb.set_trace()
        #print(comb_list)
    return running_list


if __name__=='__main__':
    eN = 200
    #print(number_of_sums(eN, 3))
    #print(brute_force_3(eN))
    #print(number_of_sums(eN, 4))
    #print(brute_force_4(eN))
    #print(number_of_sums(eN, 5))
    #print(brute_force_5(eN))
    from datetime import datetime

    print(f'en = {eN}')
    t0 = datetime.now()
    print(len(func(eN, 3)))
    t1 = datetime.now()
    print('func', t1-t0)
    
    t0 = datetime.now()
    print(len(py_iter_combs(eN, 3)))
    t1 = datetime.now()
    print('py_iter_combo', t1-t0)

    m = 1
    total_items = 0
    added_items = 9999
    #while total_items==0 or added_items!=0:
        #added_items = py_iter_combs(eN, m)
        #total_items += added_items
        #print(f'Slots: {m}, unique combinations: {added_items}, running total: {total_items}')
        #m += 1