from medcodes.diagnoses._mappers import charlson_matches_codes_v9, charlson_startswith_codes_v9, elixhauser_matches_codes_v9, elixhauser_startswith_codes_v9


def charlson(icd_code, icd_version=9, verbose=True):
    """
    Outputs Charlson comorbidity for a given ICD code.

    Parameters
    ----------
    code : str
        ICD code
    icd_version : str
        Can be either 9 or 10

    Returns
    -------
    Charlson comorbidity

    References
    ----------
    [1] Quan H, Sundararajan V, Halfon P, et al. Coding algorithms for defining Comorbidities in ICD-9-CM
    and ICD-10 administrative data. Med Care. 2005 Nov; 43(11): 1130-9.
    """
    if not isinstance(icd_code, str):
        raise TypeError("ICD code must be a string.")

    icd_code = icd_code.replace(".", "")
    icd_code = icd_code.strip()

    comorbidity = []
    for k, val in charlson_matches_codes_v9.items():
        if icd_code in val:
            comorbidity.append(k)
    for k, val in charlson_startswith_codes_v9.items():
        if icd_code.startswith(tuple(val)):
            comorbidity.append(k)
    if verbose:
        if not comorbidity:
            print(f"No Charlson comorbidities available for ICD {icd_code}")
    return comorbidity

def elixhauser(icd_code, icd_version=9, verbose=True):
    """
    Outputs Elixhauser comorbidity for a given ICD code.

    Parameters
    ----------
    code : str
        ICD code
    icd_version : str
        Can be either 9 or 10
    
    Returns
    -------
    Elixhauser comorbidity
    """
    if not isinstance(icd_code, str):
        raise TypeError("ICD code must be a string.")

    icd_code = icd_code.replace(".", "")
    icd_code = icd_code.strip()

    comorbidity = []
    for k, val in elixhauser_matches_codes_v9.items():
        if icd_code in val:
            comorbidity.append(k)
    for k, val in elixhauser_startswith_codes_v9.items():
        if icd_code.startswith(tuple(val)):
            comorbidity.append(k)
    if verbose:
        if not comorbidity:
            print(f"No Elixhauser comorbidities available for ICD {icd_code}")
    return comorbidity