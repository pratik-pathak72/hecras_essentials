import os
import shutil
import sys

user_directory_input = input("Enter the path of the directory:")

def rename_model_names():
    for models in os.listdir(user_directory_input):
        models_path_up = os.path.join(user_directory_input, models)
        dirname = os.path.basename(models_path_up)
        for path, sub_directories, files in os.walk(models_path_up):
            for subs in sub_directories:
                simulations_folder = os.path.join(models_path_up, subs)
                old_simulations_folder = os.path.join(models_path_up,'Simulations')
                # print(simulations_folder,old_simulations_folder)
                # print(simulations_folder, old_simulations_folder)
                if simulations_folder == old_simulations_folder:
                    print('YAYA')
                else:
                    os.chdir(path)
                    os.rename(simulations_folder, old_simulations_folder)
        simulation_path = os.path.join(models_path_up, 'Simulations')
        for path, sub_directories, files in os.walk(models_path_up):
            for file in files:
                file_name, extension_of_file_name = os.path.splitext(file)
                file_path = os.path.join(simulation_path,file)
                new_file_path = os.path.join(simulation_path,f'{models}{extension_of_file_name}')
                if not os.path.exists(new_file_path):
                    os.chdir(path)
                    os.rename(file_path,new_file_path)


if __name__ == '__main__':
    rename_model_names()
