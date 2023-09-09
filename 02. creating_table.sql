-- 1 - Creating table to receive all csv files 
--   (TABLE SCHEMA OR BLUEPRINT)

CREATE TABLE industrialized_meds01 (
    ANO_VENDA INT,
    MES_VENDA INT,
    UF_VENDA VARCHAR(2),
    MUNICIPIO_VENDA NVARCHAR(32),
    PRINCIPIO_ATIVO NVARCHAR(602),
    QTD_VENDIDA INT,
    UNIDADE_MEDIDA NVARCHAR(6),
    CID10 NVARCHAR(4),
    SEXO FLOAT,
    IDADE FLOAT,
    UNIDADE_IDADE FLOAT
);


-- 2 - Use bulk_copy_program.bat script to insert files into industrialized_meds01 table. 




-- 3 - But now how do we know all rows have been sucessfully imported? 


-- We can count number of rows for each Month/year and then compare with the table we counting table. 
-- Remember, this is done after files are inserted in the table.


SELECT MES_VENDA, ANO_VENDA, COUNT(*) AS Quantity
FROM industrialized_meds01
GROUP BY MES_VENDA, ANO_VENDA
ORDER BY ANO_VENDA, MES_VENDA
INTO OUTFILE '/filepath/of/file.csv' -- If your sql server has a built in export function
FIELDS TERMINATED BY ';' -- Optional: Defines the field separator (comma)
LINES TERMINATED BY '\n'; -- Optional: Defines the line separator (newline character)




-- /////////////////////////////////////////////////////////// Below this line is not code /////////////////////////////////////


This was the Output from sql: 
    
| MES_VENDA | ANO_VENDA | Quantidade |
|-----------|-----------|------------|
| 8         | 2016      | 5834235    |
| 9         | 2016      | 5709574    |
| 10        | 2016      | 5668903    |
| 11        | 2016      | 5527562    |
| 12        | 2016      | 5619019    |
| 1         | 2017      | 5440392    |
| 2         | 2017      | 5149754    |
| 3         | 2017      | 6109657    |
| 4         | 2017      | 5691856    |
| 5         | 2017      | 6297176    |
| 6         | 2017      | 6196471    |
| 7         | 2017      | 6164184    |
| 8         | 2017      | 6336582    |
| 9         | 2017      | 6151470    |
| 10        | 2017      | 6146654    |
--                              (...)



-- After comparing tables "matching_00" and "matching_01" 
-- It is evident that all lines were successfully imported.
