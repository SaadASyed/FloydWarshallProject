import sys
import itertools
import numpy as mtr

# Declaring initial variables. no_path is to signify no possible
# routes between respective nodes. Given that this is an equal sides
# matrix, we use the vertices variable to decipher the number of
# items in each list. Mid variable will be used in the recursive code.
no_path = sys.maxsize
graph = [[0, 7, no_path, 8],
         [no_path, 0, 5, no_path],
         [no_path, no_path, 0, 2],
         [no_path, no_path, no_path, 0]]
vertices = len(graph[0])
mid = 0

# This will be the main floyd function which loops through the
# start and end nodes.


def mainfloyd(matrix):
    for start in range(vertices):
        for end in range(vertices):
            # if start and end nodes are the same, then distance will be 0.
            if start == end:
                matrix[start][end] = 0
                continue
            # if start and end nodes are not same, we will call another function.
            else:
                matrix[start][end] = floydrecursive(start, mid, end, matrix)
    answer(matrix)
    return matrix

# This is the main recursive function which calls on itself
# in finding the shortest paths between the nodes.


def floydrecursive(start, mid, end, matrix):
    # given that the list count begins from 0, we run through the
    # possible paths with the middle node starting from 0 up to 3.
    while mid <= 3:
        matrix[start][end] = min(
            matrix[start][end], matrix[start][mid] + matrix[mid][end])
        mid = mid + 1
        # The following is a simple check to see if all middle nodes have
        # been explored. If it has and 3 has been reached, we get the shortest
        # path. Otherwise the function recursively calls itself to begin the
        # next iteration.
        if mid == 3:
            return matrix[start][end]
        else:
            floydrecursive(start, mid, end, matrix)

# creating a function to print final graph in a matrix format.


def answer(matrix):
    # I have used x and y as coordinates along the graph and
    # anywhere where we have the no_path variable, I have included
    # the first 5 numbers, otherwise kept the distance the same.
    for x in range(vertices):
        for y in range(vertices):
            if matrix[x][y] == no_path:
                matrix[x][y] = int(str(no_path)[0:5])
            else:
                matrix[x][y] = matrix[x][y]
     # The array method from numpy library is used to print in matrix form.
    print(mtr.array(matrix))


mainfloyd(graph)
