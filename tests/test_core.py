# -*- coding: utf-8 -*-
"""Core object tests.
"""

import os
import pytest
import logging

from pymms import _initLogging

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
