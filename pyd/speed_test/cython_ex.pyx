# example.pyx

def count_to_ten_billion():
    cdef int c = 0
    cdef int i
    cdef int x
    for i in range(1, 10000000001):
        x = i * i
        c += 1
        pass  # No operation, just counting
    print(c)