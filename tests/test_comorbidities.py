"""
Comorbidities
=============
"""

import pytest
import pandas as pd
from medcodes.diagnoses import elixhauser, charlson, custom_comorbidities, comorbidities


def test_elixhauser_output():
    """
    Test that elixhauser() outputs a list.
    """
    output = elixhauser('40491')
    assert(isinstance(output, list))

def test_elixhauser_wrong_type_input_error():
    """
    Test that elixhauser() raises a TypeError when
    a non-string is pass in. 
    """
    with pytest.raises(TypeError):
        elixhauser(1001)

def test_charlson_output():
    """
    Test that charlson() outputs a list.
    """
    output = charlson('39891')
    assert(isinstance(output, list))

def test_comorbidities_output():
    """
    Test that comorbidities() outputs a dataframe. 
    """
    icd_codes = ['3318', '82320', '33382']
    custom_map = {
        'stroke': ['33']
    }
    output = comorbidities(icd_codes, icd_version=9, mapping='custom', custom_map=custom_map)
    assert(isinstance(output, pd.DataFrame))

def test_comorbidities_custom_map_schema_error():
    """
    Test that comorbidities() raises a TypeError if custom_map
    does not follow the appropriate schema. Values of the custom_map 
    dictionary must be a list. 
    """
    icd_codes = ['3318', '82320', '33382']
    custom_map = {
        'stroke': '33'
    }
    with pytest.raises(TypeError):
        comorbidities(icd_codes, icd_version=9, mapping='custom', custom_map=custom_map)

def test_comorbidities_custom_map_type_error():
    """
    Test that comorbidities() raises a TypeError when
    custom_map is not a dictionary.
    """
    icd_codes = ['3318', '82320', '33382']
    custom_map = {
        'stroke': '33'
    }
    with pytest.raises(TypeError):
        comorbidities(icd_codes, icd_version=9, mapping='custom', custom_map='123')
  