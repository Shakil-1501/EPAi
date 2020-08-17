from typing import List
import time
import sys
import weakref
import random
from math import tan, pi


def temp_convertor(temp,temp_given_in = 'f'):
    if temp_given_in =='f' and temp>=0:
        t= (temp-32) * 5/9
    elif temp_given_in =='c' and temp>=0:
        t=(temp*(9/5))+32
    elif temp<0 and temp_given_in not in ('c','f'):
        t="please select valid range and correct scale"  
    elif temp<0:
        t="please enter the valid range"
    elif temp_given_in not in ('c','f'):
        t="please select correct scale"
    return t


def polygon_area(side_length,side=3):
    if side_length>0 and 3<=side<=6:
        area=round(side * (side_length ** 2) / (4 * tan(pi /side)),4)
    elif side_length<=0 and (side<3 or side>6):
        area="please enter valid side and side_length"
    elif side_length<=0:
        area="please enter valid side_length"
    elif side<3 or side>6:
        area="please enter side in range 3 to 6"
    return area
 

def squared_power_list(number,start=0,end=5):
    a=[]
    if number>0 and start<end:
        for i in range(start,end+1):
            a.append(number**i)
    elif number<0 and start>end:
        a.append("select valid number and proper start and end")
    elif start>end:
        a.append("start value should be less than end")
    elif number<0:
        a.append("select valid number")
    return a 


def speed_convertor(speedk,dist='km', time='min'):
    if speedk>0 and dist=='m' and time=='s':
        a=round(speedk/3.6,2)
    if speedk>0 and dist=='yrd' and time=='s':
        a=round(speedk*0.3038,2)
    if dist not in ('km','m','ft','yrd'):
        a='please enter the correct distance scale'
    if time not in ('ms','s','m','hr','day'):
        a='please enter the correct time scale'
    if speedk<0:
        a='speed must be positive'
    return a


def time_it(fn, *args, repetitons= 5, **kwargs):
    for i in range(repetitons):
        start=time.perf_counter()
        #print(start)
        #start=int(round(time.time() * 1000))
        #start=int(round(time.time() * 100000000))
        fn(*args,**kwargs)
        #end=time.perf_counter()
        #end=int(round(time.time() * 100000000))
        #print(end)
    end=time.perf_counter()
    #print(end)
    time_taken=(end-start)/repetitons
    return time_taken


