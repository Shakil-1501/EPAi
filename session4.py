from typing import List
import time
import sys
import weakref
import random
import math
import cmath

class Qualean:

    def __init__(self,choice):
        self.choice = choice
        self.k = round(choice*(random.uniform(-1,1)),10)

    def __str__(self):
        return 'Qualean: choice={0}, k={1}'.format(self.choice, self.k)


    def __repr__(self):
        return 'Qualean({0}, {1})'.format(self.choice,self.k)

    def __lt__(self, other):
        if isinstance(other, Qualean):
            return self.k < other.k
        else:
            print("I was called")
            raise NotImplementedError


    def __eq__(self,other):
        if  isinstance(other,Qualean):
            return self.k==other.k 
        else:
            return False


    def __le__(self,other):
        if isinstance(other,Qualean):
            return self.k <=other.k
        else:
            raise NotImplementedError

    def __gt__(self,other):
        if isinstance(other,Qualean):
            return self.k > other.k
        else:
            raise NotImplementedError

    def __ge__(self,other):
        if isinstance(other,Qualean):
            return self.k >=other.k
        else:
            raise NotImplementedError

    def __add__(self,other):
        if isinstance(other,Qualean):
            total=self.k+other.k
            return total
        else:
            raise NotImplementedError

    def __sqrt__(self):
        if isinstance(self,Qualean):
            total=cmath.sqrt(self.k)
            return total
        else:
            raise NotImplementedError

    def __mul__(self,other):
        if isinstance(other,Qualean):
            total=self.k*other.k
            return total
        else:
            raise NotImplementedError

    def __and__(self,other):
        if isinstance(other,Qualean):
            return self.k and other.k
        else:
            raise NotImplementedError

    def __or__(self,other):
        if isinstance(other,Qualean):
            return self.k or other.k
        else:
            raise NotImplementedError

    def __bool__(self):
        if isinstance(self,Qualean):
            return bool(self.k)
        else:
            raise NotImplementedError

    def __float__(self):
        if isinstance(self,Qualean):
            return float(self.k)
        else:
            raise NotImplementedError
'''
    def __invertsign__(self,other):
        if isinstance(other,Qualean):
            return self.k and other.k
        else:
            raise NotImplementedError
'''