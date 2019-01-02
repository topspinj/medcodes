import json
import requests
import lxml.html as lh
from lxml.html import fromstring
import pandas as pd

class Authentication:
    """Authentication for UMLS API."""
    def __init__(self, apikey):
        self.apikey=apikey
        self.service="http://umlsks.nlm.nih.gov"
        self.uri="https://utslogin.nlm.nih.gov"
        self.auth_endpoint = "/cas/v1/api-key"
        
    def gettgt(self):
        params = {'apikey': self.apikey}
        h = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "User-Agent":"python" }
        r = requests.post(self.uri+self.auth_endpoint,data=params,headers=h)
        response = fromstring(r.text)
        tgt = response.xpath('//form/@action')[0]
        return tgt
    
    def getst(self,tgt):
        params = {'service': self.service}
        h = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "User-Agent":"python" }
        r = requests.post(tgt,data=params,headers=h)
        st = r.text
        return st


def search_string(string, apikey):
    """
    Gets search results for a string.

    Params
    ------
    string : str
        drug name, diagnosis, procedure
    
    apikey : str
        UMLS API key
    
    Returns
    -------
    list of dicts
    """
    uri = "https://uts-ws.nlm.nih.gov"
    a = Authentication(apikey=apikey)
    tgt = a.gettgt()
    ticket = a.getst(tgt)
    content_endpoint = "/rest/search/current"

    query = {'string':string,'ticket':ticket}
    r = requests.get(uri+content_endpoint,params=query)
    r.encoding = 'utf-8'
    items  = json.loads(r.text)
    results = items['result']['results']
    cui = []
    name = []
    source = []
    for i in results:
        cui.append(i['ui'])
        name.append(i['name'])
        source.append(i['rootSource'])
    data = pd.DataFrame({'cui': cui, 'name': name, 'root_source': source})
    return data

def get_cui_info(cui, apikey, infotype=None):
    """
    Gets information for a given CUI.
    
    Params
    ------
    cui : str
        Concept Unique Identifier defined by UMLS.
        You can find the CUI of a drug, diagnosis, procedure
        using get_cui() or search_string().
    
    apikey : str
        UMLS API key
    
    infotype : str
        Can be one of 'definitions', 'atoms', 'relations'.
        If None, will output all generic info.
    """
    uri = "https://uts-ws.nlm.nih.gov"
    a = Authentication(apikey=apikey)
    tgt = a.gettgt()
    ticket = a.getst(tgt)
    content_endpoint = f"/rest/content/current/CUI/{cui}"
    if infotype is not None:
        content_endpoint = f"/rest/content/current/CUI/{cui}/{infotype}"
    query = {'ticket':ticket}
    r = requests.get(uri+content_endpoint,params=query)
    r.encoding = 'utf-8'
    items  = json.loads(r.text)
    return items