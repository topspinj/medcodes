import os
import sys

import pandas as pd
import pytest

sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("../"))

from medcodes import atc_classification

def test_df_output():
    """
    Check that atc_classification()
    returns a pandas.DataFrame.
    """
    assert(isinstance(atc_classification('V08AC08'), pd.DataFrame))

def test_wrong_type_input_error():
    """
    Check that atc_classification() 
    raises when passed a list.
    """
    msg = "ATC code must be a string."
    with pytest.raises(ValueError):
        atc_classification(['1',2,'3'])

def test_wrong_len_input_error():
    msg = "ATC code must be a string of 7 characters."
    with pytest.raises(ValueError):
        atc_classification('V02')