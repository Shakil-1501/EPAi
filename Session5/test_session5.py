import pytest , os , session5 , inspect , re , random
from decimal import Decimal
import math
import cmath


def test_temp_convertor_to_c():
    q1=session5.temp_convertor(212,temp_given_in = 'f')
    assert q1==100, 'Wrong value fetched'


def test_temp_convertor_to_f():
    q1=session5.temp_convertor(100,temp_given_in = 'c')
    assert q1==212, 'Wrong value fetched'


def test_valid_temperature_scale():
    q1=session5.temp_convertor(100,temp_given_in = 'd')
    assert q1=='please select correct scale'


def test_valid_temperature_range():
    q1=session5.temp_convertor(-5,temp_given_in = 'c')
    assert q1=='please enter the valid range'


def test_valid_temperature_range_and_scale():
    q1=session5.temp_convertor(-5,temp_given_in = 'd')
    assert q1=='please select valid range and correct scale'


def test_polygon_area():
    q1=session5.polygon_area(3,side=4)
    assert q1==9.0,'Wrong area calculated'


def test_polygon_side_length():
    q1=session5.polygon_area(-2,side=4)
    assert q1=='please enter valid side_length'


def test_polygon_side():
    q1=session5.polygon_area(3,side=1)
    assert q1=='please enter side in range 3 to 6'

def test_valid_side_and_length():
    q1=session5.polygon_area(-2,side=1)
    assert q1=='please enter valid side and side_length'


