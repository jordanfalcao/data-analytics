-- FULL OUTER JOIN
-- FULL OUTER JOIN Table_B ON Table_A.column_name = Table_B.column_name;

-- quando se quer apenas os que não atendem a condição do ON:
-- WHERE Table_A.column_name IS NULL OR Table_B.column_name IS NULL

-- 01 QUIZ

-- 01
-- cada 'account' que tem um 'sales_rep' e vice-versa
SELECT a.name AS account, s.name AS sales_reps
FROM accounts a 
FULL JOIN sales_reps s 
ON s.id = a.sales_rep_id    -- todas as contas tem representante

-- 02
-- cada 'account' que NÃO tem um 'sales_rep' e vice-versa
SELECT a.name AS account, s.name AS sales_reps
FROM accounts a 
FULL JOIN sales_reps s 
ON s.id = a.sales_rep_id
WHERE (s.id IS NULL OR a.sales_rep_id IS NULL)  -- vazio


-- 02 QUIZ


-- 01
-- QUERY com LEFT JOIN das 'accounts' com a tabela 'sales_reps', junte isso usando 'accounts.primary_poc < sales_reps.name'
SELECT a.name AS account, a.primary_poc, s.name AS sales_reps 
FROM accounts a 
LEFT JOIN sales_reps s 
ON s.id = a.sales_rep_id
AND a.primary_poc < s.name  -- apenas as contas com o 'primary_poc' alfabeticamente antes do s.name


-- 03  QUIZ

-- 01
-- modificar a QUERY do video para 'web_events' ocorridos no máximo 1 dia após do outro
SELECT w1.id AS w1_id,
       w1.account_id AS w1_account_id,
       w1.occurred_at AS w1_occurred_at,
       w1.channel AS w1_channel,
       w2.id AS w2_id,
       w2.account_id AS w2_account_id,
       w2.occurred_at AS w2_occurred_at,
       w2.channel AS w2_channel
  FROM web_events w1
 LEFT JOIN web_events w2
   ON w1.account_id = w2.account_id
  AND w2.occurred_at > w1.occurred_at
  AND w2.occurred_at <= w1.occurred_at + INTERVAL '1 days'
ORDER BY w1.account_id, w1.occurred_at 