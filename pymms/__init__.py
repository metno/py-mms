# -*- coding: utf-8 -*-
"""
PY-MMS : Main Package Init
==========================

Copyright 2020–2021 MET Norway

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
import logging

from .config import Config

# Create Config object before initialising any other classes as they
# depend on the Config object.
_CONFIG = Config()

from .productevent import ProductEvent # noqa: E402
from .exceptions import MMSError # noqa: E402

__package__ = "pymms"
__version__ = "0.0.1"

__all__ = ["ProductEvent", "MMSError"]

# Initiating logging
def _initLogging(logObj):
    strLevel = os.environ.get("PYMMS_LOGLEVEL", "INFO")
    if hasattr(logging, strLevel):
        logLevel = getattr(logging, strLevel)
    else:
        print("Invalid logging level '%s' in environment variable PYMMS_LOGLEVEL" % strLevel)
        logLevel = logging.INFO

    if logLevel < logging.INFO:
        logFormat = "[{asctime:s}] {levelname:8s} {message:}"
    else:
        logFormat = "{levelname:8s} {message:}"

    logFmt = logging.Formatter(fmt=logFormat, style="{")

    cHandle = logging.StreamHandler()
    cHandle.setLevel(logLevel)
    cHandle.setFormatter(logFmt)

    logObj.setLevel(logLevel)
    logObj.addHandler(cHandle)

    return

# Logging Setup
logger = logging.getLogger(__name__)
_initLogging(logger)

# Initialise Config
_CONFIG.initConfig()
