# -*- coding: utf-8 -*-
"""py-mms init

 PY-MMS : Main Package Init
 ==========================

 Copyright 2020 MET Norway

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

from .pymms import PyMMS # noqa: E402

__package__ = "pymms"
__version__ = "0.0.1"

__all__ = ["PyMMS"]

# Initiating logging
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

logging.basicConfig(format=logFormat, style="{", level=logLevel)
logger = logging.getLogger(__name__)

# Initialise Config
_CONFIG.initConfig()
