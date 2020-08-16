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
        area=side * (side_length ** 2) / (4 * tan(pi /side))
    elif side_length<=0 and (side<3 or side>6):
        area="please enter valid side and side_length"
    elif side_length<=0:
        area="please enter valid side_length"
    elif side<3 or side>6:
        area="please enter side in range 1 to 6"
        
    return area