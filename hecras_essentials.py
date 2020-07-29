#title           :file_copy.py
#description     :This script will create excel files, folders, rasmap file, run hecras models and copy projection files.
#author          :Pratik Pathak
#date            :20200626
#version         :0.4
#usage           :python projection_file_to_copy.py
#notes           :Please contact Pratik if the code fails for bug fix
#python_version  :3.8
#==============================================================================

# Import the modules needed to run the script.
import os
import shutil
import sys
import datetime
import fileinput
import win32com.client

# timenow
time_now = str(datetime.datetime.now().strftime('%y-%m-%d_%a_%H:%M:%S'))

# Asking the user to input the AFG style folder where all the models are
print("--------------------------------------------------------------")
user_directory_input = input("Enter the path of the directory:")

# Checking if the folder exists or not
# if os.path.isdir(user_directory_input):
#     print("This Directory exists")
# else:
#     print("This Directory doesn't exist")

# Asking the user to input the file to copy
user_file_input = input("Enter the path of the file that you want to copy along with the extension:")
file_name_with_extension = os.path.basename(user_file_input)
# folder_name_with_extension
file_name, extension_of_file_name = os.path.splitext(file_name_with_extension)
rasmap_file_to_copy = r'C:\python_projects\project_1\test_data\LITCACPN.rasmap'
projection_file_to_copy = input("Provide the path of Projection file to copy along with extension:")
prj_file_name_with_extension = os.path.basename(projection_file_to_copy)
prj_file_name, prj_extension_of_file_name = os.path.splitext(prj_file_name_with_extension)
# remove_file = input("Do you want to remove any file (Y/N):")
#
# if remove_file.lower() == 'y':
#     file_to_delete = input ('Enter the file to delete with full extension:')
#     try:
#         shutil.rmtree(file_to_delete)
#     except OSError as e:
#         print('Error: %s - %s.' % (e.filename, e.strerror))

def input_folder():
    folder_input = input("How many folders you want to create?:")
    if int(folder_input) > 0:
        for folder in range(int(folder_input)):
            folder = input("Enter the name of the folder:")
            for models in os.listdir(user_directory_input):
                models_path = os.path.join(user_directory_input, models)
                folder_path = os.path.join(models_path, folder)
                if os.path.exists(folder_path):
                    continue
                else:
                    os.makedirs(folder_path)


def prj_file_to_copy():
    for models in os.listdir(user_directory_input):
        models_path = os.path.join(user_directory_input, models)
        join_path = os.path.join(models_path, prj_file_name_with_extension)
        if os.path.exists(join_path):
            os.remove(join_path)
            shutil.copy2(projection_file_to_copy, models_path)
        else:
            shutil.copy2(projection_file_to_copy, models_path)

def excel_file_copy():
    for models in os.listdir(user_directory_input):
        models_path = os.path.join(user_directory_input, models)
        join_path = os.path.join(models_path, file_name_with_extension)
        new_name = os.path.join(models_path , f'{file_name}_{models}{extension_of_file_name}')
        rasmap_file = os.path.join(models_path , f'{models}.rasmap')
        if os.path.exists(join_path):
            os.remove(join_path)
            shutil.copy2(user_file_input, models_path)
            os.rename(join_path, new_name)
        elif os.path.exists(new_name):
            pass
        else:
            shutil.copy2(user_file_input, models_path)
            os.rename(join_path, new_name)

def create_rasmap():
    for models in os.listdir(user_directory_input):
        models_path = os.path.join(user_directory_input, models)
        join_path = os.path.join(models_path, file_name_with_extension)
        new_name = os.path.join(models_path , f'{file_name}_{models}{extension_of_file_name}')
        rasmap_file = os.path.join(models_path , f'{models}.rasmap')
        with open (rasmap_file_to_copy, 'r') as f:
            with open (rasmap_file, 'w') as f1:
                for line in f:
                    f1.write(line)

            f2 = open(rasmap_file,'r')
            filedata = f2.read()
            f2.close()

            newdata = filedata.replace("LITCACPN",f'{models}')

            f2 = open(rasmap_file,'w')
            f2.write(newdata)
            f2.close()

def edit_po1():
    for models in os.listdir(user_directory_input):
        models_path = os.path.join(user_directory_input, models)
        models_path_p01 = os.path.join(models_path, f'{models}.p01')
        match_string = "Run PostProcess= 0"
        insert_string = "Run RASMapper= -1"
        check_string = "Run RASMapper= 0"
        with open(models_path_p01, 'r+') as fd:
            contents = fd.readlines()
            for index, line in enumerate(contents):
                if line.startswith(match_string) and insert_string not in contents[index + 1] and insert_string not in contents[index + 2] and insert_string not in contents[index + 3] :
                    contents.insert(index + 1, insert_string + "\n")
                    break
            fd.seek(0)
            fd.writelines(contents)

def run_ras():
    RC507=win32com.client.Dispatch("RAS507.HECRASCONTROLLER") # HECRAS 507
    for models in os.listdir(user_directory_input):
        models_path = os.path.join(user_directory_input, models)
        models_path_prj = os.path.join(models_path, f'{models}.prj')
        TabMsg, NMsg, block = None, None, True
        RC507.ShowRas()
        RC507.Project_Open(models_path_prj)
        RC507.Compute_CurrentPlan(NMsg, TabMsg,block)
        RC507.Project_Close()
        RC507.QuitRas()

def main():
    excel_file_copy()
    prj_file_to_copy()
    create_rasmap()
    edit_po1()
    input_folder()
    run_ras()


if __name__ == '__main__':
    main()
