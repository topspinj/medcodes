# MedCodes

[![CircleCI](https://circleci.com/gh/topspinj/medcodes.svg?style=svg&circle-token=15b881e69898a9326b263b848fabd0036b5eb6ae)](https://circleci.com/gh/topspinj/medcodes)

MedCodes is a Python package that facilitates the standardization and interpretation of clinical data. 


## Drug Classification

Drugs can be categorized based on attributes such as mechanism of action, chemical structure, function, and metabolic properties. [RxNorm](https://www.nlm.nih.gov/research/umls/rxnorm/) is one component of the Unified Medical Language System (UMLS) that standardizes clinical drug names into a unique identifier and provides capabilities to extract meaningful information for a given drug such as Anatomical Therapeutic Chemical (ATC) classification and MeSH terms. 

##### 1. Anatomical Therapeutic Chemical (ATC) classification
ATC divides the active substances of a drug into different groups accordingly to the organ or system on which they act and their therapeutic, pharmacological, and chemical properties ([1](https://www.who.int/medicines/regulation/medicines-safety/toolkit_atc/en/)). Drugs are grouped at five different levels in which each level represents a different part of a 7 character ATC code. The first (most generic) level contains 14 anatomical/pharmacological groups that are represented by different letters:

- **A:** alimentary tract and metabolism 
- **B:** blood and blood forming organs
- **C:** cardiovascular system 
- **D:** dermatologicals 
- **G:** genito-urinary system and sex hormones
- **H:** systemic hormonal preparations
- **J:** anti-infectives for systemic use
- **L:** anti-neoplastic and immunomodulating agents
- **M:** musculo-skeletal system
- **N:** nervous system
- **P:** anti-parasitic products, insecticides, repellents
- **R:** respiratory system
- **S:** sensory organs
- **V:** various

An example of an ATC code is `C03CA01` and can be broken down into its 5 levels as follows:

- 1st level: `C` - cardiovascular system
- 2nd level: `C03` - diuretics
- 3rd level: `C03C` - high-ceiling diuretics
- 4th level: `C03CA` - sulfonamids
- 5th level: `C03CA01` - furosemide

MedCodes provides functionality to interpret a given ATC code.

<img src="docs/imgs/medcodes_example.png"/>

Example of how it works:

```
get_atc_info('M01AE01')
```

Output:

|atc_level|code|description|
|---------|----|-----------|
|1|M|MUSCOLOSKELETAL SYSTEM|
|2|M01|ANTIINFLAMMATORY AND ANTIRHEUMATIC PRODUCTS|
|3|M01A|NON-STEROIDS|
|4|M01AE|PROPRIONIC ACID DERIVATIVES|
|5|M01AE01|IBUPROFEN|



##### 2. Medical Subject Headings (MeSH) classification

MeSH terms are typically used in the context of indexing and retrieval of literature. Unlike ATC's 5-level classification system, MeSH has several parallel classifications: chemical structure, mechanism of action, and therapeutic use ([2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4120719/)). 

<img src="docs/imgs/drug_classification_example.png"/>

Example of how MedCodes works:

```
get_mesh_info('ibuprofen')
```

Outputs:

|mesh_term|mesh_type|
|---------|---------|
|cyclooxygenase inhibitors|mechanism of action|
|anti-inflammatory agents|therapeutic use|
|analgesic|therapeutic use|

## Drug Information

WIP. 

- To-do: investigate whether it's possible to extract the following information for a given drug:
	- patent info
	- side effects
	- studies involving said drug


## Comorbidities

`International Statistical Classification of Diseases`, also known as ICD, is a classification system used for patient diagnosis. ICD-9 contains 13,000 codes, while ICD-10 has 68,000 codes. At the end of a patient's hospital stay, a list of ICD codes are assigned to that particular hospital admission, which ultimately gets used for reimbursement purposes.  

Comorbidity measures, such as the Charlson comorbidity index and Elixhauser score, are used to cluster the overwhelming number of ICD codes into a smaller subset of well-defined comorbidities. These tools have used in the context of clinical prognosis and comorbidity adjustment in epidemiological outcome studies ([3](https://www.ncbi.nlm.nih.gov/pubmed/15528055), [4](https://www.ncbi.nlm.nih.gov/pubmed/21305268), [5](https://www.ncbi.nlm.nih.gov/pubmed/21509773)). The Charlson comorbidity index covers 17 comorbidities, while the Elixhauser score covers 30. There are 6 overlapping comorbidities between Charlson and Elixhauser comorbidity mappings:

1. congestive heart failure
2. peripheral vascular disease
3. chronic pulmonary disease
4. hemiplegia/paraplegia
5. HIV/AIDS
6. metastatic solid tumors

An example of a Charlson/Elixhauser comorbidty is `congestive heart failure`, which covers the following ICD codes:  

- **428.0:** Congestive heart failure, unspecified
- **428.1:** Left heart failure
- **428.2:** Systolic heart failure
- **428.3:** Diastolic heart failure
- **428.4:** Combined systolic and diastolic heart failure
- **428.9:** Heart failure, unspecified

These comorbidity mappings are able to cluster ICD codes into well-defined categories. This reduces the dimensionality of our clinical dataset, which makes it significantly easier for machine learning models. 

Example of how it works:

```
from medcodes.diagnoses import comorbidities
comorbidities(icd_code=['4280','4284'], mapping='elixhauser')
```

Outputs:

|icd_code|description|elixhauser|
|----|----|-----|
|4280|Congestive heart failure, unspecified|congestive heart failure|
|4284|Combined systolic and diastolic heart failure|congestive heart failure|

### References

1. The World Health Organization. https://www.who.int/medicines/regulation/medicines-safety/toolkit_atc/en/
2. Winnenburg R, Bodenreider O. A framework for assessing the consistency of drug classes across sources. J Biomed Semantics. 2014;5:30. 
3. Perkins AJ, Kroenke K, Unützer J, et al. Common comorbidity scales were similar in their ability to predict health care costs and mortality. J Clin Epidemiol. 2004;57(10):1040–1048. https://www.ncbi.nlm.nih.gov/pubmed/15528055
4. Lix LM, Quail J, Teare G, et al. Performance of comorbidity measures for predicting outcomes in population-based osteoporosis cohorts. Osteoporos Int. 2011;22(10):2633–2643 https://www.ncbi.nlm.nih.gov/pubmed/21305268
5. Lieffers JR, Baracos VE, Winget M, et al. A comparison of Charlson and Elixhauser comorbidity measures to predict colorectal cancer survival using administrative health data. Cancer. 2011;117(9):1957–1965. https://www.ncbi.nlm.nih.gov/pubmed/21509773