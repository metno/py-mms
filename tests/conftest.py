# -*- coding: utf-8 -*-
"""Test Config
"""

import os
import sys
import pytest

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

@pytest.fixture(scope="session")
def goLib():
    libDir = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), os.path.pardir, "pymms", "lib"
        )
    )
    if not os.path.isdir(libDir):
        return False

    currDir = os.getcwd()
    os.chdir(libDir)
    exStatus = os.system("%s/makeLib.sh" % libDir)
    os.chdir(currDir)

    return exStatus == 0
