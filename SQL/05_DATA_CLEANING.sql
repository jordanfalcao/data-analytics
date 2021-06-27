-- LEFT     - retorna um número específico de caracteres, começando do início
-- RIGHT    - retorna um número específico de caracteres, começando do fim
-- LENGTH   - retorna o número de caracteres de cada coluna da coluna especificada

-- 01 QUIZ

-- 01
-- quantos de cada tipo diferentes de website existem na tabela 'account'
SELECT RIGHT(website, 3) AS address_type, COUNT(*)
FROM accounts a
GROUP BY 1

-- 02
-- retorne a primeira letra de cada conta e veja a distribuição de empresas que começam com cada letra/número
SELECT LEFT(name, 1) AS first_letter, COUNT(*)
FROM accounts
GROUP BY 1
ORDER BY 2 DESC

-- 03
-- criar duas colunas, uma com as empresas que começam o nome com um número e outro que começa com letra
-- qual a proporção?
WITH t1 AS (  -- criamos duas colunas se é num ou não
    SELECT CASE WHEN LEFT(name, 1) IN ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9') THEN 1 ELSE 0 END AS num,
           CASE WHEN LEFT(name, 1) IN ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9') THEN 0 ELSE 1 END AS letter
    FROM accounts
)    
SELECT SUM(num) AS total_num, SUM(letter) AS total_letter
FROM t1

-- 04
--
WITH t1 AS (
    SELECT CASE WHEN LEFT(name, 1) IN ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U') THEN 1 ELSE 0 END AS vowel,
           CASE WHEN LEFT(name, 1) IN ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U') THEN 0 ELSE 1 END AS not_vowel
FROM accounts
)
SELECT SUM(vowel) AS total_vowel, SUM(not_vowel) AS total_others
FROM t1