# -*- coding: utf-8 -*-
"""Post event object tests.
"""

import pytest

from pymms import ProductEvent

@pytest.mark.events
def testCreateProductEvent():
    pEvent = ProductEvent("FirstA", "FirstB", "FirstC")

    assert pEvent.product == "FirstA"
    assert pEvent.productSlug == "FirstB"
    assert pEvent.productionHub == "FirstC"

    with pytest.raises(ValueError):
        pEvent.product = 0

    with pytest.raises(ValueError):
        pEvent.productSlug = 1

    with pytest.raises(ValueError):
        pEvent.productionHub = 2

    pEvent.product = "SecondA"
    pEvent.productSlug = "SecondB"
    pEvent.productionHub = "SecondC"

    assert pEvent.product == "SecondA"
    assert pEvent.productSlug == "SecondB"
    assert pEvent.productionHub == "SecondC"
