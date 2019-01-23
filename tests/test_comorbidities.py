"""
Comorbidities
=============
"""

import pytest
import pandas as pd
from medcodes.diagnoses import elixhauser, charlson, custom_comorbidities, comorbidities


def test_elixhauser_output():
    output = elixhauser('40491')
    assert(isinstance(output, list))

def test_elixhauser_wrong_type_input_error():
    with pytest.raises(TypeError):
        elixhauser(1001)

def test_charlson_output():
    output = charlson('39891')
    assert(isinstance(output, list))

def test_comorbidities_output():
    icd_codes = ['3318', '82320', '33382']
    custom_map = {
        'stroke': ['33']
    }
    output = comorbidities(icd_codes, icd_version=9, mapping='custom', custom_map=custom_map)
    assert(isinstance(output, pd.DataFrame))

def test_comorbidities_custom_map():
    icd_codes = ['3318', '82320', '33382']
    custom_map = {
        'stroke': '33'
    }
    with pytest.raises(TypeError):
        comorbidities(icd_codes, icd_version=9, mapping='custom', custom_map=custom_map)
