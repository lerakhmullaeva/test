import pytest 
from additional import my_string, word, filter_strings, add, param

def test_my_string():
    assert my_string("I'm tired of learning Python") is True

def test_my_string_2():
    assert my_string("short") is False

def test_word():
    assert word('Hummer') is True

def test_filter_strings():
    data = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
    
    expected_result = ['1', '2', 'False', '6', 'Python', 'Lorem Ipsum']

    assert filter_strings(data) ==  expected_result


# @pytest.mark.smoke
# def test_add():
#     result = add(3, 7)
#     assert result == 10

@pytest.mark.parametrize("a, b, expected_result",
        [
             (1, 1, 2),
             ('1', '1', '11'),
             (True, False, False)
        ])
def test_param_parametrize(a, b, expected_result):
    assert param(a, b) == expected_result

# @pytest.mark.skip - ignores test
# @pytest.mark.skipif - ignores with a condition
# @pytest.mark.xfail - expected fail
# @pytest.mark.your_mark
# @pytest.parametrize
# @pytest.fixture