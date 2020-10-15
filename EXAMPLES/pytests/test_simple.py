#!/usr/bin/env python
import pytest

def test_two_plus_two_equals_four():  # <1>
    print("Hi MOM!")
    assert 2 + 2 == 4, "2 + 2 is not 4"   #  <2>


class TestSomeThings:

    def test_3_cubed_is_27(self):
        assert 3 ** 3 == 27, "3 cubed is not 81"

    def test_floats(self):
        assert 10 / 3 == pytest.approx(3.333, .001)

