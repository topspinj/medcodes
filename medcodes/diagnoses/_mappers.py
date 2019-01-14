"""
ICD-Comorbidity Mappers
================
"""

def icd_list(first_code, last_code, letter=None):
    icd_list = [str(n) for n in range(first_code,last_code)]
    if letter:
        icd_list = [letter+str(n) for n in range(first_code,last_code)]
    return icd_list


charlson_matches_codes_v9 = {
    'congestive heart failure': ['39891','40201','40211','40291','40401','40403','40411','40413','40491','40493','4254','4255','4256','4257','4258','4259'],
    'peripheral vascular disease': ['4431', '4432', '4433', '4434', '4435', '4436', '4437', '4438', '4439', '0930', '4373', '4471', '5571', '5579', 'V434'],
    'cerebrovascular disease': ['36234'],
    'dementia': ['2941', '3312'],
    'chronic pulmonary disease': ['4168','4169','5064','5081','5088'],
    'rheumatic disease': ['4465', '7100', '7101', '7102', '7103', '7104', '7140', '7141', '7142', '7148'],
    'mild liver disease': ['07022', '07023', '07032', '07033', '07044', '07054', '0706', '0709', '5733', '5734', '5738', '5739', 'V427'],
    'diabetes without chronic complication': ['2500', '2501', '2502', '2503', '2508', '2509'],
    'diabetes with chronic complication': ['2504', '2505', '2506', '2507'],
    'hemiplegia': ['3340', '3341', '3342', '3343', '3344', '3345', '3346', '3341', '3349'],
    'renal disease': ['40301','40311','40391','40402','40403','40412','40413','40492','40493','5830','5831','5832','5833','5834','5835','5836','5837','5880','V420','V451'],
    'malignancy': ['2386'],
    'moderate or severe liver disease': ['4560','4561','4562','5722','5723','5724','5725','5726','5727','5728']
}

charlson_startswith_codes_v9 = {
    'myocardial infarction': ['410', '412'],
    'congestive heart failure': ['428'],
    'peripheral vascular disease': ['440', '441'],
    'cerebrovascular disease': ['430', '431', '432', '433', '434', '435', '436', '437', '438'],
    'dementia': ['290'],
    'chronic pulmonary disease': ['490','491','492','493','494','495','496','497','498','499','500','501','502','503','504','505'],
    'rheumatic disease': ['725'],
    'peptic ulcer disease': ['531', '532', '533', '534'],
    'mild liver disease': ['570', '571'],
    'hemiplegia': ['342', '343'],
    'renal disease': ['585','586','V56','582'],
    'malignancy': icd_list(140,173)+icd_list(174,195)+icd_list(200,209),
    'metastatic solid tumor': ['196', '197', '198', '199'],
    'AIDS/HIV': ['042','043','044']
}

