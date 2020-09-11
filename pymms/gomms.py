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

from . import _CONFIG
from .exceptions import MMSError

logger = logging.getLogger(__name__)

class GoMMS():
    """Main wrapper class for the Go library.
    """

    LIB_NAME = "libmms.so"

    def __init__(self):

        self.goLib = ctypes.CDLL(path.join(_CONFIG.libPath, self.LIB_NAME))
        logger.debug("Linked library '%s'" % self.LIB_NAME)

        return

    def productEvent(self, product, productionHub, productLocation):
        """Post an event to the MMS client.
        """
        payLoad = json.dumps({
            "Product":         str(product),
            "ProductionHub":   str(productionHub),
            "ProductLocation": str(productLocation),
        })
        self.goLib.PyProductEvent.restype = ctypes.c_char_p
        retData = self.goLib.PyProductEvent(payLoad.encode()).decode()
        retDict = json.loads(retData)

        if "err" in retDict and "errmsg" in retDict:
            if retDict["err"]:
                errMsg = retDict["errmsg"].replace(": ", ":\n")
                raise MMSError("\n%s" % errMsg.strip())
        else:
            raise MMSError("Invalid return data from libmms.so")

        return retDict

    def sayHello(self):
        """Function to check that the interface to the go-mms client is
        working. Should always return the double of the value sent.
        """
        self.goLib.PySayHello.restype = ctypes.c_char_p
        retByte = self.goLib.PySayHello(b"Hello Go!")
        retString = retByte.decode()
        print("Go says: %s" % retString)
        return retString

# END Class GoMMS
