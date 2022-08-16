import os
from posixpath import split
from re import sub 

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
            aux = aux.split('\t')
            if aux[0] == 'Totals':
                totals = aux.copy()
            if aux[0] == 'Name':
                name = aux.copy()
    for i in range(1, len(name)):
        aircraft[name[i]] = float(totals[i])
    return aircraft


def open_compGeom(file_name: str) -> dict:
    aircraft = {}
    name = []
    totals = []
    with open(file_name) as file:
        for l in file:
            aux = sub(r'\s+','\t', l)   # Eliminate duplicate whitespaces
            aux = aux.replace('\n', '')
            aux = aux.split('\t')
            if aux[-1] == 'Totals':
                totals = aux.copy()
            if aux[-1] == 'Name':
                name = aux.copy()
    name.reverse()
    totals.reverse()
    for i in range(1, len(name)):
        aircraft[name[i]] = float(totals[i])
    return aircraft


def open_parasiteDrag(file_name:str) -> dict:
    aircraft = {}
    with open(file_name) as file:
        for l in file:
            aux = sub(r'\s+','',l)
            aux = aux.replace('\n','')
            if ':' in aux and aux.split(':')[0] == 'Totals':
                aux = aux.split(':')
                aircraft[aux[0]] = float(aux[1])
    return aircraft


def open_waveDrag(file_name:str) -> dict:
    aircraft = {}
    with open(file_name) as file:
        for l in file:
            aux = l.replace('  ', '')
            aux = aux.replace('\n', '')
            if ':' in aux and aux.split(':')[0] == 'CdWave':
                aux = aux.split(':')
                aircraft[aux[0]] = float(aux[1])
    return aircraft

