import json
import requests
import pandas as pd
import numpy as np
from tqdm import tqdm
pd.options.mode.chained_assignment = None 


def get_rxcui(ndc_code):
    """Gets RxCui for a given NDC."""
    rxcui = None
    try:
        r = requests.get(f"https://rxnav.nlm.nih.gov/REST/rxcui.json?idtype=NDC&id={ndc_code}")
        response = r.json()
        rxcui = response['idGroup']['rxnormId'][0]
    except Exception:
        pass
    return rxcui

def get_mesh_info_from_rxcui(rxcui):
    """Gets MeSH information for a RxCui."""
    rxclass_list = []
    try:
        r = requests.get(f"https://rxnav.nlm.nih.gov/REST/rxclass/class/byRxcui.json?rxcui={rxcui}&relaSource=MESH")
        response = r.json()
        all_concepts = response['rxclassDrugInfoList']['rxclassDrugInfo']
        for i in all_concepts:
            rxclass_list.append(i['rxclassMinConceptItem']['className'])
    except Exception:
        pass
    return list(set(rxclass_list))

def get_atc_class_from_rxcui(rxcui):
    """Gets ATC level-1 class for a given RxCui."""
    atc_class_id = []
    atc_class_name = []
    try:
        r = requests.get(f"https://rxnav.nlm.nih.gov/REST/rxclass/class/byRxcui.json?rxcui={rxcui}&relaSource=ATC")
        response = r.json()
        concept_groups = response['rxclassDrugInfoList']['rxclassDrugInfo']
        for i in concept_groups:
            atc_class_name.append(i['rxclassMinConceptItem']['className'])
            atc_class_id.append(i['rxclassMinConceptItem']['classId'])
    except Exception:
        pass
    return list(set(atc_class_id)), list(set(atc_class_name))

def get_mesh_class_from_drug_name(drug_name):
    drug_name = drug_name.strip()
    drug_name = drug_name.replace(' ', '+')
    rxclass_list = []
    try:
        r = requests.get(f"https://rxnav.nlm.nih.gov/REST/rxclass/class/byDrugName.json?drugName={drug_name}&relaSource=MESH")
        response = r.json()
        all_concepts = response['rxclassDrugInfoList']['rxclassDrugInfo']
        for i in all_concepts:
            rxclass_list.append(i['rxclassMinConceptItem']['className'])
    except:
        pass
    return list(set(rxclass_list))


def get_atc_info_from_drug_name(drug_name):
    drug_name = drug_name.strip()
    drug_name = drug_name.replace(' ', '+')
    atc_class_id = []
    atc_class_name = []
    try:
        r = requests.get(f"https://rxnav.nlm.nih.gov/REST/rxclass/class/byDrugName.json?drugName={drug_name}&relaSource=ATC")
        response = r.json()
        concept_groups = response['rxclassDrugInfoList']['rxclassDrugInfo']
        for i in concept_groups:
            atc_class_name.append(i['rxclassMinConceptItem']['className'])
            atc_class_id.append(i['rxclassMinConceptItem']['classId'])
    except Exception:
        pass
    return list(set(atc_class_id)), list(set(atc_class_name))
