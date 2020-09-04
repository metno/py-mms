# -*- coding: utf-8 -*-
"""Core object tests.
"""

import pytest

from pymms import PyMMS

@pytest.mark.core
def testConfigInit():
    tObj = PyMMS()
    assert tObj.helloWorld()

@pytest.mark.core
def testGoInterface():
    tObj = PyMMS()
    assert tObj.goMMS.sayHello() == "Hello Python!"
    # assert False

@pytest.mark.core
def testProductEvent():
    tObj = PyMMS()
    assert tObj.goMMS.productEvent("A", "B", "C")
    # assert False
