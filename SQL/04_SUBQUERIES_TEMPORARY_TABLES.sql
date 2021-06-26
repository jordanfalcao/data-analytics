-- 01 
-- média dos eventos em cada canal por dia
SELECT channel, AVG(num_events) AS avg_events_per_day
FROM(SELECT DATE_TRUNC('day', occurred_at) AS day, channel, COUNT(*) AS num_events
     FROM web_events
     GROUP BY 1, 2) AS t1
GROUP BY 1
ORDER BY 2;

-- 02
-- médias das quantidas de cada tipo de papel pedida no mês do primeiro pedido feito
SELECT  AVG(standard_qty) AS avg_standard, AVG(poster_qty) AS avg_poster, AVG(gloss_qty) AS avg_gloss
FROM orders
WHERE DATE_TRUNC('month', occurred_at) =
                     (SELECT DATE_TRUNC('month', MIN(occurred_at))
                     FROM orders);

-- valor total gasto no mês do primeiro pedido feito
SELECT SUM(total_amt_usd)
FROM orders
WHERE DATE_TRUNC('month', occurred_at) = 
                     (SELECT DATE_TRUNC('month', MIN(occurred_at)) FROM orders);


                    
-- 01 QUIZ

-- 01
-- o nome do representante em cada região com o maior valor vendido
SELECT t3.sales_rep, t3.region, t2.max_total_amnt_usd
FROM(SELECT region, MAX(total_amt_usd) AS max_total_amnt_usd
    FROM(SELECT s.name AS sales_rep, r.name AS region, SUM(o.total_amt_usd) AS total_amt_usd
	    FROM region r
	    JOIN sales_reps s
	    ON r.id = s.region_id
	    JOIN accounts a
	    ON s.id = a.sales_rep_id
	    JOIN orders o
	    ON a.id = o.account_id
	    GROUP BY s.name, r.name) AS t1
    GROUP BY 1
    ORDER BY 2 DESC) AS t2
 JOIN (SELECT s.name AS sales_rep, r.name AS region, SUM(o.total_amt_usd) AS total_amt_usd
	FROM region r
	JOIN sales_reps s
	ON r.id = s.region_id
	JOIN accounts a
	ON s.id = a.sales_rep_id
	JOIN orders o
	ON a.id = o.account_id
	GROUP BY s.name, r.name) AS t3
ON t3.region = t2.region AND t3.total_amt_usd = t2.max_total_amnt_usd
ORDER BY 3 DESC;

-- 02
-- quantos pedidos foram feitos na região com maior 'total_amt_usd'
SELECT r.name AS region, COUNT(o.total) AS total_orders
FROM region r
JOIN sales_reps s
ON r.id = s.region_id
JOIN accounts a
ON s.id = a.sales_rep_id
JOIN orders o
ON a.id = o.account_id
GROUP BY 1
HAVING SUM(o.total_amt_usd) = (
        SELECT MAX(total_amt_usd) AS total_amt   -- primeiro pega-se o valor total da região que mais vendeu
        FROM(SELECT r.name AS region, SUM(o.total_amt_usd) AS total_amt_usd
	        FROM region r
	        JOIN sales_reps s
	        ON r.id = s.region_id
	        JOIN accounts a
	        ON s.id = a.sales_rep_id
	        JOIN orders o
	        ON a.id = o.account_id
	        GROUP BY r.name) AS t1)


-- 03
-- Quantas contas tiveram mais compras totais do que o nome da conta que comprou mais standard_qty
SELECT COUNT(*)
FROM(
    SELECT a.name
    FROM orders o 
    JOIN accounts a 
    ON a.id = o.account_id
    GROUP BY 1
    HAVING SUM(o.total) > (SELECT total
                        FROM(SELECT a.name AS account_name, SUM(o.standard_qty) AS total_std, SUM(o.total) AS total
                                FROM orders o
                                JOIN accounts a
                                ON a.id = o.account_id
                                GROUP BY 1
                                ORDER BY 2 DESC
                                LIMIT 1) As t1)) t2

-- 04
-- para o cliente que gastou maior valor 'total_amt_usd', quantos 'web_events' para cada 'channel'
SELECT a.name, w.channel, COUNT(*)
FROM accounts a
JOIN web_events w 
ON a.id = w.account_id
AND a.id = (SELECT id
            FROM(SELECT a.id, a.name, SUM(total_amt_usd) AS total_amt
                FROM orders o
                JOIN accounts a
                ON a.id = o.account_id
                GROUP BY 1, 2
                ORDER BY 3 DESC
                LIMIT 1) AS t1)
GROUP BY 1, 2;

-- 05
-- qual a média de gasto das 10 contas que mais gastaram
SELECT AVG(total_amt)
FROM(SELECT a.name, SUM(total_amt_usd) AS total_amt
FROM orders o
JOIN accounts a
ON a.id = o.account_id
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10) AS t1

-- 06
-- média de 'total_amt_usd' apenas das contas que gastaram mais que a média de todos os pedidos
SELECT AVG(avg_amt) AS total_avg_amt
FROM(SELECT a.id, AVG(o.total_amt_usd) AS avg_amt
    FROM orders o
    JOIN accounts a
    ON a.id = o.account_id
    GROUP BY 1
    HAVING AVG(total_amt_usd) > (SELECT AVG(total_amt_usd) avg_all
		FROM orders)) AS t1




