-- In 12.sql, count the number of unique episode titles.

select * from episodes;

SELECT COUNT(DISTINCT title) from episodes;
