import math
import random

arr = []

for i in range(10):
    arr.insert(i, random.randint(0, 100))

for i in range(len(arr)):
    if (arr[i] % 2) == 0:
        print(f"Pari\t {arr[i]}")
    else:
        print(f"Dispari\t {arr[i]}")


