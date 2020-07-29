import os
import shutil
import sys

user_directory_input = input("Enter the path of the directory:")
# user_plan_name_input = input("Enter the name of the plan and short identifier")
extensions = {'f01', 'f02', 'f03'}
# the order they want this to be
new_flow_name =['P100yr','P10yr', 'P25yr', 'P50yr', 'P101yr', 'P500yr']


def check_list_order(list_flows):
    list_len = len(list_flows)
    if list_len > 1:
        if list_flows == ['1%', '10%', '4%', '2%', '1%+', '0.2%\n']:
            return True
        elif list_flows == ['1p', '10p', '4p', '0pt2p', '2p', '1pPLUS\n']:
            return False
        elif list_flows == ['1p', '10p', '4p', '2p', '1pPlus', '0pt2p\n']:
            return True
        elif list_flows == ['1p', '10p', '4p', '2p', '1pPLUS', '0pt2p\n']:
            return True
        elif list_flows == ['FLOW_1p', 'FLOW_10p', 'FLOW_4p', 'FLOW_2p', 'FLOW_1p+', 'FLOW_0.2p','PF 7\n']:
            return 'True_1'
        elif list_flows == ['FLOW_1p', 'FLOW_10p', 'FLOW_4p', 'FLOW_2p', 'FLOW_1p+', 'FLOW_0.2p\n']:
            return True
        elif list_flows == ['10Yr', '25Yr', '50Yr', '100Yr', '100+Yr', '500Yr\n']:
            return 'False1'
        elif list_flows == ['100Yr', 'P10Yr', '50Yr', '100Yr', '100+Yr', '500Yr\n']:
            return 'False2'
        else:
            return 'False3'
    elif list_len == 1:
        if list_flows == ['1p\n']:
            return 'True1'

def rename_flows():
    for models in os.listdir(user_directory_input):
        models_path_up = os.path.join(user_directory_input, models)
        simulation_path = os.path.join(models_path_up, 'Simulations')
        for extension in extensions:
            models_path = os.path.join(simulation_path, f'{models}.{extension}')
            if os.path.exists(models_path):
                with open (models_path,'r') as f:
                    read_lines = f.readlines()
                    searchquery='Plan Title','Short Identifier'
                    new_line = read_lines[3].split('=')[1].split(',')
                    if check_list_order(new_line) == True:
                        if len(new_line) > 1:
                            for line in new_line:
                                if line == '1%' or line == '1p' or line == 'FLOW_1p':
                                    new_line[0] = 'P100yr'
                                elif line == '10%' or line == '10p' or line == 'FLOW_10p':
                                    new_line[1] = 'P10yr'
                                elif line == '4%' or line == '4p' or line == 'FLOW_4p':
                                    new_line[2] = 'P25yr'
                                elif line == '2%' or line == '2p' or line == 'FLOW_2p':
                                    new_line[3] = 'P50yr'
                                elif line == '1%+'or line == '1pPlus' or line == '1pPLUS' or line == 'FLOW_1p+':
                                    new_line[4] = 'P101yr'
                                elif line == '0.2%\n' or line == '0pt2p\n' or line == 'FLOW_0.2p\n':
                                    new_line[5] = 'P500yr'
                            read_lines[3] = read_lines[3].split('=')[0] + '=' + new_line[0] + ','
                            + new_line[1]+','+ new_line[2]+','+ new_line[3]+','+ new_line[4]+','+ new_line[5]+'\n'
                    if check_list_order(new_line) == 'True_1':
                        if len(new_line) > 1:
                            for line in new_line:
                                if  line == 'FLOW_1p':
                                    new_line[0] = 'P100yr'
                                elif line == 'FLOW_10p':
                                    new_line[1] = 'P10yr'
                                elif line == 'FLOW_4p':
                                    new_line[2] = 'P25yr'
                                elif line == 'FLOW_2p':
                                    new_line[3] = 'P50yr'
                                elif line == 'FLOW_1p+':
                                    new_line[4] = 'P101yr'
                                elif line == 'FLOW_0.2p':
                                    new_line[5] = 'P500yr'
                                elif line == 'PF 7\n':
                                    new_line[6] = 'PF7'
                            read_lines[3] = read_lines[3].split('=')[0] + '=' + new_line[0] + ','
                            + new_line[1]+','+ new_line[2]+','+ new_line[3]+','+ new_line[4]+','+ new_line[5]+','+new_line[6]+'\n'

                    elif check_list_order(new_line) == False:
                        if len(new_line) > 1:
                            for line in new_line:
                                if line == '1p':
                                    new_line[0] = 'P100yr'
                                elif line == '10p':
                                    new_line[1] = 'P10yr'
                                elif line == '4p':
                                    new_line[2] = 'P25yr'
                                elif line == '0pt2p':
                                    new_line[3] = 'P500yr'
                                elif line == '2p':
                                    new_line[4] = 'P50yr'
                                elif line == '1pPLUS\n':
                                    new_line[5] = 'P101yr'
                            read_lines[3] = read_lines[3].split('=')[0] + '=' + new_line[0] + ','
                            + new_line[1]+','+ new_line[2]+','+ new_line[3]+','+ new_line[4]+','+ new_line[5]+'\n'
                    elif check_list_order(new_line) == 'False1':
                        if len(new_line) > 1:
                            for line in new_line:
                                if line == '10Yr':
                                    new_line[0] = 'P10yr'
                                elif line == '25Yr':
                                    new_line[1] = 'P25yr'
                                elif line == '50Yr':
                                    new_line[2] = 'P50yr'
                                elif line == '100Yr':
                                    new_line[3] = 'P100yr'
                                elif line == '100+Yr':
                                    new_line[4] = 'P101yr'
                                elif line == '500Yr\n':
                                    new_line[5] = 'P500yr'
                            read_lines[3] = read_lines[3].split('=')[0] + '=' + new_line[0] + ','
                            + new_line[1]+','+ new_line[2]+','+ new_line[3]+','+ new_line[4]+','+ new_line[5]+'\n'
                    elif check_list_order(new_line) == 'True1':
                        if len(new_line) == 1:
                            for line in new_line:
                                if line == '1p\n':
                                    new_line[0] = 'P100yr'
                                read_lines[3] = read_lines[3].split('=')[0] + '=' + new_line[0] +'\n'

                with open (models_path,'w') as f:
                    for lines in read_lines:
                        f.writelines(lines)

if __name__ == '__main__':
    rename_flows()
