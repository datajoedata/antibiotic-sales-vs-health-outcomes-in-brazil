import os
import pyarrow as pa
import pyarrow.parquet as pq
from utilities import load_config_and_set_env

config = load_config_and_set_env(bacteria_project\\config.json')


# Função para converter todo o schema para String
def converter_para_string(table):
    """
    Converte todas as colunas da tabela para o tipo String.
    """
    schema = table.schema
    fields = [pa.field(field.name, pa.string()) for field in schema]
    novo_schema = pa.schema(fields)
    
    # Converter a tabela para o novo schema (tudo como String)
    return table.cast(novo_schema)


def concatenar_parquet_em_chunks_pyarrow(folder_path, output_path, chunk_size=200000):
    """
    Lê e concatena arquivos Parquet em chunks, forçando todas as colunas a serem do tipo string.
    
    Args:
    - folder_path (str): Caminho da pasta com os arquivos Parquet.
    - output_path (str): Caminho do arquivo Parquet final.
    - chunk_size (int): Tamanho dos chunks em termos de número de linhas.
    """
    parquet_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.parquet')]

    writer = None
    for file_path in parquet_files:
        print(f"Processando arquivo: {os.path.basename(file_path)}")
        parquet_file = pq.ParquetFile(file_path)

        for i in range(parquet_file.metadata.num_row_groups):
            row_group = parquet_file.read_row_group(i)
            
            # Forçar conversão de todas as colunas para string
            string_columns = [pa.array(row_group.column(col_name).to_pandas().astype(str)) for col_name in row_group.column_names]
            table_string = pa.table(string_columns, names=row_group.column_names)
            
            if writer is None:
                writer = pq.ParquetWriter(output_path, table_string.schema)
            writer.write_table(table_string)

    if writer is not None:
        writer.close()

    print(f"Dados concatenados e salvos em {output_path}.")




# Variáveis de pastas de entrada e saída
folder_paths = config['output_folders']

# Definir a pasta de output final diretamente do config.json
output_path_base = config['output_final']

# Concatenar arquivos para cada tipo de pasta
for folder_name, folder_path in folder_paths.items():
    output_parquet_path = os.path.join(output_path_base, f"{folder_name}_concatenado.parquet")
    print(f"Concatenando arquivos da pasta: {folder_name}")
    concatenar_parquet_em_chunks_pyarrow(folder_path, output_parquet_path)
