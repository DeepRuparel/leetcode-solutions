# Write your MySQL query statement below
select customer_id , COUNT(v.visit_id) as count_no_trans
FROM visits v
LEFT JOIN transactions t
on v.visit_id = t.visit_id
WHERE transaction_id is NULL
GROUP BY customer_id