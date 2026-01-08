-- In 13.sql, write a SQL query to explore a question of your choice. This query should:
-- Involve at least one condition, using WHERE with AND or OR

SELECT * from episodes where season = "1"  AND (title like 'R%' or topic like 'm%');