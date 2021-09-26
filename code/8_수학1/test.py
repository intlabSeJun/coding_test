
import time

s = time.time()

for i in range(1000000):
    print(i)
e = time.time()
print(e-s)