REM The lines starting with REM are comments that explain what each variable is for. ###########

REM What is the BCP?  #########
REM The bulk copy program (bcp) utility bulk copies data between an instance of SQL Server and a data file in a user-specified format. ##########

@echo off

REM 1-  Setting up variables like server, database, schema, table, and folder path: ###########

set "server= your_server_here"

set "database= your_database_here"

set "schema=dbo"

set "table=your_target_table_name_here"

set "folder_path=your_folder_path_here"



REM 2- This code below Loops through all CSV files in the specified folder  ###########

for %%F in ("%folder_path%\*.csv") do (
    REM Using BCP (Bulk Copy Program) to import data from each CSV file to SQL Server 
    bcp "%database%.%schema%.%table%" in "%%~fF" -S %server% -T -c -t";" -r "\n" -C 1252
)

REM Displaying a message indicating the completion of the import process for all files  ###########

echo Data import completed.
