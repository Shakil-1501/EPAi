import pytest , os , session4 , inspect , re , random
from decimal import Decimal
import math
import cmath

README_CONTENT_CHECK_FOR = ['__and__' ,
                            '__or__',
                            '__repr__',
                            '__str__',
                            '__add__',
                            '__eq__',
                            '__float__',
                            '__ge__',
                            '__gt__',
                            '__invertsign__',
                            '__le__',
                            '__lt__',
                            '__mul__',
                            '__sqrt__',
                            '__bool__'
                            ]


#1
def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


#2
def test_readme_words_counts():
    readme = open('README.md','r')
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100 , "Kindly define README properly"


#3
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


#4
def test_readme_for_formatting():
    readme = open('README.md','r')
    content = readme.read()
    readme.close()
    assert content.count('#') >= 5 , "Kindly format the README.md"


#5
def test_identation():
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert re.search('[a-zA-Z#@\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines" 


#6
def test_funcation_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction )
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


#7
def test_repr():
    a = random.choice([-1,0,1])
    q = session4.Qualean(a)
    assert 'Object at' not in q.__repr__() , "Kindly return meaningful message from __repr__"


#8
def test_str():
    a = random.choice([-1,0,1])
    q = session4.Qualean(a)
    assert 'Object at' not in q.__str__() , "Kindly return meaningful message from __str__"



#9
def test_lt_check():
    q1 = session4.Qualean(random.choice([-1 , 0 , 1]))
    q2 = session4.Qualean(random.choice([-1 , 0 , 1]))
    assert type(q1.__lt__(q2)) is bool


#10
def test_mul_check():
    q1 = session4.Qualean(random.choice([-1 , 0 , 1]))
    q2 = session4.Qualean(random.choice([-1 , 0 , 1]))
    assert q1.__mul__(q2) == q1*q2


#11
def test_add_check():
    a = session4.Qualean(random.choice([-1 , 0 , 1]))
    b = session4.Qualean(random.choice([-1 , 0 , 1]))
    assert a.__add__(b)==a+b


#12
def test_and_check():
    a = session4.Qualean(random.choice([-1 , 0 , 1]))
    b = session4.Qualean(random.choice([-1 , 0 , 1]))
    assert a.__and__(b)==float(a and b)


#13
def test_or_check():
    a = session4.Qualean(random.choice([-1 , 0 , 1]))
    b = session4.Qualean(random.choice([-1 , 0 , 1]))
    assert a.__or__(b) == float(a or b)


#14
def test_bool_check():
    a = session4.Qualean(random.choice([-1 , 0 , 1]))
    #b = session4.Qualean(random.choice([-1 , 0 , 1]))
    assert a.__bool__() == bool(a)


#15
def test_float_check():
    a = session4.Qualean(random.choice([-1 , 0 , 1]))
    #b = session4.Qualean(random.choice([-1 , 0 , 1]))
    assert a.__float__() == float(a)


#16
def test_gt_check():
    q1 = session4.Qualean(random.choice([-1 , 0 , 1]))
    q2 = session4.Qualean(random.choice([-1 , 0 , 1]))
    assert type(q1.__gt__(q2)) is bool


#17
def test_le_check():
    q1 = session4.Qualean(random.choice([-1 , 0 , 1]))
    q2 = session4.Qualean(random.choice([-1 , 0 , 1]))
    assert type(q1.__le__(q2)) is bool


#18
def test_ge_check():
    q1 = session4.Qualean(random.choice([-1 , 0 , 1]))
    q2 = session4.Qualean(random.choice([-1 , 0 , 1]))
    assert type(q1.__ge__(q2)) is bool


#19
def test_eq_check():
    q1 = session4.Qualean(random.choice([-1 , 0 , 1]))
    q2 = session4.Qualean(random.choice([-1 , 0 , 1]))
    assert type(q1.__eq__(q2)) is bool


#20
def test_sqrt_check():
    a = session4.Qualean(random.choice([-1 , 0 , 1]))
    #b = session4.Qualean(random.choice([-1 , 0 , 1]))
    assert a.__sqrt__() == cmath.sqrt(a)


#21 
def test_notimplementederror_check():
    with pytest.raises(NotImplementedError):
        session4.Qualean(random.choice([-1 , 0 , 1])).__le__('TSAI') 
        session4.Qualean(random.choice([-1 , 0 , 1])).__lt__('TSAI')
        session4.Qualean(random.choice([-1 , 0 , 1])).__gt__('TSAI')
        session4.Qualean(random.choice([-1 , 0 , 1])).__ge__('TSAI')



#22
def test_function_exist_check():
    a = session4.Qualean(random.choice([-1 , 0 , 1]))
    b = session4.Qualean(random.choice([-1 , 0 , 1]))
    assert a.__lt__(b) , "__lt__ is not implementated"
    assert a.__le__(b) , "__le__ is not implementated"
    assert a.__gt__(b) , "__gt__ is not implemented"
    assert a.__ge__(b) , "__ge__ is not implementated"






'''
def test_sqrtcheck_with_Decimal():
    a = random.choice([-1,0,1])
    q = session4.Qualean(a)
    assert q.__sqrt__() == Decimal(a).sqrt() , "session4.Qualean.__sqrt__(a) == Decimal(a).sqrt() returns different value"
'''

















'''
#9 Less than and equals to
def test_function_exist_check():
    a = random.uniform(-1,1)
    assert session4.Qualean.__lt__(a) , "__lt__ is not implementated"
    assert session4.Qualean.__le__(a) , "__le__ is not implementated"
    assert session4.Qualean__eq__(a) , "__eq__ is not implemented"
    assert session4.Qualean__ge__(a) , "__ge__ is not implementated"
    assert session4.Qualean.__gt__(a) , " __gt__ is not implementated"
    assert session4.Qualean.__or__() , "__or__ is not implemented"
    assert session4.Qualean.__bool_._() , "__bool__ is not implementated"
    assert session4.Qualean.__float__(a) , "__float__ is not implementated"
    assert session4.Qualean.__add__(a) , "__add__ is not implementated"
    assert session4.Qualean.__mul__(a) , "__mul__ is not implemented"
    assert session4.Qualean.__and__(a) , "__and__ is not implemented"
#10 NotImplementedError Check 
def test_notimplementederror_check():
    with pytest.raises(NotImplementedError):
        session4.Qualean.__le__('TSAI') 
        session4.Qualean.__lt__('TSAI')
        session4.Qualean.__gt__('TSAI')
        session4.Qualean.__ge__('TSAI')
        session4.Qualean.__eq__('TSAI')
        session4.Qualean.__or__('TSAI')
        session4.Qualean.__bool__('TSAI')
        session4.Qualean.__float__('TSAI')
        session4.Qualean.__add__('TSAI')
        session4.Qualean.__sqrt__('TSAI')
        session4.Qualean.__mul__('TSAI')
        session4.Qualean.__and__('TSAI')
#11 Decimal sqrt check with class Qualean
def test_sqrtcheck_with_Decimal():
    a = random.uniform(-1,1)
    q = session4.Qualean(a)
    assert q.__sqrt__() == Decimal(a).sqrt() , "session4.Qualean.__sqrt__(a) == Decimal(a).sqrt() returns different value"
#12'''