elixhauser_matches_codes_v9 = {
    'congestive heart failure': ['39891','40201','40211','40291','40401','40403','40411','40413','40491','40493','4254','4255','4256','4257','4258','4259'],
    'cardiac arrhythmias': ['4260','42613','4267','4269','42610','42612','4270','4271','4272','4273','4274','4276','4277','4278','4279','7850','99601','99604','V450','V533'],
    'valvular disease': ['0932','7463','7464','7465','7466','V422','V433'],
    'pulmonary circulation disorders': ['4150','4151','4170','4178','4179'],
    'peripheral vascular disorders': ['0930','4373','4431', '4432', '4433', '4434', '4435', '4436', '4437', '4438', '4439','4471','5571','5579','V434'],
    'paralysis': ['3440', '3441', '3442', '3443', '3444', '3445', '3446','3341','3449'],
    'other neurological disorders': ['3319','3320','3321','3334','3335','33392','3362','3481','3483','7803','7843'],
    'chronic pulmonary disease': ['4168','4169','5064','5081','5088'],
    'diabetes, uncomplicated': ['2500','2501','2502','2503'],
    'diabetes, complicated': ['2504','2505','2506','2507','2508','2509'],
    'hypothyroidism': ['2409','2461','2468'],
    'renal failure': ['40301','40311','40391','40402','40403','40493','5880','V420'],
    'liver disease': ['07022','07023','07032','07033','07044','07054','0706','0709','4560','4561','4562','5722','5723','5724','5725','5726','5727','5728','5733','5734','5738','5739','V427'],
    'peptic ulcer diease excluding bleeding': ['5317','5319','5327','5329','5337','5339','5347','5349'],
    'lymphoma': ['2030','2386'],
    'rheumatoid arthritis': ['7010','7100','7101','7102','7103','7104','7108','7109','7112','7193','7285','72889','72930'],
    'coagulopathy': ['2871','2873','2874','2875'],
    'obesity': ['2780'],
    'weight loss': ['7832','7994'],
    'fluid and electrolyte disorders': ['2536'],
    'blood loss anemia': ['2800'],
    'deficiency anemia': ['2801', '2802', '2803', '2804', '2805', '2806', '2807', '2808', '2809'],
    'alcohol abuse': ['2652','2911','2913','2915', '2916', '2917', '2918', '2919','3030','3039','3050','3575','4255','5353','5710','5711','5712','5713','V113'],
    'drug abuse': ['3052','3053','3054','3055','3056','3057','3058','3059','V6542'],
    'psychoses': ['2938','29604','29614','29644','29654'],
    'depression': ['2962','2963','2965','3004','311']
    }

elixhauser_startswith_codes_v9 = {
    'congestive heart failure': ['428'],
    'valvular disease': ['394', '395', '396', '397','424'],
    'pulmonary circulation disorders': ['416'],
    'peripheral vascular disorders': ['440','441'],
    'hypertension, uncomplicated': ['401'],
    'hypertension, complicated': ['402','403','404','405'],
    'paralysis': ['342','343'],
    'other neurological disorders': ['334','335','340','341','345'],
    'chronic pulmonary disease': icd_list(490,506),
    'hypothyroidism': ['243','244'],
    'renal failure': ['585','586','V56','V451'],
    'liver disease': ['570','571'],
    'AIDS/HIV': ['042','043','044'],
    'lymphoma': ['200','201','202'],
    'metastatic cancer': ['196','197','198','199'],
    'solid tumor metastasis': icd_list(140,173)+icd_list(174,196),
    'rheumatoid arthritis': ['446','714','720','725'],
    'coagulopathy': ['286'],
    'weight loss': ['260','261','262','263'],
    'fluid and electrolyte disorders': ['276'],
    'deficiency anemia': ['281'],
    'alcohol abuse': ['980'],
    'drug abuse': ['292','304'],
    'psychoses': ['295','297','298'],
    'depression': ['309']
    }


charlson_matches_codes_v10 = {
    'myocardial infarction': ['I252'],
    'congestive heart failure': ['I099','I110','I132','I255','I420','I425','I426','I427','I428','I429','P290'],
    'peripheral vascular disease': ['I731','I738','I739','I771','I790','I792','K551','K558','K559','Z958','Z959'],
    'cerebrovascular disease': ['H340'],
    'dementia': ['F051','G311'],
    'chronic pulmonary disease': ['I278','I279','J684','J701','J703'], 
    'rheumatic disease': ['M315','M351','M353','M360'],
    'mild liver disease': ['K700','K701','K702','K703','K709','K713','K714','K715','K717','K760','K762','K763','K764','K768','K769','Z944'],
    'diabetes without chronic complication': ['E100', 'E101', 'E106', 'E108', 'E109', 'E110', 'E111', 'E116', 'E118', 'E119', 'E120', 'E121', 'E126', 'E128', 'E129', 'E130', 'E131', 'E136', 'E138', 'E139', 'E140', 'E141', 'E146', 'E148', 'E149'],
    'diabetes with chronic complication': ['E102','E103','E104','E105','E107','E112','E113','E114','E115','E117','E122','E123','E124','E125','E127','E132','E133','E134','E135','E137','E142','E143','E144','E145','E147'],
    'hemiplegia or paraplegia': ['G041','G114','G801','G802','G830','G831','G832','G833','G834','G839'],
    'renal disease': ['I120','I131','N032','N033','N034','N035','N036','N037','N052','N053','N054','N055','N056','N057','N250','Z490','Z491','Z492','Z940','Z992'],
    'moderate or severe liver disease': ['I850','I859','I864','I982','K704','K711','K721','K729','K765','K766','K767']
}

