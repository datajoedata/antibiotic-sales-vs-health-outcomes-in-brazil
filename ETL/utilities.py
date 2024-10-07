import os
import json

# Função para carregar o arquivo config.json e definir as variáveis de ambiente
def load_config_and_set_env(config_path):
    """
    Carrega o arquivo config.json e define as variáveis de ambiente.
    
    Args:
    - config_path (str): Caminho para o arquivo de configuração config.json.
    
    Returns:
    - config (dict): O conteúdo do arquivo config.json como dicionário.
    """
    # Carregar o arquivo config.json
    with open(config_path, 'r') as file:
        config = json.load(file)

    # Chamar a função que define as variáveis de ambiente
    set_environment_variables(config)

    return config

# Função para definir variáveis de ambiente a partir do config.json
def set_environment_variables(config):
    """
    Define variáveis de ambiente a partir do arquivo de configuração.
    
    Args:
    - config (dict): Dicionário com os valores de configuração.
    """
    for key, value in config.get('folder_paths', {}).items():
        os.environ[key.upper()] = value
        print(f"Variável de ambiente {key.upper()} definida com sucesso.")

    for key, value in config.get('output_folders', {}).items():
        os.environ[key.upper()] = value
        print(f"Variável de ambiente {key.upper()} definida com sucesso.")





# Função para listar os arquivos dentro de um diretório
def get_file_paths(folder_path):
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]



# Função para verificar se o arquivo Parquet já existe
def parquet_exists(file_path, output_folder):
    parquet_path = os.path.join(output_folder, os.path.basename(file_path).replace('.csv', '.parquet').replace('.xls', '.parquet').replace('.xlsx', '.parquet'))
    return os.path.exists(parquet_path)


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
