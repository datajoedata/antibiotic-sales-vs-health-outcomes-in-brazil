-- 4.0  First I've manually defined an antibiotics list that is used to treat drug resistant bacteria.  

-- 4.1  Now we need to separate antibiotics of interest from all the controlled substances.  

-- There were two approaches in this case:

-- Deleting rows that don't have any antibiotics of interest in it. Or we could create a 
-- new table with the same blueprint to receive values from a normal filtering where one of the antibiotics is found.

-- 4.1.1 At this point, I aimed the quicker approach. While deletion carries integrity risks unless backed up (which I had), I mistakenly assumed deletion to be the swifter option.
-- Upon further investigation, I discovered that the second method is, in fact, faster. This is attributed to the fact that for each row that requires deletion, the database must execute supplementary tasks,
-- such as index maintenance, statistic updates, change logging, and potentially data reorganization.



-- 4.2 The code: 


-- 4.2.1 Creating a table with the previous blueprint to receive values: (I also translated columns values to eng. here)

CREATE TABLE antibiotics_meds01 (
    year INT,
    month INT,
    state VARCHAR(2),
    city NVARCHAR(32),
    active_ingredient NVARCHAR(602),
    quantity_sold INT,
    measurement_unit NVARCHAR(6),
    prescription_type VARCHAR(3),
    ICD_10 NVARCHAR(4),
    gender FLOAT,
    age FLOAT,
    age_unit FLOAT
);

-- 4.2.2 Inserting data that meet the criteria from antibiotics list into the new table and change column names to English:

INSERT INTO antibiotics_meds01
SELECT
    ANO_VENDA AS year,
    MES_VENDA AS month,
    UF_VENDA AS state,
    MUNICIPIO_VENDA AS city,
    PRINCIPIO_ATIVO AS active_ingredient,
    QTD_VENDIDA AS quantity_sold,
    UNIDADE_MEDIDA AS measurement_unit,
    TIPO_RECEITUARIO AS prescription_type,
    CID10 AS ICD_10,
    SEXO AS gender,
    IDADE AS age,
    UNIDADE_IDADE AS age_unit
FROM industrialized_meds01
WHERE PRINCIPIO_ATIVO IN (
    
    'DIPROPIONATO DE BETAMETASONA + SULFATO DE GENTAMICINA',
    'DESONIDA + SULFATO DE GENTAMICINA',
    'CLIOQUINOL + SULFATO DE GENTAMICINA + TOLNAFTATO + VALERATO DE BETAMETASONA',
    'SULFATO DE GENTAMICINA',
    '17-VALERATO DE BETAMETASONA + CLIOQUINOL + SULFATO DE GENTAMICINA + TOLNAFTATO',
    'FOSFATO DISSÓDICO DE BETAMETASONA + SULFATO DE GENTAMICINA',
    'DESXIRRIBONUCLEASE + FIBRINOLISINA + SULFATO DE GENTAMICINA',
    'FOSFATO DISSÓDICO DE BETAMETASONA + GENTAMICINA',
    'LEVETIRACETAM',
    'SULFATO DE AMICACINA',
    'SULFATO DE TOBRAMICINA',
    'ETABONATO DE LOTEPREDNOL + TOBRAMICINA',
    'DEXAMETASONA + TOBRAMICINA',
    'TOBRAMICINA',
    'CLORIDRATO DE CIPROFLOXACINO MONOIDRATADO',
    'CLORIDRATO DE CIPROFLOXACINO MONOIDRATADO + DEXAMETASONA',
    'CLORIDRATO DE CIPROFLOXACINO',
    'CLORIDRATO DE CIPROFLOXACINO + DEXAMETASONA',
    'CIPROFLOXACINO + HIDROCORTISONA MICRONIZADA',
    'CIPROFLOXACINO + CLORIDRATO DE CIPROFLOXACINO',
    'CIPROFLOXACINO',
    'CIPROFLOXACINO + DEXAMETASONA',
    'CLORIDRATO DE CIPROFLOXACINO + HIDROCORTISONA',
    'CLORIDRATO DE CIPROFLOXINA H2O + CLORIDRATO DE CIPROFLOXACINO MONOIDRATADO',
    'AMOXICILINA TRI-HIDRATADA + LANSOPRAZOL + LEVOFLOXACINO',
    'LEVOFLOXACINO',
    'LEVOFLOXACINO HEMI-HIDRATADO',
    'LEVOFLOXACINO HEMIIDRATADO',
    'AMOXICILINA TRI-HIDRATADA + LANSOPRAZOL + LEVOFLOXACINO HEMI-HIDRATADO',
    'OFLOXACINO',
    'CLORIDRATO DE MOXIFLOXACINO + FOSFATO DISSÓDICO DE DEXAMETASONA',
    'CLORIDRATO DE MOXIFLOXACINO',
    'NORFLOXACINO',
    'GATIFLOXACINO',
    'ACETATO DE PREDNISOLONA + GATIFLOXACINO SESQUI-HIDRATADO',
    'CLORIDRATO DE BESIFLOXACINO',
    'CEFOXITINA',
    'CEFOXITINA SÓDICA',
    'CEFTAZIDIMA'
);
