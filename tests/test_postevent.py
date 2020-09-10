# -*- coding: utf-8 -*-
"""Post event object tests.
"""

import pytest

from pymms import ProductEvent

@pytest.mark.events
def testCreateProductEvent():
    pEvent = ProductEvent(
        product="FirstA",
        productionHub="FirstB",
        productLocation="FirstC"
    )

    assert pEvent.product == "FirstA"
    assert pEvent.productionHub == "FirstB"
    assert pEvent.productLocation == "FirstC"

    with pytest.raises(ValueError):
        pEvent.product = 0

    with pytest.raises(ValueError):
        pEvent.productionHub = 1

    with pytest.raises(ValueError):
        pEvent.productLocation = 2

    pEvent.product = "SecondA"
    pEvent.productionHub = "SecondB"
    pEvent.productLocation = "SecondC"

    assert pEvent.product == "SecondA"
    assert pEvent.productionHub == "SecondB"
    assert pEvent.productLocation == "SecondC"
