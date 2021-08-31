# py-mms

[![flake8](https://github.com/metno/py-mms/workflows/flake8/badge.svg?branch=master)](https://github.com/metno/py-mms/actions)
[![pytest](https://github.com/metno/py-mms/workflows/pytest/badge.svg?branch=master)](https://github.com/metno/py-mms/actions)
[![codecov](https://codecov.io/gh/metno/py-mms/branch/master/graph/badge.svg)](https://codecov.io/gh/metno/py-mms)

Python client for MET Messaging System (MMS).

The client requires Python >= 3.6.

## How to Use
Make sure that the `MMS_API_KEY` environment variable is set correctly with a key generated at the MMSD side.

Currently, `py-mms` only contains a wrapper for sending MMS product events to the `go-mms` API.

Here's a usage example:
```Python
from pymms import ProductEvent, MMSError

pEvent = ProductEvent(
    jobName="Job",
    product="Test",
    productionHub="http://localhost:8080",
    productLocation="/tmp",
    eventInterval=3600,
    refTime="2021-06-22T12:00:00Z",
    counter=1,
    totalCount=1
)

try:
    retData = pEvent.send()
except MMSError as err:
    print(f"Error: {err}")
```

## Tests

The tests can be run with `pytest`. For full details and coverage report, run
```bash
pytest -v --cov=pymms
```
from the root folder. Alternatively, you may need to use `pytest-3` on some systems with both
Python 2 and 3 as `pytest` often defaults to the Python 2 version.

The coverage report requires the package `pytest-cov` to be installed.
