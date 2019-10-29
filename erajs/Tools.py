import hashlib
import os
import random
import sys
import secrets


# def new_hash():
#     m = hashlib.md5()
#     m.update(str(random.random()).encode("utf-8"))
#     return m.hexdigest().upper()


def new_hash(level=8):
    """
    # 随机哈希值生成器
    返回随机生成的哈希字符串
    - level == n，返回长度为2n的字符串，在16^n个项目中随机，任意两个值相同的概率为1/16^n/2。
    """
    return secrets.token_hex(level).upper()


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
