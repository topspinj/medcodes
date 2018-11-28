atc_level_one = {
    'A': 'alimentary tract and metabolism',
    'B': 'blood and blood forming organs',
    'C': 'cardiovascular system',
    'D': 'dermatologicals',
    'G': 'genito-urinary system and sex hormones',
    'H': 'systemic hormonal preparations, excluding sex hormones and insulins',
    'J': 'anti-infectives for systemic use',
    'L': 'antineoplastic and immunomodulating agents',
    'M': 'musculo-skeletal system',
    'N': 'nervous system',
    'P': 'antiparasitic products, insecticides and repellents',
    'Q': 'veterinary drug',
    'R': 'respiratory system',
    'S': 'sensory organs',
    'V': 'various'
}

def atc_info(atc_id, level=1):
    """Gets information for a given ATC id."""
    info = None
    if level == 1:
        category = atc_id.upper()[0]
        if category in atc_level_one.values():
            info = atc_level_one[category]
    return info