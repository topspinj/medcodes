"""
Comorbidities
=============
"""

import pytest
import pandas as pd
from medcodes.diagnoses import elixhauser


def test_output():
    assert(isinstance(elixhauser('40491'), list))
