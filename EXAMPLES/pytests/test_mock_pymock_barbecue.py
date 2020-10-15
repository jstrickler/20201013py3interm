#!/usr/bin/env python
import pytest  # <1>
import hamlib  # <2>

class Barbecue():  # <3>

    def doit(self):  # <4>
        return hamlib.mydecorator(8)

def test_barbecue_doit_calls_ham(mocker):   # <5>
    mocker.patch('hamlib.ham')  # <6>
    b = Barbecue()
    result = b.doit()
    hamlib.mydecorator.assert_called_once_with(8)  # <9>

if __name__ == '__main__':
    pytest.main([__file__, '-s'])   # <10>
