import math
import os
import random
import re
import sys


n = int(input())

if 1 <= n <= 100:
    if 2 < n < 5 :
        print("Not Weird")
    elif 6 < n < 20:
        print("Weird")
    elif n > 20 & n%2 == 0 :
        print("Not Weird")
    else:
        print("Weird")
