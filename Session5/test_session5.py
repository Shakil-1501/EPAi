import pytest , os , session5 , inspect , re , random
from decimal import Decimal
import math
import cmath

README_CONTENT_CHECK_FOR = ['temp_convertor']



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


def test_squared_power_list():
    q1=session5.squared_power_list(2,start=0,end=5)
    assert q1==[1, 2, 4, 8, 16, 32],'Wrong Result'


def test_speed_convertor():
    q1=session5.speed_convertor(100,dist='m', time='s')
    assert q1==27.78,'Wrong speed conversion'


def test_validity_speed():
    q1=session5.speed_convertor(-100,dist='m', time='s')
    assert q1=='speed must be positive'


def test_speed_yard_s():
    q1=session5.speed_convertor(100,dist='yrd', time='s')
    assert q1==30.38


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_funcation_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction )
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_identation():
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert re.search('[a-zA-Z#@\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines" 


def test_squared_valid_number():
    q1=session5.squared_power_list(-2,start=0,end=5)
    assert q1==["select valid number"]


def test_squared_start_end():
    q1=session5.squared_power_list(2,start=3,end=1)
    assert q1==["start value should be less than end"]


def test_squared_validity():
    q1=session5.squared_power_list(-2,start=5,end=1)
    assert q1==["select valid number and proper start and end"]


def test_print_function():
    a=print(1, 2, 3, sep='-', end= ' ***\n')
    assert bool(a)==False


def test_time_it_print():
    q1=session5.time_it(print, 1, 2, 3,repetitons=100 , sep='-', end= ' ***\n')
    assert type(q1) is float


def test_readme_words_counts():
    readme = open('README.md','r')
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100 , "Kindly define README properly"



def test_readme_proper_desscription():
    READMELOOKSGOOD = True
    readme = open('README.md','r')
    readme_words = readme.read().split()
    readme.close()
    for words in README_CONTENT_CHECK_FOR:
        if words not in readme_words:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True , "You have not defined all functions/classes in README.md"



def test_readme_for_formatting():
    readme = open('README.md','r')
    content = readme.read()
    readme.close()
    assert content.count('#') >= 5 , "Kindly format the README.md"


def test_dist_scale():
    q2=session5.speed_convertor(100,dist='z', time='s')
    assert q2=='please enter the correct distance scale'

def test_time_scale():
    q1=session5.speed_convertor(100,dist='m', time='k')
    assert q1=='please enter the correct time scale'
