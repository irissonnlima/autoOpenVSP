import os
from ssl import ALERT_DESCRIPTION_UNSUPPORTED_CERTIFICATE


def open_estability(file_name: str) -> dict:
    aircraft = {}

    with open(file_name) as file:
        for l in file:
            aux = l.replace(' ', '')
            aux = aux.replace('\t', '')
            aux = aux.replace('\n', '')
            aux = aux.replace('#', '')
            if aux != '':
                aircraft[aux.split(':')[0]] = float(aux.split(':')[1])
    return aircraft


def open_massProp(file_name: str) -> dict:
    aircraft = {}
    name = []
    totals = []
    with open(file_name) as file:
        for l in file:
            aux = l.replace('  ', '')
            aux = aux.replace('\n', '')
            auxl = aux.split('\t')
            if auxl[0] == 'Totals':
                totals = auxl.copy()
            if auxl[0] == 'Name':
                name = auxl.copy()
    for i in range(1, len(name)):
        aircraft[name[i]] = float(totals[i])
    return aircraft

def open_waveDrag(file_name:str) -> dict:
    aircraft = {}
    name = []
    totals = []
    with open(file_name) as file:
        for l in file:
            aux = l.replace('  ', '')
            aux = aux.replace('\n', '')
            auxl = aux.split(':')
            if auxl[0] == 'CdWave':
                aircraft[auxl[0]] = float(auxl[1])
    return aircraft