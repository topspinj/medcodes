"""
Comorbidities
=============
"""

import pytest
import pandas as pd
from medcodes.diagnoses import elixhauser, charlson, custom_comorbidities, comorbidities


def test_elixhauser_output():
    assert(isinstance(elixhauser('40491'), list))

def test_elixhauser_wrong_type_input_error():
    with pytest.raises(TypeError):
        elixhauser(1001)

def test_charlson_output():
    assert(isinstance(charlson('39891'), list))

def _test_comorbidities_output():
    icd_codes = ['33191', '33212', '78030']
    custom_map = {
        'stroke': ['33']
    }
    comorbidities(icd_codes, icd_version=9, mapping='custom', custom_map=custom_map)