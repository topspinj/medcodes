from medcodes.diagnoses._mappers import charlson_codes_v9, charlson_codes_v10, elixhauser_codes_v9, elixhauser_codes_v10

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

    if icd_version not in [9,10]:
        raise ValueError("icd_version must be either 9 or 10. Default is set to 9.")

    if (icd_version==10 and len(icd_code)!=4):
        raise ValueError("ICD10 code must be exactly 4 characters in length.")

    if (icd_version==9 and len(icd_code)!=5):
        raise ValueError("ICD9 code must be exactly 5 characters in length.")

    icd_comorbidity_mapper = charlson_codes_v9
    if icd_version == 10:
        icd_comorbidity_mapper = charlson_codes_v10

    comorbidity = []
    for k, val in icd_comorbidity_mapper.items():
        if icd_code.startswith(tuple(val)):
            comorbidity.append(k)
    if verbose:
        if not comorbidity:
            print(f"No Charlson comorbidities available for ICD {icd_code}")
        else:
            print(f"Comorbidities for ICD {icd_code}:",comorbidity)
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

    References
    ----------
    [1] Quan H, Sundararajan V, Halfon P, et al. Coding algorithms for defining Comorbidities in ICD-9-CM
    and ICD-10 administrative data. Med Care. 2005 Nov; 43(11): 1130-9.
    """
    if not isinstance(icd_code, str):
        raise TypeError("ICD code must be a string.")

    icd_code = icd_code.replace(".", "")
    icd_code = icd_code.strip()

    if icd_version not in [9,10]:
        raise ValueError("icd_version must be either 9 or 10. Default is set to 9.")

    if (icd_version==10 and len(icd_code)!=4):
        raise ValueError("ICD10 code must be exactly 4 characters in length.")

    if (icd_version==9 and len(icd_code)!=5):
        raise ValueError("ICD9 code must be exactly 5 characters in length.")

    icd_comorbidity_mapper = elixhauser_codes_v9
    if icd_version == 10:
        icd_comorbidity_mapper = elixhauser_codes_v10

    comorbidity = []
    for k, val in icd_comorbidity_mapper.items():
        if icd_code.startswith(tuple(val)):
            comorbidity.append(k)
    if verbose:
        if not comorbidity:
            print(f"No Charlson comorbidities available for ICD {icd_code}")
    return comorbidity