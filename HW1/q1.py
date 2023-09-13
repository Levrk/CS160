
import timeit

def binSearchAux (list, element, left, right):
    # helper function to limit redundant arguments in original function call
    if not list:
        #if the list is empty
        return -1
    if (left < right) :
        #if there is still elements to be evaluated
        middle = (left + right) // 2
        #identify the mid point
        if (list[middle] == element):
            #item has been found
            return middle
        elif (list[middle] > element):
            #item is in lower half of list
            return binSearchAux (list, element, left, middle)
        elif (list[middle] < element):
            #item is in upper half of list
            return binSearchAux (list, element, middle+1, right)
    #item has not been found
    return -1

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
t2 = [j for j in range(1, 5000001)]
t3 = [k for k in range(1, 10000001)]



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



print(f"execution time for 100 function calls with a list of length:")

time1 = timeit.timeit(lambda: binSearch(t1, 0), number=100)
print(f"10: {time1:.6f} seconds")


time2 = timeit.timeit(lambda: binSearch(t2, 0), number=100)
print(f"5000000: {time2:.6f} seconds")

time3 = timeit.timeit(lambda: binSearch(t3, 0), number=100)
print(f"10000000: {time3:.6f} seconds")

"""
Sample results of time complexity testing:

execution time for 100 function calls with a list of length:
10: 0.000163 seconds
5000000: 0.000897 seconds
10000000: 0.001112 seconds

These results align with the expected outcome. The function binSearch should be executed in log time, 
meaning results will grow at a slower rate as the size of the input increases. Our results indicate
that the functions execution time increased by 5.5 times between inputs of size 10 and 5 million. 
The growth then increased by a factor of only 1.2 between the input of size 5 million and ten million. 
This aligns with our expectations because it shows that the functions time complexity grows quickly at first,
but eventually slows down with larger inputs.

"""

