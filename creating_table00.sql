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


-- 2 - But now how do I know all rows have been sucessfully imported? 
-- 
