# -*- coding: utf-8 -*-
"""py-mms go wrapper class

 PY-MMS : Wrapper Class for GO-MMS
 ==================================

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

import ctypes
import logging

from os import path

from . import _CONFIG

logger = logging.getLogger(__name__)

class GoMMS():
    """Main wrapper class for the Go library.
    """

    LIB_NAME = "libdummy.so"

    def __init__(self):

        self.goLib = ctypes.CDLL(path.join(_CONFIG.libPath, self.LIB_NAME))
        logger.debug("Linked library '%s'" % self.LIB_NAME)

        return

    def doubleIt(self, intVal):
        return self.goLib.DoubleIt(intVal)

# END Class GoMMS
