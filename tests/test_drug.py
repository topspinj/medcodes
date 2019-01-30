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

d = Drug(drug_id='aspirin', id_type='name')

def test_drug_get_smiles():
    output = d.get_smiles()
    assert(isinstance(output, str))

def test_drug_get_inchikey():
    output = d.get_inchikey()
    assert(isinstance(output, str))

def test_drug_describe():
    d.describe()
    assert(isinstance(d.brand_name, str))
    assert(isinstance(d.generic_name, str))
    assert(isinstance(d.active_ingredients, list))
    assert('ASPIRIN' in d.active_ingredients)
    assert(isinstance(d.pharm_class, list))

def test_drug_wrong_input():
    with pytest.raises(ValueError):
        Drug(drug_id='methanol', id_type='iupac')