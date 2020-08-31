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

import json
import ctypes
import logging

from os import path
from random import randint

from . import _CONFIG

logger = logging.getLogger(__name__)

class GoMMS():
    """Main wrapper class for the Go library.
    """

    LIB_NAME = "libgomms.so"

    def __init__(self):

        self.goLib = ctypes.CDLL(path.join(_CONFIG.libPath, self.LIB_NAME))
        logger.debug("Linked library '%s'" % self.LIB_NAME)

        return

    def postEvent(self):
        """Post an event to the MMS client.
        """
        payLoad = {"A": 0}
        self.goLib.PyPostEvent.restype = ctypes.c_char_p
        retData = self.goLib.PyPostEvent(ctypes.c_char_p(json.dumps(payLoad).encode()))
        print("Python received message:")
        print(json.loads(retData.decode()))
        return True

    def sayHello(self):
        """Function to check that the interface to the go-mms client is
        working. Should always return the double of the value sent.
        """
        intVal = randint(1, 100)
        retVal = self.goLib.PyHello(intVal)
        isOk = retVal == 2*intVal
        if isOk:
            logger.debug("Testing go-mms interface: OK")
        else:
            logger.error("Testing go-mms interface: Failed")
        return isOk

# END Class GoMMS
