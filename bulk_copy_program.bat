@echo off

set "server=DESKTOP-AV0JTTN"
set "database=PROJECT2_DRUG_RESISTANT_ANTIBIOTICS"
set "schema=dbo"
set "table=industrialized_meds01"
set "folder_path=C:\Users\ninol\Desktop\PROFESSIONAL\DATA_STORAGE\MEDICAMENTOS"

for %%F in ("%folder_path%\*.csv") do (
    bcp "%database%.%schema%.%table%" in "%%~fF" -S %server% -T -c -t";" -r "\n" -C 1252
)

echo Importação de todos os arquivos concluída.2