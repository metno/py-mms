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
import json

from urllib import request, error
from datetime import datetime, timedelta

from .exceptions import MMSError

logger = logging.getLogger(__name__)

class ProductEvent():
    """Wrapper class for the go-mms product event.
    """

    def __init__(
        self, jobName="", product="", productionHub="", productLocation="", eventInterval=0
    ):

        # Event properties
        self._eventJobName = jobName
        self._eventProduct = product
        self._eventProductionHub = productionHub
        self._eventProductLocation = productLocation
        self._eventInterval = eventInterval

        return

    ##
    #  Getters
    ##

    @property
    def jobName(self):
        return self._eventJobName

    @property
    def product(self):
        return self._eventProduct

    @property
    def productionHub(self):
        return self._eventProductionHub

    @property
    def productLocation(self):
        return self._eventProductLocation

    @property
    def eventInterval(self):
        return self._eventInterval

    ##
    #  Setters
    ##

    @jobName.setter
    def jobName(self, value):
        if isinstance(value, str):
            self._eventJobName = value
        else:
            self._eventJobName = ""
            raise ValueError("ProductEvent.jobName must be a string")
        return

    @product.setter
    def product(self, value):
        if isinstance(value, str):
            self._eventProduct = value
        else:
            self._eventProduct = ""
            raise ValueError("ProductEvent.product must be a string")
        return

    @productionHub.setter
    def productionHub(self, value):
        if isinstance(value, str):
            self._eventProductionHub = value
        else:
            self._eventProductionHub = ""
            raise ValueError("ProductEvent.productionHub must be a string")
        return

    @productLocation.setter
    def productLocation(self, value):
        if isinstance(value, str):
            self._eventProductLocation = value
        else:
            self._eventProductLocation = ""
            raise ValueError("ProductEvent.productLocation must be a string")
        return

    @eventInterval.setter
    def eventInterval(self, value):
        if isinstance(value, int):
            self._eventInterval = value
        else:
            self._eventInterval = ""
            raise ValueError("ProductEvent.eventInterval must be an integer")
        return

    ##
    #  Methods
    ##

    def send(self):
        """Send the event data to the MMSd API.
        """
        nowTime = datetime.now().astimezone()
        nextTime = nowTime + timedelta(seconds=self._eventInterval)

        payLoad = json.dumps({
            "JobName":         str(self._eventJobName),
            "Product":         str(self._eventProduct),
            "ProductionHub":   str(self._eventProductionHub),
            "ProductLocation": str(self._eventProductLocation),
            "CreatedAt":       nowTime.isoformat(),
            "NextEventAt":     nextTime.isoformat(),
        })

        apiURL = self._eventProductionHub + "/api/v1/postevent"
        httpReq = request.Request(apiURL, data=str(payLoad).encode("utf-8"))

        httpReq.add_header("User-Agent", "Py-MMS (Python script)")
        httpReq.add_header("Content-Type", "application/json")
        httpReq.add_header("Api-Key", "APIKEY")

        try:
            httpResp = request.urlopen(httpReq)
        except error.HTTPError as hErr:
            logger.error(str(hErr))
            raise MMSError
        except error.URLError as uErr:
            logger.error(str(uErr))
            raise MMSError

        return httpResp

# END Class ProductEvent
