import pandas as pd
import glob

# Obter a lista de todos os arquivos CSV na pasta
folder_path = r"C:\Users\ninol\Desktop\PROFESSIONAL\DATA_STORAGE\MEDICAMENTOS"
csv_files = glob.glob(folder_path + "/*.csv")

# Iterar sobre cada arquivo CSV e executar o código
for file_path in csv_files:
    # Carregar o arquivo CSV em um DataFrame do Pandas com encoding "cp1252"
    df = pd.read_csv(file_path, sep=";", encoding="cp1252")

    # Drop columns 'DESCRICAO_APRESENTACAO', 'CONSELHO_PRESCRITOR', 'UF_CONSELHO_PRESCRITOR'
    columns_to_drop = ['DESCRICAO_APRESENTACAO', 'CONSELHO_PRESCRITOR', 'UF_CONSELHO_PRESCRITOR']
    df.drop(columns=columns_to_drop, inplace=True)

    # Salvar o DataFrame modificado em um novo arquivo CSV
    output_file_path = file_path[:-4] + "_modified.csv"  # Adiciona "_modified" ao nome do arquivo
    df.to_csv(output_file_path, index=False, sep=";", encoding="cp1252")