import my_funcs2
import pytest
import sys


@pytest.mark.skipif(sys.version_info < (3, 3), reason="do not run number add test")
def test_add():
    assert my_funcs2.add(7, 3) == 10
    assert my_funcs2.add(7) == 9
    print(my_funcs2.add(7, 3), '-----------------------------------')


@pytest.mark.number
def test_product():
    assert my_funcs2.product(5, 5) == 25
    assert my_funcs2.product(5) == 10


@pytest.mark.string
def test_add_strings():
    result = my_funcs2.add('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Hello' in result


@pytest.mark.skip(reason="do not run number product test")
def test_product_strings():
    assert my_funcs2.product('Hello ', 3) == 'Hello Hello Hello '
    result = my_funcs2.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result
    
# multiple test cases
@pytest.mark.parametrize("test_input,expected", [(1, 2), (3, 4), (5, 6)])
def test_add_parametrize(test_input, expected):
    assert my_funcs2.add(test_input, 1) == expected