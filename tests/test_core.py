# -*- coding: utf-8 -*-
"""Core object tests.
"""

import pytest

from pymms import PyMMS

@pytest.mark.core
def testConfigInit(nwTemp):
    tObj = PyMMS()
    assert tObj.helloWorld()