
import timeit

def binSearchAux (list, element, left, right):
    # helper function to limit redundant arguments in original function call
    if not (left < right):
        #list is empty
        return -1
    else :
        #if there is still elements to be evaluated
        middle = (left + right) // 2
        #identify the mid point
        if (list[middle] == element):
            #item has been found
            return middle
        elif (list[middle] > element):
            #item is in lower half of list
            #use midpoint as the new right index
            return binSearchAux (list, element, left, middle)
        elif (list[middle] < element):
            #item is in upper half of list
            #use midpoint+1 as the new left index
            return binSearchAux (list, element, middle+1, right)


def binSearch (list, element):
    #calls helper function 
    return binSearchAux(list, element, 0, len(list))



#Test Data
l0 = [1,2,3,4,5]
l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [1,3,4,5,6,7,8,9,10]
l3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
l4 = [2,4,6,8,10,12,14,16,18,20]
l5 = []

t1 = [i for i in range(1, 11)]
t2 = [j for j in range(1, 250001)]
t3 = [k for k in range(1, 500001)]
t4 = [l for l in range(1, 750001)]
t5 = [m for m in range(1, 1000001)]



#Test Cases
assert(2 == binSearch(l0,3))
assert(1 == binSearch(l0, 2))
assert(-1 == binSearch(l0, 11))
assert(4 == binSearch(l0, 5))
assert(1 == binSearch(l1, 2))
assert(-1 == binSearch(l1, 11))
assert(5 == binSearch(l1, 6))
assert(2 == binSearch(l2, 4))
assert(-1 == binSearch(l2, 2))
assert(-1 == binSearch(l2, 0))
assert(14 == binSearch(l3, 15))
assert(-1 == binSearch(l3, 25))
assert(10 == binSearch(l3, 11))
assert(-1 == binSearch(l4, 1))
assert(-1 == binSearch(l4, 13))
assert(9 == binSearch(l4, 20))
assert(-1 == binSearch(l5, 20))




print(f"execution time for 100 function calls with a list of length:")

time1 = timeit.timeit(lambda: binSearch(t1, 0), number=100)
print(f"10: {time1:.6f} seconds")


time2 = timeit.timeit(lambda: binSearch(t2, 0), number=100)
print(f"250000: {time2:.6f} seconds")

time3 = timeit.timeit(lambda: binSearch(t3, 0), number=100)
print(f"500000: {time3:.6f} seconds")

time4 = timeit.timeit(lambda: binSearch(t4, 0), number=100)
print(f"750000: {time4:.6f} seconds")

time5 = timeit.timeit(lambda: binSearch(t5, 0), number=100)
print(f"1000000: {time5:.6f} seconds")

"""
Sample results of time complexity testing:

10: 0.000100 seconds
2500000: 0.000392 seconds
5000000: 0.000443 seconds
7500000: 0.000592 seconds
10000000: 0.000675 seconds

These results align with the expected outcome. The function binSearch should be executed in log time, 
meaning results will grow at a slower rate as the size of the input increases. Our results indicate
that the functions execution time increased by 4.43 times between inputs of size 10 and .5 million. 
The growth then increased by a factor of only 1.52 between the input of size .5 million and 1 million. 
This aligns with our expectations because it shows that the functions time complexity grows quickly at first,
but eventually slows down with larger inputs. We can see this even more clearly by plotting the points generated
by this time complexity analysis on a graph along side a logarithmic equation y = .0001log_{2.7}(x)-.001. 
We can see from the graph that the time taken to execute these function calls increases logarithmically,
which is what we expect.

"""

