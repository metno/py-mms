# -*- coding: utf-8 -*-
"""Test Config
"""

import sys
import pytest
import shutil
from os import path, mkdir

sys.path.insert(1, path.abspath(path.join(path.dirname(__file__), path.pardir)))

@pytest.fixture(scope="session")
def nwTemp():
    """Creates a temp folder that is destroyed before a new test session
    is started. It's destroyed before, not after, so that the output can
    be checked in case of errors.
    """
    testDir = path.dirname(__file__)
    tempDir = path.join(testDir, "temp")
    if path.isdir(tempDir):
        shutil.rmtree(tempDir)
    if not path.isdir(tempDir):
        mkdir(tempDir)
    return tempDir

@pytest.fixture(scope="function")
def nwFuncTemp(nwTemp):
    """This ficture creates a folder within the temp folder that is
    destroyed after the each test using it is finished.
    """
    funcDir = path.join(nwTemp, "ftemp")
    if path.isdir(funcDir):
        shutil.rmtree(funcDir)
    if not path.isdir(funcDir):
        mkdir(funcDir)
    yield funcDir
    if path.isdir(funcDir):
        shutil.rmtree(funcDir)
    return
