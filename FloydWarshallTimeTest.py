import time
import subprocess
import FloydWarshallIterative
import FloydWarshallRecursive

time_StartIterative = time.time()
subprocess.call(['python', 'import FloydWarshallIterative.py'])
time_EndIterative = time.time()
print("Iterative Code time taken: ", time_EndIterative - time_StartIterative)

time_StartRecursive = time.time()
subprocess.call(['python', 'FloydWarshallRecursive.py'])
time_EndRecursive = time.time()
print("Recursive Code time taken: ", time_EndRecursive - time_StartRecursive)
