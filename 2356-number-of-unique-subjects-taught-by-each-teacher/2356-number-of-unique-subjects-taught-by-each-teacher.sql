# Write your MySQL query statement below

select teacher_id , COUNT(DISTINCT(subject_id)) as cnt
FROM teacher
GROUP BY teacher_id
