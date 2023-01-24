import pytest 

from average_calculator.calc import rounded_average

# @pytest.mark.skip
def test_average_of_two_numbers_is_properly_computed():
    actual = rounded_average([4, 6])
    assert actual == 5
    # pass

# @pytest.mark.skip
def test_average_of_empty_list_raises_ValueError():
    with pytest.raises(ZeroDivisionError):
        rounded_average([])
    # assert act
    # Delete the skip and write the test here!
    # Hint: use pytest.raises
    # pass
