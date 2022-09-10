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


