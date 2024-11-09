import threading, functools
from decimal import Decimal, getcontext
import time
import sys, os
#import winsound

#Calculate pi using Gregory-Leibniz Series

@functools.cache #trying to optimize, shaves a few milliseconds lol
def a4(a:bool):
    return Decimal(a*2-1)*4
a4(True) #put True in cache
a4(False) #put False in cache

Digits = int(input("How many digits of pi should be calculated?\n"))
print("Calculating...\nThe first number is the current approx., The second number is the iteration")
start = time.perf_counter()
checkiter = 5 #increase this if it gives the wrong result
PrecAdd = 20 #alternatively, increase/decrease this value (if the output seems "stuck")
#increasing the values would lead to longer processing times but more precision
#decreasing the values would lead to shorter processing times but less precision (more error prone)
getcontext().prec = Digits+PrecAdd
a = True
count = 0
x = 1
sum = Decimal(0)
CheckList = list(range(checkiter)) #check last checkiter iterations, if theyre all the same, assume pi to Digits digits has been calculated
while len(set(CheckList)) != 1:
    sum += a4(a)/Decimal(x)
    CheckList[(count)%checkiter] = str(sum)[:-PrecAdd]
    a = not a
    x+=2
    count +=1
    if count%10_000==0: #increase the number if you want the screen to "update" less, decrease to make it update more. 
        print(sum, count, end="\r")

print("  "*len(str(sum)), end="\r")
print(str(sum)[:-PrecAdd])
print(f"Done! in: {time.perf_counter()-start}")

#for x in range(100, 1000, 200):
#    winsound.Beep(x, 20)
#for x in range(1000, 100, -200):
#    winsound.Beep(x, 40)
#winsound.Beep(40, 40)