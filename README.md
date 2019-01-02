# MedCodes

## Drug Classification

Drugs can be categorized based on attributes such as mechanism of action, chemical structure, function, and metabolic properties. Two different classification systems exist for describing drugs in a clinical setting:

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
- 2nd level: `03` - diuretics
- 3rd level: `C` - high-ceiling diuretics
- 4th level: `A` - sulfonamids
- 5th level: `01` - furosemide

##### 2. Medical Subject Headings (MeSH) classification

MeSH terms are typically used in the context of indexing and retrieval of literature. Unlike ATC's 5-level classification system, MeSH has two parallel classifications: chemical structure, and functional properties ([2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4120719/)). 

## Comorbidities

`International Statistical Classification of Diseases`, also known as ICD, is a classification system used for patient diagnosis. ICD-9 contains 13,000 codes, while ICD-10 has 68,000 codes. At the end of a patient's hospital stay, a list of ICD codes are assigned to that particular hospital admission, which ultimately gets used for reimbursement purposes.  

Comorbidity measures, such as the Charlson comorbidity index and Elixhauser score, are used to cluster the overwhelming number of ICD codes into a smaller subset of well-defined comorbidities. These tools have used in the context of clinical prognosis and comorbidity adjustment in epidemiological outcome studies ([3](https://www.ncbi.nlm.nih.gov/pubmed/15528055), [4](https://www.ncbi.nlm.nih.gov/pubmed/21305268), [5](https://www.ncbi.nlm.nih.gov/pubmed/21509773)). The Charlson comorbidity index covers 17 comorbidities, while the Elixhauser score covers 30. The two comorbidity measures have 6 overlapping comorbidites: 

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

These comorbidity summaries are useful in the context of machine learning, in which each comorbidity can represents a separate feature in the machine learning model. 

### References

1. The World Health Organization. https://www.who.int/medicines/regulation/medicines-safety/toolkit_atc/en/
2. Winnenburg R, Bodenreider O. A framework for assessing the consistency of drug classes across sources. J Biomed Semantics. 2014;5:30. 
3. Perkins AJ, Kroenke K, Unützer J, et al. Common comorbidity scales were similar in their ability to predict health care costs and mortality. J Clin Epidemiol. 2004;57(10):1040–1048. https://www.ncbi.nlm.nih.gov/pubmed/15528055
4. Lix LM, Quail J, Teare G, et al. Performance of comorbidity measures for predicting outcomes in population-based osteoporosis cohorts. Osteoporos Int. 2011;22(10):2633–2643 https://www.ncbi.nlm.nih.gov/pubmed/21305268
5. Lieffers JR, Baracos VE, Winget M, et al. A comparison of Charlson and Elixhauser comorbidity measures to predict colorectal cancer survival using administrative health data. Cancer. 2011;117(9):1957–1965. https://www.ncbi.nlm.nih.gov/pubmed/21509773