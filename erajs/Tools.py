import hashlib
import os
import random
import sys


def new_hash():
    m = hashlib.md5()
    m.update(str(random.random()).encode("utf-8"))
    return m.hexdigest().upper()


def fix_path():
    if getattr(sys, 'frozen', False):
        # frozen
        d = os.path.dirname(sys.executable)
        gamepath = os.path.dirname(d)
        workingpath = d
    else:
        # unfrozen
        d = os.path.dirname(os.path.realpath(__file__))
        gamepath = os.path.dirname(os.path.dirname(d))
        workingpath = os.path.dirname(d)
    sys.path.append(gamepath)
    os.chdir(workingpath)
