# -*- coding: utf-8 -*-
"""Core object tests.
"""

import pytest

from pymms import PyMMS

@pytest.mark.core
def testConfigInit(ptTemp):
    tObj = PyMMS()
    assert tObj.helloWorld()
