-- 01 
-- média dos eventos em cada canal por dia
SELECT channel, AVG(num_events) AS avg_events_per_day
FROM(SELECT DATE_TRUNC('day', occurred_at) AS day, channel, COUNT(*) AS num_events
     FROM web_events
     GROUP BY 1, 2) AS t1
GROUP BY 1
ORDER BY 2;

-- 02
-- médias das quantidas de cada tipo de papel pedida no primeiro mês de pedido feito
SELECT  AVG(standard_qty) AS avg_standard, AVG(poster_qty) AS avg_poster, AVG(gloss_qty) AS avg_gloss
FROM orders
WHERE DATE_TRUNC('month', occurred_at) =
                     (SELECT DATE_TRUNC('month', MIN(occurred_at))
                     FROM orders);

-- valor total gasto no primeiro mês de pedido feito
SELECT SUM(total_amt_usd)
FROM orders
WHERE DATE_TRUNC('month', occurred_at) = 
                     (SELECT DATE_TRUNC('month', MIN(occurred_at)) FROM orders);