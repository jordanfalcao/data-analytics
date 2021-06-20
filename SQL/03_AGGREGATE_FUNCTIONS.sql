-- COUNT
-- retorna a quantidade de linhas NÃO NULAS
SELECT COUNT(*) AS order_count
FROM orders;


-- SUM
-- retorna a soma de valores NÚMERICOS e NÃO NULOS
SELECT SUM(standard_qty) AS standard_qty
FROM orders;


-- 01 QUIZ

-- total de vendas de poster paper
SELECT SUM(poster_qty) total_poster_sales
FROM orders;

-- total de vendas de standard paper
SELECT SUM(standard_qty) total_standard_sales
FROM orders;

-- valor total vendido (USD)
SELECT SUM(total_amt_usd) total_dollar_sales
FROM orders;

-- valor total do standar e gloss paper (USD), separadamente
SELECT SUM(standard_amt_usd) standard_total, 
SUM(gloss_amt_usd) gloos_total
FROM orders;

-- preço por unidade do standard paper
SELECT SUM(standard_amt_usd)/ SUM(standard_qty) AS standard_price_per_unit
FROM orders;


-- MIN e MAX
-- retorna o mínimo e o máximo, respectivamente, da coluna indicada
-- pode receber como parâmetro um NÚMERO, uma DATA ou uma STRING (ordem alfabética)


-- AVG
-- retorna a média da coluna indicada, apenas valores NUMÉRICOS
-- ignora colunas NULL


-- 02 QUIZ

-- 01
-- pedido mais antigo
SELECT MIN(occurred_at)
FROM orders;

-- 02
-- mesma questão acima sem usar aggregation function
SELECT occurred_at
FROM orders
ORDER BY occurred_at
LIMIT 1;

-- 03
-- quando o web event mais recente ocorreu
SELECT MAX(occurred_at)
FROM web_events;

-- 04
-- mesma questão acima sem aggregation function
SELECT occurred_at
FROM web_events
ORDER BY occurred_at DESC
LIMIT 1;

-- 05
-- média dos valores dos pedidos e média da quentidade pedida de cada tipo de papel
SELECT AVG(standard_amt_usd) avg_standard, AVG(gloss_amt_usd) avg_gloss, AVG(poster_amt_usd) avg_poster, 
       AVG(standard_qty) avg_standard_qty, AVG(gloss_qty) avg_gloss_qty, AVG(poster_qty) avg_poster_qty
FROM orders;

-- 06
-- mediana na gambiarra, SQL não calcula mediana
SELECT *
FROM (SELECT total_amt_usd
      FROM orders
      ORDER BY total_amt_usd
      LIMIT 3457) AS Table1  -- 3456 é metade dos valores
ORDER BY total_amt_usd DESC
LIMIT 2; -- pegamos o resultado e tiramos a média


-- GROUP BY

-- 03 QUIZ

-- 01
-- nome da conta que fez o pedido mais antigo
SELECT a.name, o.occurred_at
FROM accounts a
JOIN orders o
ON a.id = o.account_id
ORDER BY o.occurred_at
LIMIT 1;

-- 02
-- total de valor gasto por cada conta
SELECT a.name, SUM(o.total_amt_usd) total_amt_usd_per_account
FROM accounts a
JOIN orders o
ON a.id = o.account_id
GROUP BY a.name

-- 03
-- qual canal e conta associada ao web event mais recente
SELECT w.occurred_at, w.channel, a.name
FROM web_events w
JOIN accounts a
ON a.id = w.account_id
ORDER BY w.occurred_at DESC
LIMIT 1;

-- 04
-- quantas vezes cada canal dos eventos web foram usados
SELECT w.channel, COUNT(w.channel)
FROM web_events w
GROUP BY w.channel;

-- 05
-- o contato principal associado ao evento mais antigo
SELECT a.primary_poc
FROM web_events w
JOIN accounts a
ON a.id = w.account_id
ORDER BY w.occurred_at
LIMIT 1

-- 06
-- valor mínimo pedido por cada conta, ordernar pelo menor valor
SELECT a.name, MIN(o.total_amt_usd) smallest_order
FROM accounts a
JOIN orders o
ON a.id = o.account_id
GROUP BY a.name
ORDER BY smallest_order;

-- 07
-- quantidade de representantes em cada região, ordernar da menor quantidade para a maior
SELECT r.name, COUNT(*) num_reps
FROM sales_reps s
JOIN region r
ON r.id = s.region_id
GROUP BY r.name
ORDER BY num_reps;