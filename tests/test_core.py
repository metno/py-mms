# -*- coding: utf-8 -*-
"""Core object tests.
"""

import pytest

from pymms import PyMMS

@pytest.mark.core
def testConfigInit(goLib):
    assert goLib
    tObj = PyMMS()
    assert tObj.helloWorld()

@pytest.mark.core
def testDummyGoInterface(goLib):
    assert goLib
    tObj = PyMMS()
    assert tObj.goMMS.doubleIt(21) == 42
