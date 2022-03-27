import os

def open_estability(estability:str) -> dict:
    missile     = {}

    with open(estability) as file:
        for l in file:
            aux = l.replace  ( ' ', '')
            aux = aux.replace('\t', '')
            aux = aux.replace('\n', '')
            aux = aux.replace( '#', '')
            if aux != '':
                missile[aux.split(':')[0]] = float(aux.split(':')[1])
    return missile

def open_massProp(massProp:str) -> dict:              
    missileMass = {}           
    name    = []
    totals  = []
    with open(massProp) as file:
        for l in file:
            aux  = l.replace  ('  ','')
            aux  = aux.replace('\n','')
            auxl = aux.split('\t')
            if (auxl[0] == 'Totals'):
                totals = auxl.copy() 
            if (auxl[0] == 'Name'):
                name = auxl.copy()
    for i in range(1,len(name)):
        missileMass[name[i]] = float(totals[i])
    return missileMass
