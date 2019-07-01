"""
[X] -detect_USB_drives
[ ] -update_software
[ ] -store_data
[ ] -start_GUI
[ ] -update_configs
"""

import sys
import os
from subprocess import PIPE, run
import shutil
from time import sleep


std_disks = ['internal_0', 'rootfs', 'boot']
media_path = "/media/andy/"
code_path = "ARP07"
internal_path = None #media_path + "internal_0"
external_path = None
path_disk_label = "/dev/disk/by-label"

path_internal_dev = "/home/andy/projects/1/data/"
path_external_dev = "/home/andy/projects/2/"


main_running = False        # True if main is running
external_handled = False    # is True if a newly detected disk was checked for updates and file deltas
#software_updated = False


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


def check_disks(disks_label):
    global internal_path
    global external_path
    global main_running
    global external_handled
    global code_path
    found_internal = False
    found_external = False

    for d in disks_label:
        if d[:8] == "internal":
            internal_path = media_path + d
            found_internal = True
        if d not in std_disks:
            print("not in std_disk", d)
            external_path = media_path + d
            found_external = True
    if not found_internal:
        internal_path = None
    if not found_external:
        external_path = None
    print("Internal: ", internal_path)
    print("External: ", external_path)

    if not main_running and internal_path is not None and (external_handled or external_path is None):
        try:
            main_running = True
            run_main(code_path)
        except Exception as e:
            main_running = False
            print("main.py exited: ", e)
    elif internal_path is None:
        main_running = False
    print(main_running)

def run_main(internal_code):
    #import main from internal_code
    print("run_main()")


"""
if get_file_delta(path_internal_dev, path_external_dev):
    print("found deltas!")
    fix_file_deltas(path_internal_dev, path_external_dev)
else:
    print("No deltas found!")
"""
try:
    while True:
        try:
            disks = os.listdir(path_disk_label)
            if disks is not None:
                check_disks(disks)
        except FileNotFoundError as e:
            print("No disks found: ", e)
        sleep(3)
except KeyboardInterrupt:
    pass
