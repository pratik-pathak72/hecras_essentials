import os
import shutil
import sys

user_directory_input = input("Enter the path of the directory:")
# user_plan_name_input = input("Enter the name of the plan and short identifier")
extensions = {'p01', 'p02', 'p03'}

def rename_plan():
    for models in os.listdir(user_directory_input):
        models_path_up = os.path.join(user_directory_input, models)
        simulation_path = os.path.join(models_path_up, 'Simulations')
        for extension in extensions:
            models_path = os.path.join(simulation_path, f'{models}.{extension}')
            # print(models_path)
            if os.path.exists(models_path):
                with open (models_path,'r') as f:
                    read_lines = f.readlines()
                    searchquery='Plan Title','Short Identifier'
                    read_lines[0] = read_lines[0].split('=')[0] + '=' + read_lines[0].split('=')[1].replace(read_lines[0].split('=')[1],'Floodplain\n')
                    read_lines[2] = read_lines[2].split('=')[0] + '=' + read_lines[2].split('=')[1].replace(read_lines[2].split('=')[1],'Floodplain\n')
                    # Uncomment the two lines below to check if everything worked
                    # print(models, read_lines[0].split('=')[1], end ='')
                    # print(models, read_lines[2].split('=')[1], end ='')

                with open (models_path,'w') as f:
                    for lines in read_lines:
                        f.writelines(lines)

if __name__ == '__main__':
    rename_plan()
