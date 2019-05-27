import sys
import os
from subprocess import PIPE, run


def cmd(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout


ls = cmd("ls /dev/disk/by-label/")

print(ls)
