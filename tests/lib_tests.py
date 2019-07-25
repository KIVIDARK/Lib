import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import test_lib_pkg


def test_true_name():
    assert test_lib_pkg.name == 'test_lib_pkg'


def test_false_name():
    assert test_lib_pkg.name != 'test_lib_name'
