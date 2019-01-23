"""
Comorbidtiies
=============
ICD (International Classification of Diseases) is a classification system that standardizes
diagnoses into alphanumeric codes. There are two variants of ICD: 1) ICD-9, an earlier version
which contains 13,000 codes, and 2) ICD-10, a more recent version with over 68,000 codes.

The comorbidity functions in this module are used to cluster diagnoses into comorbidity groups using
comorbidity mapping indices such as Elixhauser, Charlson, or a custom mapper.
"""

import pandas as pd

from medcodes.diagnoses._mappers import comorbidity_mappers

def _check_icd_inputs(icd_code, icd_version):
    """Checks that icd_code input is the correct format."""
    if icd_version not in [9,10]:
        raise ValueError("icd_version must be either 9 or 10. Default is set to 9.")
    if not isinstance(icd_code, str):
        raise TypeError("icd_code must be a string.")
    if (icd_version==10 and len(icd_code)!=4):
        raise ValueError("icd_code version 10 must be exactly 4 characters in length.")
    if (icd_version==9 and len(icd_code)!=5):
        raise ValueError("icd_code version 9 must be exactly 5 characters in length.") 

def _format_icd_code(icd_code):
    """Removes punctuation from icd_code string."""
    icd_code = icd_code.replace(".", "")
    icd_code = icd_code.strip()
    return icd_code

def _check_custom_map(custom_map):
    """Checks that vals of custom_map dict are dictionaries."""
    if not isinstance(custom_map, dict):
        raise TypeError("custom_map must be a dictionary.")
    for k, val in custom_map.items():
        if not isinstance(val, list):
            raise TypeError(f'{k} values must be a list')

def charlson(icd_code, icd_version=9):
    """
    Identifies relevant Charlson comorbidities for a ICD code of interest.
    Uses Charlson comorbidity index mappings as defined by Quan et al. [1].

    Parameters
    ----------
    icd_code : str
        ICD code
    icd_version : str
        Can be either 9 or 10

    Returns
    -------
    list
        Charlson comorbidities

    References
    ----------
    [1] Quan H, Sundararajan V, Halfon P, et al. Coding algorithms for 
    defining Comorbidities in ICD-9-CM and ICD-10 administrative data. 
    Med Care. 2005 Nov; 43(11): 1130-9.
    """
    _check_icd_inputs(icd_code=icd_code, icd_version=icd_version)
    icd_code = _format_icd_code(icd_code=icd_code)

    mapper = comorbidity_mappers[f'charlson_{icd_version}']

    comorbidities = []

    for k, val in mapper.items():
        if icd_code.startswith(tuple(val)):
            comorbidities.append(k)
    return comorbidities

def elixhauser(icd_code, icd_version=9):
    """
    Identifies relevant Elixhauser comorbidities for a given ICD code.
    Uses Elixhauser comorbidity index mappings as defined by Quan et al. [1].

    Parameters
    ----------
    icd_code : str
        International Classification of Diseases (ICD) code
    icd_version : str
        Version of International Classification of Diseases (ICD). Can be either 9 or 10.
    
    Returns
    -------
    list
        Elixhauser comorbidities

    References
    ----------
    [1] Quan H, Sundararajan V, Halfon P, et al. Coding algorithms for 
    defining Comorbidities in ICD-9-CM and ICD-10 administrative data. 
    Med Care. 2005 Nov; 43(11): 1130-9.
    """
    _check_icd_inputs(icd_code=icd_code, icd_version=icd_version)
    icd_code = _format_icd_code(icd_code=icd_code)

    mapper = comorbidity_mappers[f'elixhauser_{icd_version}']

    comorbidities = []

    for k, val in mapper.items():
        if icd_code.startswith(tuple(val)):
            comorbidities.append(k)
    return comorbidities

def custom_comorbidities(icd_code, icd_version, custom_map):
    """
    Applies custom mapping to ICD code.

    Parameters
    ----------
    icd_code : str
        I
    icd_version : int
    custom_map : dict
        A customized mapper that defines one group of 
        multiple groups of ICD codes.

    Example
    -------
    >>> custom_map = {'stroke': ['33']}
    >>> icd_code = '33010'
    >>> custom_comorbidities(icd_code=icd_code, icd_version=9, custom_map=custom_map)
    """
    _check_icd_inputs(icd_code=icd_code, icd_version=icd_version)
    icd_code = _format_icd_code(icd_code=icd_code)
    _check_custom_map(custom_map)

    comorbidities = []
    for k, val in custom_map.items():
        if icd_code.startswith(tuple(val)):
            comorbidities.append(k)
    return comorbidities

def comorbidities(icd_codes, icd_version=9, mapping='elixhauser', custom_map=None):
    """
    Parameters
    ----------
    icd_codes : list
    icd_version : int
    mapping : str
    custom_map : dict

    Returns
    -------
    pd.DataFrame
    
    References
    ----------
    [1] Quan H, Sundararajan V, Halfon P, et al. Coding algorithms for 
    defining Comorbidities in ICD-9-CM and ICD-10 administrative data. 
    Med Care. 2005 Nov; 43(11): 1130-9.
    """
    if mapping not in ['elixhauser', 'charlson', 'custom']:
        raise ValueError("mappign must be one of 'elixhauser', 'charlson', 'custom'")

    all_comorbidities = []
    for icd_code in icd_codes:
        c = None
        if mapping == 'custom':
            c = custom_comorbidities(icd_code, icd_version, custom_map)
        if mapping == 'elixhauser':
            c = elixhauser(icd_code, icd_version)
        if mapping == 'charlson':
            c = charlson(icd_code, icd_version)
        all_comorbidities.append(c)
    
    comorbidities_table = pd.DataFrame({'icd_code':icd_codes, f'{mapping.lower()}_comorbidity': all_comorbidities})

    return comorbidities_table


