import os
import json
import pandas as pd
from utilities import set_environment_variables

# Carregar o arquivo config.json
with open('\\bacteria_project\\config.json', 'r') as file:
    config = json.load(file)

# Chamar a função set_environment_variables
set_environment_variables(config)

# Função para listar os arquivos dentro de um diretório
def get_file_paths(folder_path):
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Função para verificar se o arquivo Parquet já existe
def parquet_exists(file_path, output_folder):
    parquet_path = os.path.join(output_folder, os.path.basename(file_path).replace('.csv', '.parquet').replace('.xls', '.parquet').replace('.xlsx', '.parquet'))
    return os.path.exists(parquet_path)

# Função para converter arquivos CSV, XLS, ou XLSX para o formato Parquet
def convert_to_parquet(file_path, output_folder):
    try:
        if parquet_exists(file_path, output_folder):
            print(f"Arquivo {file_path} já convertido para Parquet. Pulando...")
            return

        # Converter CSV para Parquet
        if file_path.endswith(".csv"):
            print(f"Convertendo arquivo CSV {file_path} para Parquet...")
            df = pd.read_csv(file_path, delimiter=';', encoding='latin-1', dtype=str)
            parquet_path = os.path.join(output_folder, os.path.basename(file_path).replace('.csv', '.parquet'))
            df.to_parquet(parquet_path, index=False)
            print(f"Arquivo {file_path} convertido para {parquet_path}.")

        # Converter Excel (XLS/XLSX) para Parquet
        elif file_path.endswith(".xls") or file_path.endswith(".xlsx"):
            print(f"Convertendo arquivo Excel {file_path} para Parquet...")
            df = pd.read_excel(file_path, engine='openpyxl', dtype=str)
            parquet_path = os.path.join(output_folder, os.path.basename(file_path).replace('.xls', '.parquet').replace('.xlsx', '.parquet'))
            df.to_parquet(parquet_path, index=False)
            print(f"Arquivo {file_path} convertido para {parquet_path}.")
        
        else:
            print(f"Formato de arquivo não suportado: {file_path}")

    except Exception as e:
        print(f"Erro ao converter {file_path} para Parquet: {str(e)}")

# Função para definir as pastas de saída conforme o tipo de arquivo
def get_output_folder_for_file_type(folder_name):
    if 'industrialized' in folder_name:
        return os.environ['INDUSTRIALIZED_PARQUET']
    elif 'manipulated' in folder_name:
        return os.environ['MANIPULATED_PARQUET']
    elif 'raw_sim_files' in folder_name:
        return os.environ['SIM_PARQUET']
    else:
        return os.environ['IBGE_PARQUET']

# Processar os arquivos e convertê-los em Parquet
for folder_name, folder_path in config['folder_paths'].items():
    absolute_path = os.path.abspath(folder_path)
    print(f"Processando arquivos na pasta: {absolute_path}")

    # Definir a pasta de saída com base no tipo de arquivo
    output_folder = get_output_folder_for_file_type(folder_name)
    os.makedirs(output_folder, exist_ok=True)

    # Listar arquivos dentro da pasta e convertê-los para Parquet
    file_paths = get_file_paths(absolute_path)
    for file_path in file_paths:
        convert_to_parquet(file_path, output_folder)
