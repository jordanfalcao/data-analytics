-- 01 QUIZ

-- média dos eventos em cada canal por dia
SELECT channel, AVG(num_events) AS avg_events_per_day
FROM(
SELECT DATE_TRUNC('day', occurred_at) AS day, channel, COUNT(*) AS num_events
FROM web_events
GROUP BY 1, 2) AS t1
GROUP BY 1
ORDER BY 2;

