# -*- coding: utf-8 -*-
"""py-mms product event

 PY-MMS : Product Event Class
 ============================

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

import logging

from .gomms import GoMMS

logger = logging.getLogger(__name__)

class ProductEvent():
    """Wrapper class for the go-mms product event.
    """

    def __init__(self, product="", productSlug="", productionHub=""):

        self._goMMS = GoMMS()

        # Event properties
        self._eventProduct = product
        self._eventProductSlug = productSlug
        self._eventProductionHub = productionHub

        return

    ##
    #  Getters
    ##

    @property
    def product(self):
        return self._eventProduct

    @property
    def productSlug(self):
        return self._eventProductSlug

    @property
    def productionHub(self):
        return self._eventProductionHub

    ##
    #  Setters
    ##

    @product.setter
    def product(self, value):
        if isinstance(value, str):
            self._eventProduct = value
        else:
            self._eventProduct = ""
            raise ValueError("ProductEvent.product must be a string")
        return

    @productSlug.setter
    def productSlug(self, value):
        if isinstance(value, str):
            self._eventProductSlug = value
        else:
            self._eventProductSlug = ""
            raise ValueError("ProductEvent.productSlug must be a string")
        return

    @productionHub.setter
    def productionHub(self, value):
        if isinstance(value, str):
            self._eventProductionHub = value
        else:
            self._eventProductionHub = ""
            raise ValueError("ProductEvent.productionHub must be a string")
        return

    ##
    #  Methods
    ##

    def send(self):
        """Bundle the event data and send to the GoMMS library. Returns
        a dictionary of the response from go-mms.
        """
        retData = self._goMMS.productEvent(
            product=self._eventProduct,
            productSlug=self._eventProductSlug,
            productionHub=self._eventProductionHub
        )
        return retData

# END Class ProductEvent
