def charlson_comorbidities(code, icd_version='9'):
    """
    Outputs Charlson comorbidity for a given ICD code.

    Parameters
    ----------
    code : str
        ICD code
    icd_version : str
        Can be either '9' or '10'
    
    Returns
    -------
    Charlson comorbidity 
    References
    ----------
    [1] Quan H, Sundararajan V, Halfon P, et al. Coding algorithms for defining Comorbidities in ICD-9-CM
    and ICD-10 administrative data. Med Care. 2005 Nov; 43(11): 1130-9. 

    """
    if not isinstance(code, str):
        raise TypeError("Code must be a string.")
    
    code = code.replace(".","")
    code = code.strip()

    peripheral_vascular_codes = [str(n) for n in range(4431,4440)]+['0930','4373','4471','5571','5579','V434']
    cerebrovascular_codes = [str(n) for n in range(430,440)]
    dementia_codes = ['2941','3312']
    rheumatic_codes = ['4465','7100','7101','7102','7103','7104','7140','7141','7142','7148']
    mild_liver_codes = ['07022','07023','07032','07033','07044','07054','0706','0709','5733','5734','5738','5739','V427']
    peptic_ulcer_codes = [str(n) for n in range(531,535)]
    diabetes_wo_complication_codes = ['2500','2501','2502','2503','2508','2509']
    diabetes_w_complication = [str(n) for n in range(2504,2508)]
    hemiplegia_codes = [str(n) for n in range(3340,3347)]+['3341','3349']
    metatastic_solid_tumor_codes = [str(n) for n in range(196,200)]
    moderate_severe_liver_codes = [[str(n) for n in range(5722,5729)]+['4560','4561','4562']
    
    comorbidity = None
    if code.startswith(('410','412')):
        comorbidity = 'myocardial infarction'
    if code.startswith(('440','441')) or code is in peripheral_vascular_codes:
        comorbidity = 'peripheral vascular disease'
    if code.startswith(tuple(cerebrovascular_codes)) or code == '36234':
        comorbidity = 'cerebrovascular disease'
    if code.startswith('290') or code is in dementia_codes:
        comorbidity = 'dementia'
    if code.startswith('725') or code is in rheumatic_codes:
        comorbidity = 'rheumatic disease'
    if code.startswith(tuple(peptic_ulcer_codes)):
        comorbidity = 'peptic ulcer disease'
    if code.startswith(('570','571')) or code is in mild_liver_codes:
        comorbidity = 'mild liver disease'
    if code is in diabetes_wo_complication_codes:
        comorbidity = 'diabetes without chronic complication'
    if code is in diabetes_w_complication:
        comorbidity = 'diabetes with chronic complication'
    if code.startswith(('342','343')) or code is in hemiplegia_codes:
        comorbidity = 'hemiplegia'
    if code.startswith(tuple(metatastic_solid_tumor_codes)):
        comorbidity = 'AIDS/HIV'
    return comorbidity 