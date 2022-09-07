import numpy as np
import math


#5 digit sums - 
# N - (1, 2, 3, 4)
# divided by factorial?



def number_of_sums(N, m, count=0):
    if m==2:
        for i in np.arange(1, N/2):
            count += 1
    else:
        return (N - m - 1) / (2 * m) * number_of_sums(N, m - 1, count=count)
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


if __name__=='__main__':
    eN = 50
    print(number_of_sums(eN, 3))
    print(brute_force_3(eN))
    print(number_of_sums(eN, 4))
    print(brute_force_4(eN))
    print(number_of_sums(eN, 5))
    print(brute_force_5(eN))