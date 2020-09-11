# -*- coding: utf-8 -*-
"""Core object tests.
"""

import os
import pytest
import logging

from pymms import PyMMS, _initLogging

@pytest.mark.core
def testInitLogging():
    os.environ["PYMMS_LOGLEVEL"] = "DEBUG"
    logger = logging.getLogger(__name__)
    _initLogging(logger)
    assert logger.getEffectiveLevel() == logging.DEBUG

    os.environ["PYMMS_LOGLEVEL"] = "INVALID"
    logger = logging.getLogger(__name__)
    _initLogging(logger)
    assert logger.getEffectiveLevel() == logging.INFO

@pytest.mark.core
def testConfigInit():
    tObj = PyMMS()
    assert tObj.helloWorld()

@pytest.mark.core
def testGoInterface():
    tObj = PyMMS()
    assert tObj.goMMS.sayHello() == "Hello Python!"
    # assert False
