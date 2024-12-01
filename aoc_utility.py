import os

def construtct_input_file_name(code_file_name):
    problem_number = code_file_name.split('/')[-1].split('.')[0]
    return problem_number + '.txt'

def read_input(code_file_name, strip=False):
    inputs_location = os.environ['AOC_INPUTS_LOC']
    with open(inputs_location + '/' + construtct_input_file_name(code_file_name) ,'r+') as f:
        input_data = f.read()
    if strip:
        return input_data.strip()
    else:
        return input_data
