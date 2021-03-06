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
    )

    assert pEvent.jobName == "FirstA"
    assert pEvent.product == "FirstB"
    assert pEvent.productionHub == "FirstC"
    assert pEvent.productLocation == "FirstD"
    assert pEvent.eventInterval == 42

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

    pEvent.jobName = "SecondA"
    pEvent.product = "SecondB"
    pEvent.productionHub = "SecondC"
    pEvent.productLocation = "SecondD"
    pEvent.eventInterval = 43

    assert pEvent.jobName == "SecondA"
    assert pEvent.product == "SecondB"
    assert pEvent.productionHub == "SecondC"
    assert pEvent.productLocation == "SecondD"
    assert pEvent.eventInterval == 43

@pytest.mark.events
def testSendProductEvent(monkeypatch):
    # Valid Event
    pEvent = ProductEvent(
        jobName="TestJob",
        product="TestProduct",
        productionHub="http://localhost:8080",
        productLocation="/tmp",
        eventInterval=3600,
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
