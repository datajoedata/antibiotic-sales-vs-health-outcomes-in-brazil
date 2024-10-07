import os 
import json
import pandas as pd
from utilities import set_environment_variables, get_file_paths, parquet_exists, get_output_folder_for_file_type 

# Carregar o arquivo config.json
with open('C:\\Users\\ninol\\Desktop\\PROFESSIONAL\\projects\\bacteria_project\\config.json', 'r') as file:
    config = json.load(file)

# Chamar a função set_environment_variables
set_environment_variables(config)

# Função para converter arquivos CSV, XLS, ou XLSX para o formato Parquet
def convert_to_parquet(file_path, output_folder, encoding, selected_columns=None):
    try:
        if parquet_exists(file_path, output_folder):
            print(f"Arquivo {file_path} já convertido para Parquet. Pulando...")
            return

        # Converter CSV para Parquet
        if file_path.endswith(".csv"):
            print(f"Convertendo arquivo CSV {file_path} para Parquet...")
            df = pd.read_csv(file_path, delimiter=';', encoding=encoding, dtype=str, usecols=selected_columns)
            parquet_path = os.path.join(output_folder, os.path.basename(file_path).replace('.csv', '.parquet'))
            df.to_parquet(parquet_path, index=False)
            print(f"Arquivo {file_path} convertido para {parquet_path}.")

        # Converter Excel (XLS/XLSX) para Parquet
        elif file_path.endswith(".xls") or file_path.endswith(".xlsx"):
            print(f"Convertendo arquivo Excel {file_path} para Parquet...")
            df = pd.read_excel(file_path, engine='openpyxl', dtype=str, usecols=selected_columns)
            parquet_path = os.path.join(output_folder, os.path.basename(file_path).replace('.xls', '.parquet').replace('.xlsx', '.parquet'))
            df.to_parquet(parquet_path, index=False)
            print(f"Arquivo {file_path} convertido para {parquet_path}.")

        else:
            print(f"Formato de arquivo não suportado: {file_path}")

    except UnicodeDecodeError as e:
        print(f"Erro ao converter {file_path} para Parquet: Problema de codificação - {str(e)}")
    except Exception as e:
        print(f"Erro ao converter {file_path} para Parquet: {str(e)}")

# Processar os arquivos e convertê-los em Parquet
for folder_name, folder_path in config['folder_paths'].items():
    absolute_path = os.path.abspath(folder_path)
    print(f"Processando arquivos na pasta: {absolute_path}")

    # Definir a pasta de saída com base no tipo de arquivo
    output_folder = get_output_folder_for_file_type(folder_name)
    os.makedirs(output_folder, exist_ok=True)

    # Obter a codificação específica para a pasta
    encoding = config['folder_encodings'].get(folder_name, 'cp1252')  # Usando 'cp1252' como padrão

    # Selecionar colunas apenas para 'raw_sim_files'
    selected_columns = None
    if folder_name == 'raw_sim_files':
        selected_columns = ['CONTADOR', 'DTOBITO', 'NATURAL', 'CODMUNNATU', 'IDADE', 'SEXO', 'CODMUNRES', 'CODESTAB',
                            'CODMUNOCOR', 'LINHAA', 'LINHAB', 'LINHAC', 'LINHAD', 'LINHAII', 'CAUSABAS', 'CAUSABAS_O',
                            'DTCADASTRO', 'ATESTADO', 'CAUSAMAT', 'STDOEPIDEM']

    # Listar arquivos dentro da pasta e convertê-los para Parquet
    file_paths = get_file_paths(absolute_path)
    processed_files_count = 0
    for file_path in file_paths:
        convert_to_parquet(file_path, output_folder, encoding, selected_columns if folder_name == 'raw_sim_files' else None)
        processed_files_count += 1

    print(f"Processamento da pasta '{folder_name}' concluído. Total de arquivos convertidos: {processed_files_count}")

print("Processamento finalizado.")
