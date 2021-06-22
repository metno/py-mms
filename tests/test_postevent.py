# -*- coding: utf-8 -*-
"""Post event object tests.
"""

import pytest

from urllib import request
from pymms import ProductEvent

@pytest.mark.events
def testCreateProductEvent():
    pEvent = ProductEvent(
        jobName="FirstA",
        product="FirstB",
        productionHub="FirstC",
        productLocation="FirstD",
        eventInterval=42,
        refTime="2021-06-22T12:00:00Z",
        counter=1,
        totalCount=1
    )

    assert pEvent.jobName == "FirstA"
    assert pEvent.product == "FirstB"
    assert pEvent.productionHub == "FirstC"
    assert pEvent.productLocation == "FirstD"
    assert pEvent.eventInterval == 42
    assert pEvent.refTime == "2021-06-22T12:00:00Z"
    assert pEvent.counter == 1
    assert pEvent.totalCount == 1

    with pytest.raises(ValueError):
        pEvent.jobName = 0

    with pytest.raises(ValueError):
        pEvent.product = 0

    with pytest.raises(ValueError):
        pEvent.productionHub = 1

    with pytest.raises(ValueError):
        pEvent.productLocation = 2

    with pytest.raises(ValueError):
        pEvent.eventInterval = "2"

    with pytest.raises(ValueError):
        pEvent.refTime = 0

    with pytest.raises(ValueError):
        pEvent.counter = "1"

    with pytest.raises(ValueError):
        pEvent.totalCount = "1"

    pEvent.jobName = "SecondA"
    pEvent.product = "SecondB"
    pEvent.productionHub = "SecondC"
    pEvent.productLocation = "SecondD"
    pEvent.eventInterval = 43
    pEvent.refTime = "2000-01-01T00:00:00Z"
    pEvent.counter = 2
    pEvent.totalCount = 3

    assert pEvent.jobName == "SecondA"
    assert pEvent.product == "SecondB"
    assert pEvent.productionHub == "SecondC"
    assert pEvent.productLocation == "SecondD"
    assert pEvent.eventInterval == 43
    assert pEvent.refTime == "2000-01-01T00:00:00Z"
    assert pEvent.counter == 2
    assert pEvent.totalCount == 3

@pytest.mark.events
def testSendProductEvent(monkeypatch):
    # Valid Event
    pEvent = ProductEvent(
        eventInterval=3600,
        jobName="TestJob",
        product="TestProduct",
        productionHub="http://localhost:8080",
        productLocation="/tmp/testproduct.ext",
        refTime="2021-06-22T12:00:00Z",
        counter=1,
        totalCount=1,
    )
    monkeypatch.setattr(request, "urlopen", lambda *args, **kwargs: None)
    assert pEvent.send() is None

    # Invalid Hub
    pEvent.productionHub = "no-such-hub"
    with pytest.raises(ValueError):
        pEvent.send()

    # Invalid Return
    # monkeypatch.setattr(GoMMS, "productEvent", lambda self, payLoad: r"{}")
    # with pytest.raises(MMSError):
    #     retData = pEvent.send()
