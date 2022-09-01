"""
WIP: Convert elements to Pathlib objects
"""
import os
from pathlib import Path
from re import sub


def binary_exist(bin_name: str) -> Path:
    # checa as referencias
    usr_path = Path('/usr/local') / bin_name
    root_path = Path('/bin') / bin_name
    this_path = Path() / bin_name

    if this_path.exists() and this_path.is_file():
        return this_path
    elif usr_path.exists() and usr_path.is_file():
        return usr_path
    elif root_path.exists() and root_path.is_file():
        return root_path
    else:
        return None


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
            aux = sub(r'\s+', '\t', l)   # Eliminate duplicate whitespaces
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


def open_parasiteDrag(file_name: str) -> dict:
    aircraft = {}
    with open(file_name) as file:
        for l in file:
            aux = sub(r'\s+', '', l)
            aux = aux.replace('\n', '')
            if ':' in aux and aux.split(':')[0] == 'Totals':
                aux = aux.split(':')
                aircraft[aux[0]] = float(aux[1])
    return aircraft


def open_waveDrag(file_name: str) -> dict:
    aircraft = {}
    with open(file_name) as file:
        for l in file:
            aux = l.replace('  ', '')
            aux = aux.replace('\n', '')
            if ':' in aux and aux.split(':')[0] == 'CdWave':
                aux = aux.split(':')
                aircraft[aux[0]] = float(aux[1])
    return aircraft
