# py-mms

[![flake8](https://github.com/metno/py-mms/workflows/flake8/badge.svg?branch=master)](https://github.com/metno/py-mms/actions)
[![pytest](https://github.com/metno/py-mms/workflows/pytest/badge.svg?branch=master)](https://github.com/metno/py-mms/actions)
[![codecov](https://codecov.io/gh/metno/py-mms/branch/master/graph/badge.svg)](https://codecov.io/gh/metno/py-mms)

Python client for MET Messaging System (MMS).

## How to Use

Currently, `py-mms` only contains a wrapper for sending MMS product events via the `go-mms` tool.
Here's a usage example:
```Python
from pymms import ProductEvent, MMSError

pEvent = ProductEvent(
    jobName="Job",
    product="Test",
    productionHub="http://localhost:8080",
    productLocation="/tmp",
    eventInterval=3600
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
from the root folder. Alternatively, you may need to use `pytest-3` on some systems with both Python 2 and 3 as `pytest` often defaults to the Python 2 version.

The coverage report requires the package `pytest-cov` to be installed.

**Note:** The tests require the MMD daemon to be running. You can either run it from the `pymms/lib/go-mms` folder,
or from the [go-mms](https://github.com/metno/go-mms) source. It currently has to be run from the root folder of `go-mms` due to a dependence on template files in the `go-mms` repository. See [go-mms issue #31](https://github.com/metno/go-mms/issues/31).
