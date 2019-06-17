import sys
import os
from subprocess import PIPE, run


std_disks = ['internal_0', 'rootfs', 'boot']
media_path = "/media/andy/"
path_internal = media_path + "internal_0"
path_disk_label = "/dev/disk/by-label"


def cmd(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout




disks_label = os.listdir(path_disk_label)

#print(os.chroot('/media/andy/internal_0'))
#print(os.listdir(path_internal))
#print(os.listdir(path_disk_label))


def check_disks():
    found = []
    for disk in disks_label:
        if disk not in std_disks:
            found.append(disk)
    return found


# TODO: check directory first level of external disk and data directory of internal disk for deltas
# TODO: copy missing session-folders from internal to external
# TODO: bonus: check external for code-updates and overwrite internal

ex_ls = check_disks()
if ex_ls:
    print(ex_ls)
    ls_lvl_1 = os.listdir(media_path + ex_ls[0])
    print(ls_lvl_1)

