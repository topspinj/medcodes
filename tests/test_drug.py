"""
Drug Class
==========
"""

import pytest
import pandas as pd
from medcodes.drugs.standardization import Drug, get_rxcui, get_atc, get_mesh, get_pharm_class, get_pharm_class, spelling_suggestions

#######################################
# spelling_suggestion()
#######################################

def test_spelling_suggestion():
    """
    Test that spelling_suggestions() outputs a list.
    """
    output = spelling_suggestions('aspirinn')
    assert(isinstance(output, list))

def test_spelling_suggestion_error():
    """
    Test that spelling_suggestions() raises an error
    if a non-string is passed.
    """
    with pytest.raises(TypeError):
        spelling_suggestions(True)

#######################################
# get_rxcui()
#######################################

def test_rxcui_output():
    """
    Test that get_rxcui() outputs a string 
    with the correct format.
    """
    output = get_rxcui(drug_id='lipitor', id_type='name')
    assert(isinstance(output, str))
    assert(output=="153165")

def test_rxcui_wrong_id_type():
    with pytest.raises(ValueError):
        get_rxcui(drug_id='CHO', id_type='smiles')

#######################################
# get_atc()
#######################################

def test_get_atc_output():
    output = get_atc(drug_id='lipitor', id_type='name', as_df=False)
    assert(isinstance(output, list))
    output = get_atc(drug_id='lipitor', id_type='name', as_df=True)
    assert(isinstance(output, pd.DataFrame))


#######################################
# Drug()
#######################################

def test_drug_output():
    d = Drug(drug_id='aspirin', id_type='name')
    output = d.get_smiles()
    assert(isinstance(output, str))

    output = d.get_inchikey()
    assert(isinstance(output, str))

    d.describe()
    assert(isinstance(d.brand_name, str))
    assert(isinstance(d.generic_name, str))
    assert(isinstance(d.active_ingredients, str))

def test_drug_wrong_input():
    with pytest.raises(ValueError):
        Drug(drug_id='methanol', id_type='iupac')