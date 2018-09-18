# coding:utf-8
import os
import sys
import csv
import json
import configparser


def init():
    fix_path()
    fileList = {
        'plugin': scan_plugin(),
        'config': scan_config(),
        'game': scan_game(),
        'dlc': scan_dlc(),
        'save': scan_save(),
    }
    return fileList


def fix_path():
    if getattr(sys, 'frozen', False):
        # frozen
        d = os.path.dirname(sys.executable)
        gamepath = os.path.dirname(d)
    else:
        # unfrozen
        d = os.path.dirname(os.path.realpath(__file__))
        gamepath = os.path.dirname(os.path.dirname(d))
    sys.path.append(gamepath)


def scan_plugin():
    return scan('plugin')


def scan_config():
    return scan('config')


def scan_game():
    return scan('game')


def scan_dlc():
    return scan('dlc')


def scan_save():
    return scan('save')


def scan(folderName):
    fileList = []
    for root, dirs, files in os.walk(folderName):
        for each in files:
            fileList.append(root + '\\' + each)
    return fileList
