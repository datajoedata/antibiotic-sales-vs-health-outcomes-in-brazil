-- 1 - Creating table to receive all csv files

CREATE TABLE industrialized_meds01 (
    ANO_VENDA INT,
    MES_VENDA INT,
    UF_VENDA VARCHAR(2),
    MUNICIPIO_VENDA NVARCHAR(100),
    PRINCIPIO_ATIVO NVARCHAR(400),
    QTD_VENDIDA INT,
    UNIDADE_MEDIDA NVARCHAR(20),
    TIPO_RECEITUARIO VARCHAR(10),
    CID10 NVARCHAR(20),
    SEXO FLOAT,
    IDADE FLOAT,
    UNIDADE_IDADE FLOAT
);


-- 2 - Use bulk_copy_program.bat script to insert files into industrialized_meds01 table. 




-- 3 - But now how do we know all rows have been sucessfully imported? 
-- We can count number of rows for each Month/year and then compare with the pre-processing counting table. 
-- Remember, this is done after files are inserted in the table.


SELECT MES_VENDA, ANO_VENDA, COUNT(*) AS Quantity
FROM industrialized_meds01
GROUP BY MES_VENDA, ANO_VENDA
ORDER BY ANO_VENDA, MES_VENDA
INTO OUTFILE '/filepath/of/file.csv' -- If your sql server has a built int export function
FIELDS TERMINATED BY ';' -- Optional: Defines the field separator (comma)
LINES TERMINATED BY '\n'; -- Optional: Defines the line separator (newline character)




-- /////////////////////////////////////////////////////////// Below this line is not code /////////////////////////////////////


This was the Output from sql: 
    
MES_VENDA | ANO_VENDA | Quantidade | MES_VENDA | ANO_VENDA | Quantidade
---------------------------------------------------------------
1         | 2014      | 4663123   | 7         | 2018      | 6223152
2         | 2014      | 3533508   | 8         | 2018      | 6350802
3         | 2014      | 4770795   | 9         | 2018      | 6020028
4         | 2014      | 4959035   | 10        | 2018      | 6234877
5         | 2014      | 5257118   | 11        | 2018      | 5971368
6         | 2014      | 5009782   | 12        | 2018      | 5903109

1         | 2015      | 4865561   | 1         | 2019      | 5935422
2         | 2015      | 4502370   | 2         | 2019      | 5643020
3         | 2015      | 5349348   | 3         | 2019      | 6172704
4         | 2015      | 5223675   | 4         | 2019      | 6377957
5         | 2015      | 5426557   | 5         | 2019      | 6648167
6         | 2015      | 5443873   | 6         | 2019      | 6400996
7         | 2015      | 5603872   | 7         | 2019      | 6678148
8         | 2015      | 5391089   | 8         | 2019      | 6623992
9         | 2015      | 5309683   | 9         | 2019      | 6471765
10        | 2015      | 5381109   | 10        | 2019      | 6704980
11        | 2015      | 5180851   | 11        | 2019      | 6315752
12        | 2015      | 5309389   | 12        | 2019      | 6265037

1         | 2016      | 4988890   | 1         | 2020      | 6148438
2         | 2016      | 4991500   | 2         | 2020      | 5823817
3         | 2016      | 5717811   | 3         | 2020      | 6056693
4         | 2016      | 5584964   | 4         | 2020      | 4665428
5         | 2016      | 5700066   | 5         | 2020      | 5107922
6         | 2016      | 5794741   | 6         | 2020      | 10725030
7         | 2016      | 5777788   | 8         | 2020      | 5731510
8         | 2016      | 5834235   | 9         | 2020      | 5569884
9         | 2016      | 5709574   | 10        | 2020      | 5836524
10        | 2016      | 5668903   | 11        | 2020      | 5943344
11        | 2016      | 5527560   | 12        | 2020      | 6252301

1         | 2017      | 5440391   | 1         | 2021      | 6176002
2         | 2017      | 5149754   | 2         | 2021      | 5887180
3         | 2017      | 6109657   | 3         | 2021      | 6617928
4         | 2017      | 5691856   | 4         | 2021      | 5981844
5         | 2017      | 6297175   | 5         | 2021      | 6280707
6         | 2017      | 6196471   | 6         | 2021      | 6277958
7         | 2017      | 6164184   | 7         | 2021      | 6300744
8         | 2017      | 6336581   | 8         | 2021      | 6263825
9         | 2017      | 6151469   | 9         | 2021      | 6131691
10        | 2017      | 6146653   | 10        | 2021      | 5989708
11        | 2017      | 5951772   |
12        | 2017      | 5888916   |




-- 
