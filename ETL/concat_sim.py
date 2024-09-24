import os
import pyarrow as pa
import pyarrow.parquet as pq
from utilities import load_config_and_set_env

# Carregar o arquivo config.json e definir variáveis de ambiente
config = load_config_and_set_env('\\bacteria_project\\config.json')

# Definir as colunas desejadas
desired_columns_c = ['CONTADOR', 'DTOBITO', 'NATURAL', 'CODMUNNATU', 'IDADE', 'SEXO', 'CODMUNRES', 'CODESTAB',
                     'CODMUNOCOR', 'LINHAA', 'LINHAB', 'LINHAC', 'LINHAD', 'LINHAII', 'CAUSABAS', 'CAUSABAS_O',
                     'DTCADASTRO', 'ATESTADO', 'CAUSAMAT', 'STDOEPIDEM']

# Caminho da pasta dos arquivos SIM (definido nas variáveis de ambiente)
folder_path = os.environ['SIM_PARQUET']

# Função para forçar conversão de todas as colunas para string
def converter_para_string(table):
    """
    Converte todas as colunas da tabela para o tipo String.
    """
    schema = table.schema
    fields = [pa.field(field.name, pa.string()) for field in schema]
    novo_schema = pa.schema(fields)
    
    # Converter a tabela para o novo schema (tudo como String)
    return table.cast(novo_schema)

# Função para realizar a ETL dos arquivos SIM
def processar_sim_files(folder_path, output_path, desired_columns, chunk_size=200000):
    """
    Lê e processa arquivos Parquet para selecionar colunas específicas e concatenar em um único arquivo,
    forçando a conversão de todas as colunas para string.
    
    Args:
    - folder_path (str): Caminho da pasta com os arquivos Parquet.
    - output_path (str): Caminho do arquivo Parquet final.
    - desired_columns (list): Lista de colunas desejadas para a seleção.
    - chunk_size (int): Tamanho dos chunks em termos de número de linhas.
    """
    parquet_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.parquet')]

    writer = None
    try:
        for file_path in parquet_files:
            print(f"Processando arquivo: {os.path.basename(file_path)}")
            parquet_file = pq.ParquetFile(file_path)

            for i in range(parquet_file.metadata.num_row_groups):
                row_group = parquet_file.read_row_group(i)
                
                # Converter os dados para string e selecionar colunas desejadas
                row_group_string = converter_para_string(row_group)
                selected_columns = row_group_string.select(desired_columns)

                # Verificar se o writer já foi inicializado
                if writer is None:
                    writer = pq.ParquetWriter(output_path, selected_columns.schema)

                # Escrever os dados selecionados
                writer.write_table(selected_columns)

        # Fechar o writer ao final do processo
        if writer is not None:
            writer.close()
            print(f"Dados filtrados e concatenados salvos em {output_path}.")
        else:
            print(f"Erro: Nenhum dado foi escrito no arquivo {output_path}.")

    except Exception as e:
        print(f"Erro ao processar os arquivos: {str(e)}")
        if writer is not None:
            writer.close()

# Definir caminho de saída para o arquivo concatenado
output_parquet_path = os.path.join(config['output_final'], "sim_concatenado.parquet")
print(f"Verificando saída: {output_parquet_path}")

# Processar os arquivos do SIM
processar_sim_files(folder_path, output_parquet_path, desired_columns_c)

# Verificar se o arquivo foi realmente criado
if os.path.exists(output_parquet_path):
    print(f"O arquivo foi criado com sucesso: {output_parquet_path}")
else:
    print(f"Erro: O arquivo {output_parquet_path} não foi criado.")
