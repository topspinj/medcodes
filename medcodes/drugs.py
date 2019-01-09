from _drug_mappers import atc_level_one
 
def atc_classification(atc_id, level=1):
    """Gets information for a given ATC id."""
    info = None
    if level == 1:
        category = atc_id.upper()[0]
        if category in atc_level_one.values():
            info = atc_level_one[category]
    return info