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

# This will be the main floyd function loops through the start and
# end nodes.


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

    return matrix
