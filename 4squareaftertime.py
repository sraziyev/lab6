import time
import math
number = float(input())
delay = int(input())
time.sleep(delay / 1000)
answer = math.sqrt(number)
print(f"Square root of {number} after {delay} milliseconds is {answer}")