charlson_startswith_codes_v10 = {
    'myocardial infarction': ['I21','I22'],
    'congestive heart failure': ['I50','I43'],
    'peripheral vascular disease': ['I70','I71'],
    'cerebrovascular disease': ['G45','G46','I60','I61','I62','I63','I64','I65','I66','I67','I68','I69'],
    'dementia': ['F00','F01','F02','F03','G30'],
    'chronic pulmonary disease': ['J40','J41','J42','J43','J44','J45','J46','J47','J60','J61','J62','J63','J64','J65','J66','J67'],
    'rheumatic disease': ['M05','M06','M32','M33','M34'],
    'peptic ulcer disease': ['K25','K26','K27','K28'],
    'mild liver disease': ['B18','K73','K74'],
    'hemiplegia or paraplegia': ['G81','G82'],
    'renal disease': ['N18','N19'],
    'malignancy': ['C00','C01','C02','C03','C04','C05','C06','C07','C08','C09','C43','C88']+icd_list(10,27,'C')+icd_list(30,35,'C')+icd_list(37,42,'C')+icd_list(45,59,'C')+icd_list(60,77,'C')+icd_list(81,86,'C')+icd_list(90,98,'C'),
    'metastatic solid tumor': ['C77','C78','C79','C80'],
    'AIDS/HIV': ['B20','B21','B22','B24']
}

elixhauser_matches_codes_v10 = {
    'congestive heart failure': ['I099','I110','I130','I132','I255','I420','I425','I426','I427','I428','I429','P290'],
    'cardiac arrhythmias': ['I441','I442','I443','I456','I459','R000','R001','R008','T821','Z450','Z950'],
    'valvular disease': ['A520','I091','I098','Q230','Q231','Q232','Q233','Z952','Z953','Z954'],
    'pulmonary circulation disorders': [],
    'peripheral vascular disorders': [],
    'paralysis': [],
    'other neurological disorders': [],
    'chronic pulmonary disease': [],
    'diabetes, uncomplicated': [],
    'diabetes, complicated': [],
    'hypothyroidism': [],
    'renal failure': [],
    'liver disease': [],
    'peptic ulcer diease excluding bleeding': [],
    'lymphoma': [],
    'rheumatoid arthritis': [],
    'coagulopathy': [],
    'obesity': [],
    'weight loss': [],
    'fluid and electrolyte disorders': [],
    'blood loss anemia': [],
    'deficiency anemia': [],
    'alcohol abuse': [],
    'drug abuse': [],
    'psychoses': [],
    'depression': []
    }

elixhauser_startswith_codes_v10 = {
    'congestive heart failure': ['I43','I50'],
    'cardiac arrhythmias': ['I47','I48','I49'],
    'valvular disease': ['I05','I06','I07','I08','I34','I35','I36','I37','I38','I39'],
    'pulmonary circulation disorders': ['I26','I27'],
    'peripheral vascular disorders': ['I70','I71'],
    'hypertension, uncomplicated': [],
    'hypertension, complicated': [],
    'paralysis': [],
    'other neurological disorders': [],
    'chronic pulmonary disease': [],
    'diabetes, uncomplicated': [],
    'diabetes, complicated': [],
    'hypothyroidism': [],
    'renal failure': [],
    'liver disease': [],
    'peptic ulcer diease excluding bleeding': [],
    'lymphoma': [],
    'rheumatoid arthritis': [],
    'coagulopathy': [],
    'obesity': [],
    'weight loss': [],
    'fluid and electrolyte disorders': [],
    'blood loss anemia': [],
    'deficiency anemia': [],
    'alcohol abuse': [],
    'drug abuse': [],
    'psychoses': [],
    'depression': []
    }