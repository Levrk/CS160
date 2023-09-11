
import timeit

def binSearch (list, element):
    if not list:
        return False
    middle = (len(list) // 2) 
    if (list[middle] > element):
        return binSearch (list[:middle], element)
    elif (list[middle] < element):
        return binSearch (list[middle+1:], element)
    else:
        return True
    


l0 = [1,2,3,4,5]
l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [1,3,4,5,6,7,8,9,10]
l3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
l4 = [2,4,6,8,10,12,14,16,18,20]


assert(binSearch(l0, 2))
assert(not binSearch(l0, 11))
assert(binSearch(l0, 5))

assert(binSearch(l1, 2))
assert(not binSearch(l1, 11))
assert(binSearch(l1, 6))

assert(binSearch(l2, 4))
assert(not binSearch(l2, 2))
assert(not binSearch(l2, 0))

assert( binSearch(l3, 15))
assert(not binSearch(l3, 25))
assert(binSearch(l3, 11))

assert(not binSearch(l4, 1))
assert(not binSearch(l4, 13))
assert(binSearch(l4, 20))


t1 = [i for i in range(1, 101)]
t2 = [j for j in range(1, 10001)]
t3 = [k for k in range(1, 1000001)]

time1 = timeit.timeit(lambda: binSearch(t1, 0), number=1000)
print(f"Average execution time for list of length 100: {time1 / 1000:.6f} seconds")

time2 = timeit.timeit(lambda: binSearch(t2, 0), number=1000)
print(f"Average execution time for list of length 10000: {time2 / 1000:.6f} seconds")

time3 = timeit.timeit(lambda: binSearch(t3, 2334), number=1000)
print(f"Average execution time for list of length 1000000: {time3 / 1000:.6f} seconds")