import pandas as pd

from _mappers import atc_lv1, atc_lv2, atc_lv3, atc_lv4, atc_lv5

def atc_classification(atc_code):
    """Gets information for a given ATC id."""
    if not isinstance(atc_code, str):
        raise ValueError("ATC code must be a string.")

    atc_code = list(atc_code.upper())

    if len(atc_code) != 7:
        raise ValueError("ATC code must be a string of 7 characters.")
    lv1_code = atc_code[0]
    lv2_code = ''.join(atc_code[0:2])
    lv3_code = ''.join(atc_code[0:4])
    lv4_code = ''.join(atc_code[0:5])
    lv5_code = atc_code
    codes = [lv1_code, lv2_code, lv3_code, lv4_code, lv5_code]

    lv1_desc = atc_lv1[lv1_code]
    lv2_desc = atc_lv2[lv2_code]
    lv3_desc = atc_lv3[lv3_code]
    lv4_desc = atc_lv4[lv4_code]
    lv5_desc = atc_lv5[lv5_code]
    descriptions = [lv1_desc, lv2_desc, lv3_desc, lv4_desc, lv5_desc]

    atc_info = pd.DataFrame({'level': [1,2,3,4,5],
                            'code': codes,
                            'description': descriptions})
    return atc_info