from medcodes.diagnoses._mappers import comorbidity_mappers

def _check_icd_inputs(icd_code, icd_version):
    if icd_version not in [9,10]:
        raise ValueError("icd_version must be either 9 or 10. Default is set to 9.")
    if not isinstance(icd_code, str):
        raise TypeError("icd_code must be a string.")
    if (icd_version==10 and len(icd_code)!=4):
        raise ValueError("icd_code version 10 must be exactly 4 characters in length.")
    if (icd_version==9 and len(icd_code)!=5):
        raise ValueError("icd_code version 9 must be exactly 5 characters in length.") 

def _format_icd_code(icd_code):
    icd_code = icd_code.replace(".", "")
    icd_code = icd_code.strip()
    return icd_code

def _check_custom_map(custom_map):
    if not isinstance(custom_map, dict):
        raise TypeError("custom_map must be a dictionary")
    for k, val in custom_map.items():
        if not isinstance(val, list):
            raise TypeError(f'{k} values must be a list')

def charlson(icd_code, icd_version=9):
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
    list
        Charlson comorbidities

    References
    ----------
    [1] Quan H, Sundararajan V, Halfon P, et al. Coding algorithms for defining Comorbidities in ICD-9-CM
    and ICD-10 administrative data. Med Care. 2005 Nov; 43(11): 1130-9.
    """
    _check_icd_inputs(icd_code=icd_code, icd_version=icd_version)
    icd_code = _format_icd_code(icd_code=icd_code)

    mapper = comorbidity_mappers[f'charlson_{icd_version}']

    comorbidity = []
    for k, val in mapper.items():
        if icd_code.startswith(tuple(val)):
            comorbidity.append(k)
    return comorbidity

def elixhauser(icd_code, icd_version=9):
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
    list
        Elixhauser comorbidities

    References
    ----------
    [1] Quan H, Sundararajan V, Halfon P, et al. Coding algorithms for defining Comorbidities in ICD-9-CM
    and ICD-10 administrative data. Med Care. 2005 Nov; 43(11): 1130-9.
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
    """
    pass