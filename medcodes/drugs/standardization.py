import json
import requests
import pandas as pd
import numpy as np
from tqdm import tqdm
pd.options.mode.chained_assignment = None 


class Drug(object):
    """
    Drug Information
    ================

    Parameters
    ----------
    drug_id : str
        drug name
    id_type : str
        Can be one of: 'name','ndc','rxcui','smiles','iupac'


    Attributes
    ----------
    generic_name : str
        generic name of drug (e.g., clopidogrel)
    brand_name : str
        brand name of drug  (e.g., plavix)
    pharm_class : list of str
        pharmacological classes of the drug. Can be PE (physiological), MOA (mechanism of action),
        or CS (chemical structure)
    route : list of str
        possible routes of administration
    ndc : int
        National Drug Code (NDC) identifier
    rxcui : str
        RxCui identifier
    """
    def __init__(self, drug_id, id_type):
        if id_type not in ['name', 'ndc', 'smiles']:
            raise ValueError("id_type must be one of: 'name', 'smiles', 'ndc'")
        if not isinstance(drug_id, str):
            raise TypeError("drug_id must be a string")
        self.drug_id = drug_id
        self.id_type = id_type
        self.smiles = None
        self.iupac = None
        self.rxcui = None
        self.cid = None

    def get_smiles(self, canonical=True):
        """
        Gets SMILES for drug of interest. 

        Parameters
        ----------
        canonical : bool
            Detemrines whether to get canonical or isomeric SMILES. Default is set to True.
            If False, retrieves isomeric SMILES.
        """
        if self.id_type == 'smiles':
            self.smiles = self.drug_id
        else:
            r = requests.get(f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/{self.id_type}/{self.drug_id}/json")
            response = r.json()
            data = response['PC_Compounds'][0]
            cid = data['id']['id']['cid']
            smiles_type = 'Canonical'
            if not canonical:
                smiles_type = 'Isomeric'
            for i in data['props']:
                if (i['urn']['label'] == 'SMILES') and (i['urn']['name'] == smiles_type):
                    self.smiles = i['value']['sval']
        return self.smiles

    def get_iupac(self):
        if self.id_type == 'iupac':
            self.iupac = self.drug_id
        else:
            r = requests.get(f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/{self.id_type}/{self.drug_id}/json")
            response = r.json()
            smiles = None
            if len(response['PC_Compounds'] == 1):
                data = response['PC_Compounds'][0]
                cid = data['id']['id']['cid']
                for i in data['props']:
                    if (i['urn']['label'] == 'IUPAC Name') and (i['urn']['name'] == 'Preferred'):
                        self.iupac = i['value']['sval']
        return self.iupac

    def describe(self):
        r = requests.get(f"https://api.fda.gov/drug/ndc.json?search=brand_name:{self.name}")
        response = r.json()
        
        for i in response['results']:
            generic_name = i['generic_name']
            brand_name = i['brand_name']
            # pharm_class_moa = i['openfda']['pharm_class_moa']
            # pharm_class_cs = i['openfda']['pharm_class_cs']
            # pharm_class_pe = i['openfda']['pharm_class_pe']
            # pharm_class_epc = i['openfda']['pharm_class_epc']
            pharm_class = i['pharm_class']
            route = i['route']
            self.ndc = i['product_ndc']
        
        print(f"Generic name: {generic_name}")
        print(f"Brand name: {brand_name}")
        print(f"Routes of administration: {route}")
        # print(f"Mechanisms of action: {pharm_class_moa}")
        # print(f"Chemical structure: {pharm_class_cs}")
        # print(f"Physiological effect: {pharm_class_pe}")
        # print(f"EPC (Established Pharmocologic Class): {pharm_class_epc}")
        print(f"Pharmacologic Classes: {pharm_class}")
        print(f"NDC code: {self.ndc}")


    def get_atc(self):
        atc_class_id = []
        atc_class_name = []
        try:
            if self.rxcui:
                r = requests.get(f"https://rxnav.nlm.nih.gov/REST/rxclass/class/byRxcui.json?rxcui={self.rxcui}&relaSource=ATC")
            else:
                r = requests.get(f"https://rxnav.nlm.nih.gov/REST/rxclass/class/byDrugName.json?drugName={self.name}&relaSource=ATC")
                response = r.json()
                concept_groups = response['rxclassDrugInfoList']['rxclassDrugInfo']
                for i in concept_groups:
                    atc_class_name.append(i['rxclassMinConceptItem']['className'])
                    atc_class_id.append(i['rxclassMinConceptItem']['classId'])
        except Exception:
            pass
        return list(set(atc_class_id)), list(set(atc_class_name))

    def get_mesh(self):
        rxclass_list = []
        try:
            if self.rxcui:
                r = requests.get(f"https://rxnav.nlm.nih.gov/REST/rxclass/class/byRxcui.json?rxcui={self.rxcui}&relaSource=MESH")
            else:
                r = requests.get(f"https://rxnav.nlm.nih.gov/REST/rxclass/class/byDrugName.json?drugName={self.name}&relaSource=MESH")
            response = r.json()
            all_concepts = response['rxclassDrugInfoList']['rxclassDrugInfo']
            for i in all_concepts:
                rxclass_list.append(i['rxclassMinConceptItem']['className'])
        except Exception:
            pass
        return list(set(rxclass_list))




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

def get_mesh_class_from_drug_name(drug_name, as_df=False):
    drug_name = drug_name.strip()
    drug_name = drug_name.replace(' ', '+')
    mesh_terms = []
    mesh_id = []
    try:
        r = requests.get(f"https://rxnav.nlm.nih.gov/REST/rxclass/class/byDrugName.json?drugName={drug_name}&relaSource=MESH")
        response = r.json()
        all_concepts = response['rxclassDrugInfoList']['rxclassDrugInfo']
        for i in all_concepts:
            mesh_id.append(i['rxclassMinConceptItem']['classId'])
            mesh_terms.append(i['rxclassMinConceptItem']['className'])
    except:
        pass
    output = list(set(mesh_terms))
    if as_df:
        output = pd.DataFrame({'mesh_id': mesh_id, 'mesh_term':mesh_terms})
        output = output.drop_duplicates()
    return output

def get_atc_info_from_drug_name(drug_name, as_df=True):
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
    output = list(set(atc_class_id))
    if as_df:
        output = pd.DataFrame({'atc_id': atc_class_id, 'description': atc_class_name})
        output = output.drop_duplicates()
    return output