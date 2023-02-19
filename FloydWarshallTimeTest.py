import time
import subprocess
import FloydWarshallIterative
import FloydWarshallRecursive

# The following code bloc will calculate the time taken
# to execute the iterative version of the algorithm.

time_StartIterative = time.time()
subprocess.call(['python', 'FloydWarshallIterative.py'])
time_EndIterative = time.time()
print("Iterative Code time taken: ", time_EndIterative - time_StartIterative)

# The following code bloc will calculate the time taken
# to execute the recursive version of the algorithm.

time_StartRecursive = time.time()
subprocess.call(['python', 'FloydWarshallRecursive.py'])
time_EndRecursive = time.time()
print("Recursive Code time taken: ", time_EndRecursive - time_StartRecursive)
