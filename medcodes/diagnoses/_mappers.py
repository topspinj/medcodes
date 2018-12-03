charlson_matches_codes = {
    'peripheral vascular codes': ['4431', '4432', '4433', '4434', '4435', '4436', '4437', '4438', '4439', '0930', '4373', '4471', '5571', '5579', 'V434'],
    'dementia': ['2941', '3312'],
    'rheumatic disease': ['4465', '7100', '7101', '7102', '7103', '7104', '7140', '7141', '7142', '7148'],
    'mild liver disease': ['07022', '07023', '07032', '07033', '07044', '07054', '0706', '0709', '5733', '5734', '5738', '5739', 'V427'],
    'diabetes without chronic complication': ['2500', '2501', '2502', '2503', '2508', '2509'],
    'diabetes with chronic complication': ['2504', '2505', '2506', '2507'],
    'malignancy': ['2386'],
    'renal disease': [],
    'moderate or severe liver disease': ['4560','4561','4562','5722','5723','5724','5725','5726','5727','5728'],
    'hemiplegia': ['3340', '3341', '3342', '3343', '3344', '3345', '3346', '3341', '3349']
}

charlson_startswith_codes = {
    'myocardial infarction': ['410', '412'],
    'peripheral vascular disease': ['440', '441'],
    'cerebrovascular disease': ['430', '431', '432', '433', '434', '435', '436', '437', '438', '439'],
    'dementia': ['290'],
    'rheumatic disease': ['725'],
    'peptic ulcer disease': ['531', '532', '533', '534'],
    'mild liver disease': ['570', '571'],
    'hemiplegia': ['342', '343'],
    'renal disease': ['585','586','V56','582'],
    'malignancy': [str(n) for n in range(140,173)]+[str(n) for n in range(174,195)]+[str(n) for n in range(200,209)],
    'metastatic solid tumor': ['196', '197', '198', '199'],
    'AIDS/HIV': ['042','043','044']
}