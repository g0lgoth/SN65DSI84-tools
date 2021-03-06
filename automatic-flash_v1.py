import os
from tkinter import *
import subprocess

def read_input(doc):
    with open(doc) as input_list:
        input_list = input_list.readlines()
        # j'enlève le saut de page
        input_list[1] = input_list[1].rstrip("\n")
        adresses_list = input_list[1].split(" ")
        input_list[4] = input_list[4].rstrip("\n")
        values_list = input_list[4].split(" ")      
    return adresses_list, values_list

def folder_list_creation(folder_path):
    folder_list = []
    for folder_name in os.listdir(folder_path):
        folder_list.append(folder_name)
        print(folder_name, "\n")
    return folder_list

def batch_cration(adb_path, local_path):
    batch_directory_move = os.chdir(local_path)
    with open('sn65dsi84.bat', 'w') as batch:
        batch.write('cd "{}"\n'.format(adb_path))
        batch.write('adb wait-for-device\n')
        batch.write('adb root\n')
        batch.write('adb disable-verity\n')
        batch.write('adb reboot\n')
        batch.write('adb wait-for-device\n')
        batch.write('adb root\n')
        batch.write('adb wait-for-device\n')
        batch.write('adb remount\n')
        batch.write('adb wait-for-device\n')
        batch.write('TIMEOUT 5\n')
        batch.write('adb push "C:\\platform-tools_r28.0.1-windows\\script gogo\\sn65dsi84.sh" /system/bin\n')
        batch.write('adb wait-for-device\n')
        batch.write('adb shell chmod +x /system/bin/sn65dsi84.sh\n')
        batch.write('adb wait-for-device\n')
        batch.write('adb shell ./system/bin/sn65dsi84.sh\n')
        batch.close()
    # procId = subprocess.Popen('adb shell', stdin = subprocess.PIPE)
    # procId.communicate('./system/bin/sn65dsi84.sh')
    subprocess.call([r'{}sn65dsi84.bat'.format(local_path)])

def button_creation(list, adb_path, local_path):
    root = Tk()
    for item in list:
        button = Button(root, text=item, command=button_interpreter(item, adb_path, local_path))
        # button = Button(root, text=item, command=lambda x=item: func(x))
        button.pack()
    root.mainloop()

def button_interpreter(item, adb_path, local_path):
    batch_directory_move = os.chdir(local_path)
    with open('flash.bat', 'w') as batch:
        batch.write('set android_path={}}'.format(adb_path))
        batch.write('%android_path%\\adb.exe reboot bootloader')
        batch.write('adb wait-for-device\n')
    file_system_list = os.listdir("{}\\{}".format(local_path, item))
    print("PROUT", file_system_list)
    if "boot.img" in file_system_list:
        with open('flash.bat', 'w') as batch:
            batch.write('%android_path%\\fastboot.exe flash boot %system_path%\\boot.img')
    if "dtbo.img" in file_system_list:
        with open('flash.bat', 'w') as batch:
            batch.write('%android_path%\\fastboot.exe flash dtbo %system_path%\\dtbo.img')
    if "vendor.img" in file_system_list:
        with open('flash.bat', 'w') as batch:
            batch.write('%android_path%\\fastboot.exe flash vendor %system_path%\\vendor.img')
    if "vbmeta.img" in file_system_list:
        with open('flash.bat', 'w') as batch:
            batch.write('%android_path%\\fastboot.exe flash vbmeta %system_path%\\vbmeta.img')
    if "system.img" in file_system_list:
        with open('flash.bat', 'w') as batch:
            batch.write('%android_path%\\fastboot.exe flash system -S256M %system_path%\\system.img')
    if "userdata.img" in file_system_list:
        with open('flash.bat', 'w') as batch:
            batch.write('%android_path%\\fastboot.exe flash userdata %system_path%\\userdata.img')
    batch_directory_move = os.chdir(local_path)
    with open('flash.bat', 'w') as batch:
        batch.write('adb wait-for-device\n')
    batch.close()
    subprocess.call([r'{}flash.bat'.format(local_path)])

def system_file_checker(item, android_path, system_path):
    if ".boot" in item:
        "{}\\fastboot.exe flash boot %{}\\boot.img".format(android_path, system_path)

def folder_course(system_path, android_path, entry_list):
    for list_value in entry_list:
        system_location = "{}\\{}".format(system_path, list_value)
        for item in location:
            system_file_checker(item, android_path, system_location)

def main():
    folder_path = "C:\\platform-tools_r28.0.1-windows\\system"
    adb_path = "C:\\platform-tools_r28.0.1-windows\\"
    folder_list = folder_list_creation(folder_path)
    print("{}\\{}".format(folder_path, folder_list[0]))
    button_creation(folder_list, adb_path, folder_path)

if __name__ == "__main__":
    main()