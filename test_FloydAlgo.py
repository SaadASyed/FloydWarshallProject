# Importing, amongst others, the unittest module which is in
# the standard library. We also import the FloydAlgoRecursive
# module as we will be testing the code in this file.
import sys
import itertools
import numpy as mtr
import unittest
import FloydWarshallRecursive
no_path = sys.maxsize

# In order to create the test case, we need to create a class.
# I have called this TestFloydAlgo.


class TestFloydAlgo(unittest.TestCase):
    # This is the main testing code. It needs to start with
    # "test_". In our test, "self" will be the only argument.
    def test_RunAlgo(self):
        # Defining the matrix variable which is the default graph.
        matrix = [[0, 7, no_path, 8],
                  [no_path, 0, 5, no_path],
                  [no_path, no_path, 0, 2],
                  [no_path, no_path, no_path, 0]]
        # Defining a variable for the first 5 integers of no_path
        # variable so that we can use this in the correct matrix.
        short_np = int(str(no_path)[0:5])
        # Defining the correct matrix to test for accuracy.
        CorrectMatrix = [[0, 7, 12, 8],
                         [short_np, 0, 5, 7],
                         [short_np, short_np, 0, 2],
                         [short_np, short_np, short_np, 0]]
        # calling the main FloydAlgo function from the Main module.
        answer1 = FloydWarshallRecursive.mainfloyd(matrix)
        # next we use the assertEqual method to ensure that the code
        # returns/equals the CorrectMatrix variable defined earlier.
        self.assertEqual(answer1, CorrectMatrix)

    def test_IncorrectAnswer(self):
        # This is a test to see if the code works in case the wrong
        # default answer is being checked against. The main block of
        # the code is the same as the first test, only the CorrectMatrix
        # variable is being updated.
        matrix = [[0, 7, no_path, 8],
                  [no_path, 0, 5, no_path],
                  [no_path, no_path, 0, 2],
                  [no_path, no_path, no_path, 0]]

        short_np = int(str(no_path)[0:5])

        CorrectMatrix = [[0, 7, 12, 8],
                         [short_np, 0, 5, 2],
                         [short_np, short_np, 0, 2],
                         [short_np, short_np, short_np, 0]]

        answer1 = FloydWarshallRecursive.mainfloyd(matrix)
        self.assertEqual(answer1, CorrectMatrix)

    def test_UpdatedMatrix(self):
        # This is a test to see if the code works in case the wrong
        # default answer is being checked against. The main block of
        # the code is the same as the first test, only the Matrix
        # being updated.
        matrix = [[0, 9, no_path, 8],
                  [no_path, 0, 5, no_path],
                  [no_path, no_path, 0, 2],
                  [no_path, no_path, no_path, 0]]

        short_np = int(str(no_path)[0:5])

        CorrectMatrix = [[0, 7, 12, 8],
                         [short_np, 0, 5, 7],
                         [short_np, short_np, 0, 2],
                         [short_np, short_np, short_np, 0]]

        answer1 = FloydWarshallRecursive.mainfloyd(matrix)

        self.assertEqual(answer1, CorrectMatrix)


if __name__ == '__main__':
    matrix = [[0, 7, no_path, 8],
              [no_path, 0, 5, no_path],
              [no_path, no_path, 0, 2],
              [no_path, no_path, no_path, 0]]
    unittest.main()
