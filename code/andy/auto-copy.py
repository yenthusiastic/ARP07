import sys
import os
from subprocess import PIPE, run
import shutil


std_disks = ['internal_0', 'rootfs', 'boot']
media_path = "/media/andy/"
path_internal = media_path + "internal_0"
path_disk_label = "/dev/disk/by-label"

path_internal_dev = "/home/andy/projects/1/data/"
path_external_dev = "/home/andy/projects/2/"


def cmd(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout


#print(os.chroot('/media/andy/internal_0'))
#print(os.listdir(path_internal))
#print(os.listdir(path_disk_label))


def check_disks(path=path_disk_label):
    disks_label = os.listdir(path)
    found = []
    for disk in disks_label:
        if disk not in std_disks:
            found.append(disk)
    return found


# TODO: finalize disk path routine
# TODO: check external for code-updates and overwrite internal

"""
ex_ls = check_disks(path_disk_label)
if ex_ls:
    print(ex_ls)
    ls_lvl_1 = os.listdir(media_path + ex_ls[0])
    print(ls_lvl_1)
"""


def get_file_delta(path_source, path_target):
    files_delta = []
    files_source = os.listdir(path_source)
    files_target = os.listdir(path_target)
    for file in files_source:
        if file not in files_target:
            files_delta.append(file)
    return files_delta


# copy files from path_source to path_target
# or copy file path_source to path_target
def copy_files(path_source, path_target, files=None):
    if files:
        for file in files:
            #shutil.copy2(path_source+str(file), path_target+str(file))
            shutil.copytree(path_source + str(file), path_target + str(file))
    else:
        pass
        #shutil.copy2(path_source, path_target)
    print("copy: ", files)


def fix_file_deltas(path_source, path_target):
    deltas = get_file_delta(path_source, path_target)
    copy_files(path_source, path_target, deltas)


if get_file_delta(path_internal_dev, path_external_dev):
    print("found deltas!")
    fix_file_deltas(path_internal_dev, path_external_dev)
