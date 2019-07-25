import test_lib_pkg


def test_true_name():
    assert test_lib_pkg.name == 'test_lib_pkg'


def test_false_name():
    assert test_lib_pkg.name != 'test_lib_name'
