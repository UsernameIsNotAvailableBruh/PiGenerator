import threading, multiprocessing
from decimal import *

getcontext().prec = 40
a = 1
x = 0
sum = Decimal(0)
while True:
    sum += Decimal(a*4)/Decimal(x+1)
    a *= -1
    x+=2
    if x%10000000==0:
        print(sum)
