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
