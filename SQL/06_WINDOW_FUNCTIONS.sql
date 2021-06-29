-- https://www.postgresql.org/docs/9.1/tutorial-window.html
-- https://www.postgresql.org/docs/8.4/functions-window.html

-- OVER (PARTITION BY column) AS column_name
-- OVER cria janelas sem que precisemos agrupar as demais variáveis
-- o número de linhas retornado com OVER é o mesmo de uma busca sem agrupamentos
-- PARTITION BY(), agrupa segundo a variável escolhida

-- exemplo:
-- SELECT standard_qty, SUM(standard_qty) OVER (PARTITION BY DATE_TRUNC('month', occurred_at)) AS running_total
-- FROM orders

-- a QUERY acima retornaria a 'standard_qty' e a SUM de 'standard_qty' relacionado ao pedido de cada mês,
-- ou seja, todos os pedidos feitos no mesmo mês teriam a mesma SUM

-- 01 QUIZ

-- 01
-- crie uma coluna 'running_total' sobre o 'standard_amt_usd' de acordo a data (occurred_at) SEM TRUNCAMENTOS
SELECT standard_amt_usd, SUM(standard_amt_usd) OVER (ORDER BY occurred_at) AS running_total
FROM orders
-- as duas colunas provavelmente são idênticas, pois a data sem truncamento gera valores únicos de horário

-- 02
-- adicionar data truncada no ano e PARTICIONAR pelo mesmo ano truncado
SELECT standard_amt_usd, DATE_TRUNC('year', occurred_at),
    SUM(standard_amt_usd) OVER (PARTITION BY DATE_TRUNC('year', occurred_at) ORDER BY occurred_at) AS running_total
FROM orders

-- se deixarmos a QUERY do jeito que está acima, com o 'ORDER BY occurred_at', a coluna 'running_total'
-- apresentará o valor somado progressivo de cada pedido, até o fim de cada ano
-- porém, se retirarmos o 'ORDER BY occurred_at', a coluna 'running_total' de cada pedido terá o MESMO VALOR para o mesmo ano

-------------------------------------------------------------------
-- ROW_NUMBER(): enumera as linhas, pode ser usado com OVER()
-- ROW_NUMER() OVER(ORDER BY column) AS column_name, nesse caso, enumera na sequência da coluna ordenada
-- RANK(), similar a ROW_NUMBER(), porém, caso possua mesmo valor na 'column', RANK() atribui o mesmo número da linha

-- 02 QUIZ

-- 01
-- selecionar id, account_id e total, então rankear o total de papel pedido (maior p menor) para cada 'account'
SELECT id, account_id, total,
       RANK() OVER(PARTITION BY account_id ORDER BY total DESC) AS total_rank
FROM orders 


-- comparação COM e SEM 'ORDER BY'
SELECT id,
       account_id,
       standard_qty,
       DATE_TRUNC('month', occurred_at) AS month,
       DENSE_RANK() OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month',occurred_at)) AS dense_rank,
       SUM(standard_qty) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month',occurred_at)) AS sum_std_qty,
       COUNT(standard_qty) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month',occurred_at)) AS count_std_qty,
       AVG(standard_qty) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month',occurred_at)) AS avg_std_qty,
       MIN(standard_qty) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month',occurred_at)) AS min_std_qty,
       MAX(standard_qty) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month',occurred_at)) AS max_std_qty
FROM orders

SELECT id,
       account_id,
       standard_qty,
       DATE_TRUNC('month', occurred_at) AS month,
       DENSE_RANK() OVER (PARTITION BY account_id) AS dense_rank,
       SUM(standard_qty) OVER (PARTITION BY account_id) AS sum_std_qty,
       COUNT(standard_qty) OVER (PARTITION BY account_id) AS count_std_qty,
       AVG(standard_qty) OVER (PARTITION BY account_id) AS avg_std_qty,
       MIN(standard_qty) OVER (PARTITION BY account_id) AS min_std_qty,
       MAX(standard_qty) OVER (PARTITION BY account_id) AS max_std_qty
FROM orders

-- Ao retirarmos o 'ORDER BY' da janela, cada valor da coluna é uma simples agregação do 'standard_qty'
-- com o respectivo 'account_id'. Em contrapartida, usando-se o ORDER BY acima, as colunas serão ordenadas
-- de acordo com o mês ao qual pertencem, deixando a informação mais legível.

--------------------------------------------------------------------------------
-- WINDOW CLAUSE: entre o 'WHERE' e o 'GROUP BY'
-- example:
-- WINDOW window_name AS (PARTITION BY account_id ORDER BY DATE_TRUNC('month',occurred_at))

-- 03 QUIZ

-- 01
-- renomear as janelas do exercício com 'account_year_window':
SELECT id,
       account_id,
       DATE_TRUNC('year',occurred_at) AS year,
       DENSE_RANK() OVER account_year_window AS dense_rank,
       total_amt_usd,
       SUM(total_amt_usd) OVER account_year_window AS sum_total_amt_usd,
       COUNT(total_amt_usd) OVER account_year_window AS count_total_amt_usd,
       AVG(total_amt_usd) OVER account_year_window AS avg_total_amt_usd,
       MIN(total_amt_usd) OVER account_year_window AS min_total_amt_usd,
       MAX(total_amt_usd) OVER account_year_window AS max_total_amt_usd
FROM orders
WINDOW account_year_window AS (PARTITION BY account_id ORDER BY DATE_TRUNC('year',occurred_at))