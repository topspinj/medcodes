"""
Comorbidities
=============
"""

import pytest
import pandas as pd
from medcodes.diagnoses import elixhauser, charlson


def test_elixhauser_output():
    assert(isinstance(elixhauser('40491'), list))

def test_elixhauser_wrong_type_input_error():
    with pytest.raises(TypeError):
        elixhauser(1001)

def test_charlson_output():
    assert(isinstance(charlson('39891'), list))
