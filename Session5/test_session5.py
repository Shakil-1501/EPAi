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
    assert q1=='please select correct scale'


def test_valid_temperature_range_and_scale():
    q1=session5.temp_convertor(-5,temp_given_in = 'd')
    assert q1=='please select valid range and correct scale'