import pytest


def test_set_creation():
    created_set = {"a", "b", "c"}
    assert created_set == {"a", "b", "c"}


def test_set_add():
    initial_set = {"a", "b"}
    initial_set.add("c")
    assert initial_set == {"a", "b", "c"}


def test_set_remove_twice():
    initial_set = {"a", "b"}
    initial_set.add("c")
    
    try:
        initial_set.remove("c")
        initial_set.remove("c")
    except KeyError:
        print('element already removed')

    assert initial_set == {"a", "b"}


@pytest.mark.parametrize("test_input,expected", [("2", 2.0), (5, 5.0), (20.0, 20.0)])
def test_float_convert(test_input, expected):
    converted_to_float = float(test_input)
    assert isinstance(converted_to_float, float) and converted_to_float == expected


def test_float_comparison():
    calculated_float = 1/2
    const_float = 0.5
    assert calculated_float == const_float


